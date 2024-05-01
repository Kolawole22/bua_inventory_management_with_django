"""
ASGI config for buaInventory project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

from uvicorn import run
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'buaInventory.settings')

# django_asgi_app = get_asgi_application()

application = get_asgi_application()


# if __name__ == '__main__':
#     run(django_asgi_app, host='0.0.0.0', port=8000)
