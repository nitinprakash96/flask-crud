from flask import abort, flash, redirect,render_template, url_for
from flask_login import current_user, login_user, logout_user, login_required
from . import auth
from forms import LoginForm, RegistrationForm
from .. import db
from ..models import Employee


@auth.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		employee = Employee(email=form.email.data,
							username=form.username.data,
							first_name=form.first_name.data,
							last_name=form.last_name.data,
							password=form.password.data)

		# add employee to the database
		db.session.add(employee)
		db.session.commit()
		flash('You have successfully registered! You may now login.')

		# redirect to the login page
		return redirect(url_for('auth.login'))

	# load registration template
	return render_template('auth/register.html', form=form, title='Register')

@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():

		employee = Employee.query.filter_by(email=form.email.data).first()
		if employee is not None and employee.verify_password(form.password.data):
			login_user(employee)

			if employee.is_admin:
				return redirect(url_for('home.admin_dashboard'))
			else:
				return redirect(url_for('home.dashboard'))

		else:
			flash('Invalid email or passsword')
	return render_template('auth/login.html', form=form, title='Login')


@auth.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You have successfully been logged out.')

	return redirect(url_for('auth.login'))

@home.route('/')
def homepage():
	return render_template('home/index.html', title="Welcome")


@home.route('/dashboard')
@login_required
def dashboard():
	return render_template('home/dashboard.html', title="Dashboard")

@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
	# prevent non-admins from acessing the page
	if not current_user.is_admin:
		abort(403)

	return render_template('home/admin_dashboard.html', title="Dashboard")