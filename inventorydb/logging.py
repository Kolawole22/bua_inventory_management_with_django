# # logging.py

# from django.db import connection
# from django.db.utils import OperationalError
# from django.utils import timezone
# import logging
# from .models import APILog


# class DatabaseHandler(logging.Handler):
#     def emit(self, record):
#         try:
#             # Store logs in the database
#             api_type = record.api_type
#             user = record.user
#             changes_made = record.changes_made
#             created_at = timezone.now()

#             # Create an APILog instance
#             APILog.objects.create(
#                 api_type=api_type,
#                 user=user,
#                 changes_made=changes_made,
#                 created_at=created_at,
#             )
#         except OperationalError as e:
#             logger.error(f"OperationalError saving log to database: {e}")
#         except Exception as e:
#             logger.error(f"Error saving log to database: {e}")


# logger = logging.getLogger(__name__)
