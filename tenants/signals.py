import time

from django.contrib.sites.models import Site
from django.core.management import call_command
from django.db import connection
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.utils.timezone import datetime

from .models import Tenant
from .utils import generate_random_num


def populate_client_schema(client):

    with connection.cursor() as cursor:
        cursor.execute(f'SET search_path TO {client.schema}')
        cursor.execute(f"INSERT INTO tenants_tenant (name,business_email,business_phone_number,subdomain,schema,tenant_id,is_active,created,updated) " \
        f"VALUES ('{client.name}','{client.business_email}','{client.business_phone_number}','{client.subdomain}','{client.schema}','{client.tenant_id}',true,'{datetime.now()}','{datetime.now()}');")


@receiver(pre_save, sender=Tenant)
def name_schema_and_subdomain(sender, instance, *args, **kwargs):
    site = Site.objects.get(id=2)
    site_domain = site.domain

    # populate the schema and subdomain info
    if not instance.schema and not instance.subdomain:
        joined_name = instance.name.replace(" ", "").lower()
        instance.schema = joined_name
        instance.subdomain = f'{joined_name}.{site_domain}'

    if not instance.tenant_id:
        joined_name = instance.name.replace(" ", "").lower()
        substring = joined_name[0:3]
        random_num = generate_random_num()
        instance.tenant_id = slugify(f'{substring} {random_num}').upper()


@receiver(post_save, sender=Tenant)
def create_client_schema(sender, instance, created, **kwargs):
    if created:
        call_command('migrate_schema', instance.schema)
        time.sleep(1)
        populate_client_schema(instance)
