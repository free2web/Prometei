#!/usr/bin/env python
#-*- coding: UTF-8 -*-
"""Config file"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or '\xa1>\x9e\x08!\x9e|~y$Z\xb6\x9e\x10C\xdd\x93\xde\x08f\xe8\xf8\xac\xa6'
	SQL_ALCHEMY_COMMIT_ON_TEARDOWN = True
	PROMETEI_MAIL_SUBJECT_PREFIX = '[Prometei]'
	PROMETEI_MAIL_SENDER = 'Prometei <no-reply@example.com>'
	PROMETEI_POSTS_PER_PAGE = 10
	RECAPTCHA_PUBLIC_KEY = 'key'
	RECAPTCHA_PRIVATE_KEY = 'key'

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
		DEBUG = True
		MAIL_SERVER = 'smtp.example.com'
		MAIL_PORT = '465'
		MAIL_USE_SSL = True
		MAIL_USE_TLS = False
		MAIL_USERNAME = 'no-reply@example.com'
		MAIL_PASSWORD = '123'
		PROMETEI_ADMIN = os.environ.get('PROMETEI_ADMIN')
		PROMETEI_POSTS_PER_PAGE = 10
		PROMETEI_COMMENTS_PER_PAGE = 10
		SQLALCHEMY_DATABASE_URI = 'postgresql://ИмяПользователя:Пароль@localhost/ИмяБазы'
class TestingConfig(Config):
		TESTING = True
		SQLALCHEMY_DATABASE_URI = 'postgresql://ИмяПользователя:Пароль@localhost/ИмяБазы'
class ProductionConfig(Config):
		DEBUG=False
		MAIL_SERVER = 'smtp.example.com'
		MAIL_PORT = '465'
		MAIL_USE_SSL = True
		MAIL_USE_TLS = False
		PROMETEI_ADMIN = os.environ.get('PROMETEI_ADMIN')
		MAIL_USERNAME = 'no-reply@example.com'
		MAIL_PASSWORD = '123'
		PROMETEI_COMMENTS_PER_PAGE = 5
		PROMETEI_POSTS_PER_PAGE = 10
		SQLALCHEMY_DATABASE_URI = 'postgresql://ИмяПользователя:Пароль@localhost/ИмяБазы'
config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig,
	'default': DevelopmentConfig
	}