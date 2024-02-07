# import logging
# from django_db_logger.db_log_handler import DatabaseLogHandler

# logger = logging.getLogger(__name__)
# # Add this line to include DatabaseLogHandler
# logger.addHandler(DatabaseLogHandler())


# class APILoggingMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         user = request.user
#         method = request.method
#         path = request.path

#         # Log API requests to the database using the db_log handler
#         if method in ['POST', 'PUT', 'PATCH']:
#             changes_made = f"Data: {request.data}"

#             logger.info(
#                 f'API {method} request to {path} by user: {user.username}. Changes made: {changes_made}',
#                 extra={'request': request}
#             )

#         response = self.get_response(request)
#         return response
