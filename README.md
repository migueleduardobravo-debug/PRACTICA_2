# Company Management Platform - Remediación de Seguridad

Link del repositorio: https://github.com/migueleduardobravo-debug/PRACTICA_2

Este repositorio contiene la versión auditada y saneada de la plataforma de gestión de NovaCorp. La remediación se ha centrado en mitigar vulnerabilidades críticas de Inyección SQL y deficiencias en el manejo de sesiones y criptografía.

## Seguridad e Integridad
- **Commits Firmados:** Todos los commits de este repositorio han sido firmados digitalmente mediante GPG para asegurar la trazabilidad y autoría de los cambios.
- **Análisis SAST:** El código ha sido verificado con Bandit, alcanzando una puntuación de "0 hallazgos" de severidad Alta/Media.

## Tecnologías Utilizadas
- **Lenguaje:** Python 3.x
- **Framework:** Flask
- **Base de Datos:** SQLite
- **Hashing:** PBKDF2 con SHA-256 (vía Werkzeug)

## Instrucciones de Ejecución

### 1. Clonar y configurar entorno

# 🛡️ Company Management Platform - Remediación de Seguridad

Este repositorio contiene la auditoría técnica y la remediación de vulnerabilidades de la plataforma de gestión de NovaCorp, realizada como parte del Máster en Ciberseguridad.

## 📋 Resumen del Proyecto
Se ha transformado una aplicación con múltiples vulnerabilidades críticas (SQLi, XSS, MD5) en un sistema endurecido siguiendo estándares **OWASP Top 10**.

## 🚀 Instrucciones de Ejecución (Setup Seguro)

### 1. Preparar el entorno
Es fundamental usar un entorno virtual para aislar las dependencias:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
2. Reinicializar la Base de Datos Importante: Debido a la migración de MD5 a PBKDF2-SHA256, las contraseñas antiguas no funcionarán. Debes resetear la DB para aplicar el nuevo hashing:Bashpython3 init_db.py
3. Lanzar la aplicaciónBashpython3 main.py
Acceso local: http://localhost:5000 Medidas de Seguridad ImplementadasCategoríaMejora RealizadaAutenticaciónEliminación de SQL Injection mediante consultas parametrizadas.CriptografíaMigración de MD5 a PBKDF2 con Salting automático.SesionesFlags HttpOnly, SameSite y desactivación de Modo Debug.FrontendEliminación de filtros `RedireccionesValidación de rutas relativas para prevenir Open Redirects.🛠️ Auditoría y TrazabilidadAnálisis SAST: Verificado con Bandit (0 hallazgos críticos tras remediación).Integridad: Todos los commits están firmados digitalmente con GPG para garantizar la autoría de las correcciones.Análisis Manual: Identificación de fallos de lógica no detectados por herramientas automáticas.👤 AutorMiguel Eduardo Bravo - Especialista en Ciberseguridad
Inicializar Base de Datos
Es necesario reinicializar la base de datos para generar las tablas con el nuevo formato de hashing seguro (PBKDF2):

Bash
python3 init_db.py
 Ejecutar Aplicación
Bash
python3 main.py
La aplicación estará disponible en http://localhost:5000.

 Estructura del Proyecto
app/: Código fuente de la aplicación.

db/: Lógica de acceso a datos y hashing seguro.

routes/: Controladores con lógica de negocio y validación de parámetros.

templates/: Plantillas Jinja2 con sanitización manual (eliminación de filtros |safe).

 Autor
Miguel Eduardo Bravo - Máster en Ciberseguridad.
