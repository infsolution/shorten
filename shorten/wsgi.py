"""
WSGI config for shorten project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import time
import traceback
import signal
import sys

from django.core.wsgi import get_wsgi_application
sys.path.append('/var/www/html/shorten/')
sys.path.append('/var/www/html/tkvenv/lib/python3.5/site-packages')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shorten.settings")


try:
	application = get_wsgi_application()
except Exception:
	if 'mod_wsgi' in sys.modules:
		traceback.print_exc()
		os.kill(os.getpid(), signal.SIGINT)
		TIME.SLEEP(2.5)
