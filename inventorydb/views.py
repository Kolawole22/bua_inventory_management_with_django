from rest_framework import serializers
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Inventory
from .serializers import InventorySerializer
from rest_framework.views import exception_handler


class InventoryListCreateView(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def handle_response(self, serializer):
        # Customize the success message here
        success_message = 'Inventory created successfully'
        return Response(
            {'message': success_message, 'data': serializer.data},
            status=status.HTTP_201_CREATED,
            headers=self.get_success_headers(serializer.data)
        )

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return self.handle_response(serializer)
        except serializers.ValidationError as exc:
            # Handle validation error and customize the error response
            return self.handle_exception(exc)

    def handle_exception(self, exc):
        response = super().handle_exception(exc)

        if isinstance(exc, serializers.ValidationError):
            # Customize the error response for validation errors
            error_message = 'Invalid data. Please check the input.'
            response.data = {'error': error_message, 'details': exc.detail}

        return response


class InventoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def handle_response(self, serializer):
        # Customize the success message here
        success_message = 'Inventory updated successfully'
        return Response(
            {'message': success_message, 'data': serializer.data},
            status=status.HTTP_200_OK,

        )

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return self.handle_response(serializer)
        except serializers.ValidationError as exc:
            # Handle validation error and customize the error response
            return self.handle_exception(exc)

    def handle_exception(self, exc):
        response = super().handle_exception(exc)

        if isinstance(exc, serializers.ValidationError):
            # Customize the error response for validation errors
            error_message = 'Invalid data. Please check the input.'
            response.data = {'error': error_message, 'details': exc.detail}

        return response


class AssignedInventoryListView(generics.ListAPIView):
    queryset = Inventory.objects.filter(assigned=True)
    serializer_class = InventorySerializer


class UnassignedInventoryListView(generics.ListAPIView):
    queryset = Inventory.objects.filter(assigned=False)
    serializer_class = InventorySerializer


class CustomInventoryView(APIView):
    def get(self, request):
        inventories = Inventory.objects.all()
        serializer = InventorySerializer(inventories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
