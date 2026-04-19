from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'supersecretkey'
# Configuración de Seguridad de Sesión
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,  # Impide que JavaScript acceda a la cookie (Mitiga XSS)
    SESSION_COOKIE_SECURE=False,
    SESSION_COOKIE_SAMESITE='Lax', # Protege contra ataques CSRF
    PERMANENT_SESSION_LIFETIME=1800 # Sesión expira en 30 min de inactividad (más seguro)
)
@app.errorhandler(404)
def not_found(e):
    return render_template('errors/404.html'), 404

@app.errorhandler(403)
def forbidden(e):
    return render_template('errors/403.html'), 403

@app.after_request
def set_security_headers(response):
    # Bloquea que la web se cargue en un iframe de otro sitio
    response.headers['X-Frame-Options'] = 'DENY'
    # Evita que el navegador intente adivinar el tipo de contenido (MIME Sniffing)
    response.headers['X-Content-Type-Options'] = 'nosniff'
    # Política básica de seguridad de contenido
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    # Oculta la versión del servidor
    response.headers['Server'] = 'Hidden'
    return response
