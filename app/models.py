from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


class Employee(UserMixin, db.Model):
	"""
	Creates an Employee table
 	"""

 	# Ensures table will be named in plural and not in singular
	# as is the name of the model
 	__tablename__ = 'employees'

	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(60), index=True, unique=True)
	username = db.Column(db.String(60), index=True, unique=True)
	first_name = db.Column(db.String(60), index=True)
	last_name = db.Column(db.String(60), index=True)
	password_hash = db.Column(db.String(128))
	is_admin = db.Column(db.Boolean, default=False)

	@property
	def password(self):
		"""
		Prevents pasword from being accessed
		"""
		raise AttributeError('password is not a readable attribute.')

	@password.setter
	def password(self, password):
		"""
		Sets password to a hashed password
		"""
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		"""
		Checks if hashed password matches actual password
		"""
		return check_password_hash(self.password_hash, password)

	def __repr__(self):
		full_name = self.first_name + ' ' + self.last_name
		return '<Employee: {}>'.format(full_name)

	@login_manager.user_loader
	def load_user(user_id):
		return Employee.query.get(int(user_id))

class Department(db.Model):
	"""
	Creates a Department table
	"""

	__tablename__ = 'departments'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(60), unique=True)
	description = db.Column(db.String(200))
	employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
	employee = db.relationship('Employee',
								backref=db.backref('employees', lazy='dynamic'))

	def __repr__(self):
		return '<Department: {}>'.format(self.name)

class Role(db.Model):
	"""
	Creates a Role table
	"""

	__tablename__ = 'roles'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(60), unique=True)
	description = db.Column(db.String(200))
	employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
	employee = db.relationship('Employee',
								backref=db.backref('employee_roles', lazy='dynamic'))
	dept_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
	department = db.relationship('Department',
								backref=db.backref('departments', lazy='dynamic'))

	def __repr__(self):
		return '<Role: {}>'.format(self.name)