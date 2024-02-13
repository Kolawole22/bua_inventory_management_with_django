import os

import sys

import site

from django.core.wsgi import get_wsgi_application

# Add the app’s directory to the PYTHONPATH

sys.path.append("C:\Users\HR\projects\react\bua-inventory-management\backend\buaInventory\inventorydb")

#sys.path.append(‘C:/Users/myuser/Desktop/charts_django/dashboard/Census_Dashboard/dashboard/board’)

os.environ["DJANGO_SETTINGS_MODULE"] = "inventorydb.settings"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "inventorydb.settings")

application = get_wsgi_application()