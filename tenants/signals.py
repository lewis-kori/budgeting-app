import time

from django.contrib.sites.models import Site
from django.core.management import call_command
from django.db import connection
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.timezone import datetime

from .models import Tenant


def populate_client_schema(client):

    with connection.cursor() as cursor:
        cursor.execute(f'SET search_path TO {client.schema}')
        cursor.execute(f"INSERT INTO tenants_tenant (name,business_email,business_phone_number,subdomain,schema,is_active,created,updated) " \
        f"VALUES ('{client.name}','{client.business_email}','{client.business_phone_number}','{client.subdomain}','{client.schema}',true,'{datetime.now()}','{datetime.now()}');")


@receiver(pre_save, sender=Tenant)
def name_schema_and_subdomain(sender, instance, *args, **kwargs):
    site = Site.objects.get_current()
    site_domain = site.domain
    if not instance.schema and not instance.subdomain:
        joined_name = instance.name.replace(" ", "").lower()
        instance.schema = joined_name
        instance.subdomain = f'{joined_name}.{site_domain}'


@receiver(post_save, sender=Tenant)
def create_client_schema(sender, instance, created, **kwargs):
    if created:
        call_command('migrate_schema', instance.schema)
        time.sleep(1)
        populate_client_schema(instance)
