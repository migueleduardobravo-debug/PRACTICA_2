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

