# Company Management Platform — Remediación SAST
**UNIE Universidad — Máster en Ciberseguridad — Actividad 2**
Auditor: Miguel Eduardo Bravo Figueroa | Sentinel Security Partners

## Instalación
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install flask-wtf
export FLASK_SECRET_KEY=$(python3 -c "import secrets; print(secrets.token_hex(32))")
python3 main.py
```

## Acceso
http://localhost:5000

| Usuario | Contraseña | Rol   |
|---------|------------|-------|
| alice   | password1  | user  |
| bob     | password2  | owner |
| admin   | admin123   | admin |

## Vulnerabilidades remediadas
16 hallazgos — VULN-01 a VULN-16 — ver informe de auditoría PDF para detalle completo.

## Herramientas utilizadas
- SAST: Bandit 1.7+
- Framework: Flask 2.2 + SQLite + Jinja2
- Commits firmados con GPG

## Repositorio GitHub
https://github.com/migueleduardobravo-debug/PRACTICA_2
