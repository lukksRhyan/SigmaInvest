import os
from django.core.wsgi import get_wsgi_application

# Garante que o Django escute na porta correta do Railway
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SigmaInvest.settings')
os.environ.setdefault('PORT', '8000')  # Define um padrão para rodar localmente

application = get_wsgi_application()
