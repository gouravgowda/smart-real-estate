# Monkeypatch Django to support older MySQL 5.5 databases
from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.backends.mysql.base import DatabaseWrapper

# Bypass MySQL version checking (which requires MySQL >= 8.0)
BaseDatabaseWrapper.check_database_version_supported = lambda self: None

# Avoid datetime(6) and time(6) syntax errors on MySQL 5.5
DatabaseWrapper.data_types['DateTimeField'] = 'datetime'
DatabaseWrapper.data_types['TimeField'] = 'time'
