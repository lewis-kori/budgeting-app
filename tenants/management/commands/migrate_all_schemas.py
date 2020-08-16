from django.core.management import call_command
from django.core.management.commands.migrate import Command as MigrationCommand
from django.db import connection
from django.db.utils import ProgrammingError



class Command(MigrationCommand):
        
    def handle(self, *args, **kwargs):
        try:
            from tenants.models import Tenant
            tenants = Tenant.objects.all()

            if tenants.exists():
                for tenant in tenants:
                    call_command('migrate_schema', tenant.schema)

        except ProgrammingError as e:
            print(f'You are running migrations for the first time and so the error: {e} was raised')
