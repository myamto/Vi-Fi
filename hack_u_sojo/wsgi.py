"""
WSGI config for hack_u_sojo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hack_u_sojo.settings')

application = get_wsgi_application()

http_proxy  = "http://wwwproxy.itc.kansai-u.ac.jp:8080"
https_proxy = "http://wwwproxy.itc.kansai-u.ac.jp:8080"

proxyDict = {
              "http"  : http_proxy,
              "https" : https_proxy,
            }

os.environ["PROXIES"] = proxyDict
