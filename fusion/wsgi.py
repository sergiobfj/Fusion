import os
import sys
import traceback

print(">>> Iniciando WSGI...", file=sys.stderr)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fusion.settings')

try:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    print("✅ Django carregado com sucesso!", file=sys.stderr)
except Exception:
    print("❌ Erro ao iniciar Django:", file=sys.stderr)
    traceback.print_exc(file=sys.stderr)
    # Rethrow o erro pra Vercel registrar o 500
    raise
