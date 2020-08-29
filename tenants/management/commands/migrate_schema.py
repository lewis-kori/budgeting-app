from django.core.management.commands.migrate import Command as MigrationCommand

from django.db import connection

class Command(MigrationCommand):
    def add_arguments(self, parser):
        parser.add_argument('schema', type=str, help='Indicate name of schema you want to create')
        return super().add_arguments(parser)
        
    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            schema = kwargs['schema']
            cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {schema}")
            cursor.execute(f"SET search_path to {schema}")
            super(Command, self).handle(*args, **kwargs)