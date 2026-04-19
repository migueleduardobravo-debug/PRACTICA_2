from server import app
from routes import auth, companies, companies_admin, users_admin, profile

if __name__ == '__main__':
    # Cambiamos debug a False para cumplir con estándares de producción
    app.run(debug=False, port=5000)
