from flask import request, redirect, render_template, session, flash
from server import app
from db import get_data_connection

@app.route('/admin/companies')
def admin_list_companies():
    if session.get('role') != 'admin':
        return render_template('errors/403.html'), 403
    conn = get_data_connection()
    companies = conn.execute("SELECT * FROM companies").fetchall()
    conn.close()
    return render_template('admin/admin_companies.html', companies=companies)

@app.route('/admin/companies/add', methods=['GET', 'POST'])
def admin_add_company():
    if session.get('role') != 'admin':
        return render_template('errors/403.html'), 403
    if request.method == 'POST':
        company_name = request.form.get('company_name', '').strip()
        owner        = request.form.get('owner', '').strip()
        conn = get_data_connection()
        conn.execute("INSERT INTO companies (name, owner) VALUES (?, ?)", (company_name, owner))
        conn.commit()
        conn.close()
        flash("Company created successfully.", "success")
        return redirect('/admin/companies')
    return render_template('admin/admin_companies.html')

@app.route('/admin/companies/delete', methods=['POST'])
def delete_company():
    if session.get('role') != 'admin':
        return render_template('errors/403.html'), 403
    try:
        company_id = int(request.form.get('company', ''))
    except (ValueError, TypeError):
        flash("Invalid company ID.", "danger")
        return redirect('/admin/companies')
    conn = get_data_connection()
    conn.execute("DELETE FROM companies WHERE id = ?", (company_id,))
    conn.execute("DELETE FROM comments WHERE company_id = ?", (company_id,))
    conn.commit()
    conn.close()
    flash("Company deleted.", "warning")
    return redirect('/admin/companies')
