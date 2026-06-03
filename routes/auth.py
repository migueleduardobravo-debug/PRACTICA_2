from db import get_users_connection
from flask import request, redirect, render_template, session, flash
from server import app
from urllib.parse import urlparse
from werkzeug.security import check_password_hash

def _safe_next_url(candidate):
    if not candidate:
        return '/dashboard'
    parsed = urlparse(candidate)
    if parsed.scheme or parsed.netloc:
        return '/dashboard'
    if not candidate.startswith('/') or candidate.startswith('//'):
        return '/dashboard'
    return candidate

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect('/dashboard')

    next_url = _safe_next_url(request.args.get('next'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        submitted_password = request.form.get('password', '')

        conn = get_users_connection()
        user = conn.execute(
            "SELECT id, username, password, role, company_id FROM users WHERE username = ?",
            (username,),
        ).fetchone()
        conn.close()

        if user and check_password_hash(user['password'], submitted_password):
            session.permanent = True
            session['user_id']    = user['id']
            session['username']   = user['username']
            session['role']       = user['role']
            session['company_id'] = user['company_id']
            return redirect(next_url)
        else:
            flash("Invalid username or password", "danger")

    return render_template('auth/login.html', next_url=next_url)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')
