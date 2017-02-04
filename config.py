class Config(object):
	"""
	Default configurations
	"""

	TESTING = False

class DevelopmentConfig(Config):
	"""
	Development Configurations
	"""
	DEBUG = True
	SQLALCHEMY_ECHO = True
	SQLALCHEMY_MODIFICATIONS = True

class ProductionConfig(Config):
	
	DEBUG = False
	SQLALCHEMY_TRACK_MODIFICATIONS = True

app_config = {
	'development': DevelopmentConfig,
	'production': ProductionConfig
}