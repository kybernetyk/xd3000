import os,sys
apache_configuration = os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

sys.path.append('/home/xd3000')
sys.path.append('/home/xd3000/xd3000')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xd3000.settings")

#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

