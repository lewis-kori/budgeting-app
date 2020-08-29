from django.conf import settings
from django.db import migrations


def rename_site_name(apps, schema_editor):
    Site = apps.get_model('sites', 'Site')

    new_site = Site.objects.filter(id=1)
    
    if not new_site.exists():
        Site.objects.create(domain=settings.FRONTEND_HOST, name=settings.SITE_NAME)
        Site.objects.create(domain=settings.SITE_DOMAIN, name=settings.SITE_NAME)

class Migration(migrations.Migration):
    dependencies = [
        ('tenants', '0001_initial'),
        ('tenants', '0002_auto_20200816_0605'),
        ('tenants', '0003_tenant_tenant_id'),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.RunPython(rename_site_name)
    ]
