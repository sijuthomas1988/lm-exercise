import os

PROJECT_NAME = "Backend Task"
VERSION = "0.0.1"
SQLALCHEMY_DATABASE_URL: str = os.getenv('DATABASE_URI', "postgresql://postgres:@localhost:5432/testdbb")
DEBUG=True
