"""
WSGI config for n2k_1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("python manage.py startapp polls", "n2k_1.settings")

application = get_wsgi_application()
