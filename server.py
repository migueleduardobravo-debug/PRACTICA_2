from flask import Flask, render_template
from flask_wtf import CSRFProtect
from flask_wtf.csrf import CSRFError
import os

app = Flask(__name__)

def _load_secret_key():
    secret = os.environ.get('FLASK_SECRET_KEY')
    if not secret:
        raise RuntimeError(
            'FLASK_SECRET_KEY no esta definida. '
            'Genera una con: python3 -c "import secrets; print(secrets.token_hex(32))" '
            'y exportala antes de arrancar la aplicacion.'
        )
    return secret

app.secret_key = _load_secret_key()

csrf = CSRFProtect(app)

@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('errors/403.html'), 403

def _truthy(var, default):
    value = os.environ.get(var)
    return default if value is None else value.strip().lower() in {'1', 'true', 'yes', 'on'}

app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SECURE=_truthy('SESSION_COOKIE_SECURE', False),
    SESSION_COOKIE_SAMESITE='Lax',
    PERMANENT_SESSION_LIFETIME=1800,
    MAX_CONTENT_LENGTH=1 * 1024 * 1024,
)

@app.errorhandler(404)
def not_found(e):
    return render_template('errors/404.html'), 404

@app.errorhandler(403)
def forbidden(e):
    return render_template('errors/403.html'), 403

@app.after_request
def set_security_headers(response):
    response.headers['X-Frame-Options']        = 'DENY'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Content-Security-Policy'] = "default-src 'self' https://cdn.jsdelivr.net https://fonts.googleapis.com https://fonts.gstatic.com; style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net; script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net"
    response.headers['Server']                 = 'Hidden'
    return response
