# 🛡️ Company Management Platform - Remediación de Seguridad

Este repositorio contiene la auditoría técnica y la remediación de vulnerabilidades de la plataforma de gestión de NovaCorp, realizada
por Miguel Eduardo Bravo como parte del Máster en Ciberseguridad.

## 📋 Resumen del Proyecto
Se ha transformado una aplicación con múltiples vulnerabilidades críticas (SQLi, XSS, MD5) en un sistema endurecido siguiendo estándares **OWASP Top 10**.

## 🚀 Instrucciones de Ejecución (Setup Seguro)

### 1. Preparar el entorno
Es fundamental usar un entorno virtual para aislar las dependencias:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# NovaCorp — Company Management Platform

**NovaCorp Platform** is an internal web application for managing companies and their associated comments. It supports three roles (`admin`, `owner`, `user`) with different access levels.

---

## Installation

```bash
pip install -r requirements.txt
python main.py
```

Visit: `http://127.0.0.1:5000`

The database is automatically initialized on first run.

---

## Default Users

| Username | Password   | Role   | Notes                      |
|----------|------------|--------|----------------------------|
| `alice`  | password1  | user   | Standard employee          |
| `bob`    | password2  | owner  | Owns "Insegura Corp"       |
| `admin`  | admin123   | admin  | Full access                |

---

## Project Structure

```
.
├── main.py                 # Entry point
├── server.py               # Flask app configuration
├── db/
│   └── __init__.py         # Database initialization and helpers
├── routes/
│   ├── auth.py             # Login/logout
│   ├── companies.py        # Company views, dashboard, search
│   ├── companies_admin.py  # Admin company management
│   ├── users_admin.py      # Admin user management
│   └── profile.py          # User profiles
├── templates/
│   ├── base.html           # Shared layout
│   ├── dashboard.html      # Main dashboard
│   ├── auth/               # Login page
│   ├── companies/          # Company pages
│   ├── admin/              # Admin panels
│   ├── profile/            # User profile pages
│   └── errors/             # 404, 403 pages
├── static/
│   └── css/style.css       # Custom styles
└── requirements.txt
```

---

## Technologies

- Python 3 + Flask
- SQLite
- Bootstrap 5.3
- Jinja2 + Bootstrap Icons
Prueba de firma GPG realizada el Fri Apr 17 19:12:17 CEST 2026
