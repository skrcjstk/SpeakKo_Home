from django.conf import settings

class DatabaseAppsRouter(object):
    """
    A router to control all database operations on models for different
    databases.

    In case an app is not set in settings.DATABASE_APPS_MAPPING, the router
    will fallback to the `default` database.

    Settings example:

    DATABASE_APPS_MAPPING = {'model_name1': 'db1', 'model_name2': 'db2'}

    """

    def db_for_read(self, model, **hints):
        """Point all read operations to the specific database."""
        return settings.DATABASE_APPS_MAPPING.get(model._meta.model_name, None)

    def db_for_write(self, model, **hints):
        """Point all write operations to the specific database."""
        return settings.DATABASE_APPS_MAPPING.get(model._meta.model_name, None)

    def allow_relation(self, obj1, obj2, **hints):
        """Have no opinion on whether the relation should be allowed."""
        return None