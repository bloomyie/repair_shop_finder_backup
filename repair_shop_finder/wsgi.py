import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'repair_shop_finder.settings')

application = get_wsgi_application()
