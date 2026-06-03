from flask import request, redirect, render_template, session, flash
from server import app
from db import get_users_connection, get_data_connection, hash_password

ALLOWED_ROLES = {'user', 'owner', 'admin'}

@app.route('/admin/users')
def admin_users():
    if session.get('role') != 'admin':
        return render_template('errors/403.html'), 403
    conn_u = get_users_connection()
    users  = conn_u.execute("SELECT * FROM users").fetchall()
    conn_u.close()
    conn_d    = get_data_connection()
    companies = conn_d.execute("SELECT * FROM companies").fetchall()
    conn_d.close()
    return render_template('admin/admin_users.html', users=users, companies=companies)

@app.route('/admin/users/add', methods=['POST'])
def add_user():
    if session.get('role') != 'admin':
        return render_template('errors/403.html'), 403
    username = request.form.get('username', '').strip()
    password = request.form.get('password', '')
    role = request.form.get('role')
    if role not in ALLOWED_ROLES:
        flash("Invalid role specified.", "danger")
        return redirect('/admin/users')
    company_id = None
    if role == 'owner':
        try:
            company_id = int(request.form.get('company_id', ''))
        except (ValueError, TypeError):
            flash("Invalid company ID.", "danger")
            return redirect('/admin/users')
    conn = get_users_connection()
    conn.execute(
        "INSERT INTO users (username, password, role, company_id) VALUES (?, ?, ?, ?)",
        (username, hash_password(password), role, company_id),
    )
    conn.commit()
    conn.close()
    flash("User created successfully.", "success")
    return redirect('/admin/users')

@app.route('/admin/users/edit', methods=['POST'])
def edit_user():
    if session.get('role') != 'admin':
        return render_template('errors/403.html'), 403
    username = request.form.get('username', '').strip()
    new_role = request.form.get('role')
    if new_role not in ALLOWED_ROLES:
        flash("Invalid role specified.", "danger")
        return redirect('/admin/users')
    company_id = None
    if new_role == 'owner':
        try:
            company_id = int(request.form.get('company_id', ''))
        except (ValueError, TypeError):
            flash("Invalid company ID.", "danger")
            return redirect('/admin/users')
    conn = get_users_connection()
    if company_id:
        conn.execute("UPDATE users SET role = ?, company_id = ? WHERE username = ?", (new_role, company_id, username))
    else:
        conn.execute("UPDATE users SET role = ?, company_id = NULL WHERE username = ?", (new_role, username))
    conn.commit()
    conn.close()
    flash("User updated.", "success")
    return redirect('/admin/users')

@app.route('/admin/users/delete', methods=['POST'])
def delete_user():
    if session.get('role') != 'admin':
        return render_template('errors/403.html'), 403
    username = request.form.get('username', '').strip()
    conn = get_users_connection()
    conn.execute("DELETE FROM users WHERE username = ?", (username,))
    conn.commit()
    conn.close()
    flash("User deleted.", "warning")
    return redirect('/admin/users')
