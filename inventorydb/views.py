from django.http import JsonResponse
from django.views import View
from rest_framework import serializers
from rest_framework import status
from rest_framework import generics
from django_filters import rest_framework as filters, DateRangeFilter
import django_filters
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Inventory, ActionLog
from .serializers import ActionLogSerializer, InventorySerializer, LoginSerializer
from rest_framework.views import exception_handler
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.pagination import PageNumberPagination
import logging
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import viewsets
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


# logger = logging.getLogger(__name__)


# def api_log_view(request):
#     try:
#         user = request.user
#         # Assuming you want to log the HTTP method (POST, PUT, PATCH)
#         api_type = request.method

#         # Only log POST, PUT, and PATCH requests
#         if api_type in ['POST', 'PUT', 'PATCH']:
#             changes_made = f"Data: {request.data}"

#             # Log relevant information to the file
#             logger.info(
#                 f"API {api_type} request by user: {user.username}. Changes made: {changes_made}")

#             # Log relevant information to the database using the custom DatabaseHandler
#             logger.info(
#                 f"API {api_type} request by user: {user.username}. Changes made: {changes_made}",
#                 extra={'api_type': api_type, 'user': user,
#                        'changes_made': changes_made}
#             )

#         # Your view logic here
#         return JsonResponse({'message': 'Success'})
#     except Exception as e:
#         # Handle exceptions
#         logger.error(f"Error processing API request: {str(e)}")
#         return JsonResponse({'error': str(e)}, status=500)


# @api_view(['POST'])


# @login_required
@api_view(['GET'])
def check_authentication(request):
    user = request.user
    if user.is_authenticated:
        return Response({'message': f"User {user.username} is authenticated"})
    else:
        return Response({'message': 'User is not authenticated'})


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        # serializer = LoginSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # user = serializer.validated_data
        user = authenticate(
            username=request.data['username'],
            password=request.data['password']
        )

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            })
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


# @api_view(['POST'])

class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({'message': 'Logout successful!'})


# class UserListView(generics.ListAPIView):
#     # permission_classes = [IsAuthenticated]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class InventoryFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(lookup_expr='icontains')
    subsidiary = django_filters.Filter()
    date = django_filters.DateFromToRangeFilter(field_name='date')

    class Meta:
        model = Inventory
        fields = ['user', 'subsidiary', 'location', 'assigned',
                  'tag_number', 'department', 'date', 'equipment']


class InventoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Inventory.objects.order_by('-date')
    serializer_class = InventorySerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = InventoryFilter
    pagination_class = PageNumberPagination

    def create(self, request, *args, **kwargs):
        try:
            serializer = InventorySerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            inventory_instance = serializer.save()
            # print('inventory instance: ', inventory_instance)

            self.send_email_notification(
                user=inventory_instance.user,
                email=inventory_instance.email,
                model=inventory_instance.model,
                equipment=inventory_instance.equipment,
                tag_number=inventory_instance.tag_number,
                subject='New Inventory Item Assigned',
                template=f'A new item has been assigned to you. Equipment: {inventory_instance.equipment}, Model: {inventory_instance.model}, Tag Number: {inventory_instance.tag_number}'
            )

            success_message = 'Inventory created successfully'
            return Response({'message': success_message, 'data': serializer.data}, status=status.HTTP_201_CREATED)
        except serializers.ValidationError as exc:
            error_message = 'Invalid data. Please check the input.'
            return Response({'message': error_message, 'details': exc.detail}, status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        instance = serializer.save()
        return instance

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            # if serializer.validated_data.get('user', '') == '' or serializer.validated_data.get('email', '') == '':
            #     # Handle the case where 'user' or 'email' is empty
            #     return Response({'error': 'User and email must not be empty'}, status=status.HTTP_400_BAD_REQUEST)

            updated_instance = self.perform_update(serializer)
            print('updated instance check: ', updated_instance)

            if updated_instance:
                print('updated instance email: ', updated_instance.email)
                self.send_email_notification(
                    user=updated_instance.user,
                    email=updated_instance.email,
                    model=updated_instance.model,
                    equipment=updated_instance.equipment,
                    tag_number=updated_instance.tag_number,
                    subject='Inventory Item Updated',
                    template=f'The details of an inventory item assigned to you have been updated. Model: {updated_instance.model}, Equipment Type: {updated_instance.equipment}, Tag Number: {updated_instance.tag_number}'
                )
            return self.handle_response(serializer)
        except serializers.ValidationError as exc:
            # Handle validation error and customize the error response
            return self.handle_exception(exc)

    def send_email_notification(self, user, email, model, equipment, tag_number, subject, template):
        if user is not None and email is not None:
            # Load your HTML templates from files
            new_item_assigned_template = render_to_string(
                'new_item_assigned_template.html', {'user': user, 'model': model, 'equipment': equipment, 'tag_number': tag_number, 'template': template})
            item_updated_template = render_to_string('item_updated_template.html', {
                                                     'user': user, 'model': model, 'equipment': equipment, 'tag_number': tag_number, 'template': template})

            # Select the appropriate template based on the subject
            if 'New Inventory Item Assigned' in subject:
                html_template = new_item_assigned_template
            elif 'Inventory Item Updated' in subject:
                html_template = item_updated_template
            else:
                # Default to a generic template if the subject doesn't match
                html_template = render_to_string('generic_template.html', {
                                                 'user': user, 'model': model, 'equipment': equipment, 'tag_number': tag_number, 'subject': subject, 'template': template})

            message = EmailMultiAlternatives(
                subject=subject,
                body='',  # Leave this empty as you're providing HTML content
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[email],
                alternatives=[(html_template, 'text/html')],
            )

            message.send(fail_silently=False)

    def handle_response(self, serializer):
        # Customize the success message here
        success_message = 'Inventory updated successfully'
        return Response(
            {'message': success_message, 'data': serializer.data},
            status=status.HTTP_200_OK,
        )

    def handle_exception(self, exc):
        response = super().handle_exception(exc)

        if isinstance(exc, serializers.ValidationError):
            # Customize the error response for validation errors
            error_message = 'Invalid data. Please check the input.'
            response.data = {'error': error_message, 'details': exc.detail}

        return response


# class ActionLogView(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = ActionLog.objects.all()
#     serializer_class = ActionLogSerializer


# class ActionLogDetailView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = ActionLog.objects.all()
#     serializer_class = ActionLogSerializer


class EmailAPI(APIView):
    def get(self, request):
        subject = self.request.GET.get('subject')
        txt_ = self.request.GET.get('text')
        html_ = self.request.GET.get('html')
        recipient_list = self.request.GET.get('recipient_list')
        from_email = settings.DEFAULT_FROM_EMAIL

        if subject is None and txt_ is None and html_ is None and recipient_list is None:
            return Response({'msg': 'There must be a subject, a recipient list, and either HTML or Text.'}, status=200)
        elif html_ is not None and txt_ is not None:
            return Response({'msg': 'You can either use HTML or Text.'}, status=200)
        elif html_ is None and txt_ is None:
            return Response({'msg': 'Either HTML or Text is required.'}, status=200)
        elif recipient_list is None:
            return Response({'msg': 'Recipient List required.'}, status=200)
        elif subject is None:
            return Response({'msg': 'Subject required.'}, status=200)
        else:
            sent_mail = send_mail(
                subject,
                txt_,
                from_email,
                recipient_list.split(','),
                html_message=html_,
                fail_silently=False,
            )
            return Response({'msg': sent_mail}, status=200)
