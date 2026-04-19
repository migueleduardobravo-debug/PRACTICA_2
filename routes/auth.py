from db import get_users_connection, hash_password
from flask import request, redirect, render_template, session, flash
from server import app
from urllib.parse import urlparse

@app.route('/login', methods=['GET', 'POST'])
def login():
    # 1. Verificar si ya está logueado
    if 'username' in session:
        return redirect('/dashboard')

    next_url = request.args.get('next') or '/dashboard'

    if request.method == 'POST':
        # --- TODO ESTO DEBE ESTAR INDENTADO (CON 8 ESPACIOS) ---
        username = request.form['username']
        password = request.form['password']
        
        conn = get_users_connection()
        
        # FIX: Consultas parametrizadas (CWE-89) y Hashing seguro (CWE-327)
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        user = conn.execute(query, (username, hash_password(password))).fetchone()
        conn.close()

        if user:
            session['user_id'] = user['id']
            session['username'] = user['username']
            session['role'] = user['role']
            session['permanent'] = True
            
            # Protección contra Open Redirect (CWE-601)
            if not next_url or urlparse(next_url).netloc != '':
                next_url = '/dashboard'
            return redirect(next_url)
        else:
            flash("Invalid username or password", "danger")
            return render_template('auth/login.html', next_url=next_url)
        # -------------------------------------------------------

    # Si es un GET, simplemente mostramos el login
    return render_template('auth/login.html', next_url=next_url)
