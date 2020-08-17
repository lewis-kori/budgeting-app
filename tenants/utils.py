from django.contrib.sites.models import Site
from django.db import connection

from .models import Tenant


# get the host name from request
def host_name_from_request(request):
    # split on `:` to remove port
    return request.get_host().split(':')[0].lower()

def get_tenants_map():
    tenant_dict = dict(Tenant.objects.values_list("subdomain","schema"))
    return tenant_dict

# find the tenant schema from request
def tenant_schema_from_request(request):
    hostname = host_name_from_request(request)
    site = Site.objects.get_current()

    # use the postgres public schema if no subdomain specified on request
    if hostname == site.domain:
        return 'public'
    else:
        tenants_map = get_tenants_map()
        return tenants_map.get(hostname)


# set the schema to be used for all request for a particlular subdomain
def set_tenant_schema_from_request(request):
    schema = tenant_schema_from_request(request)
    with connection.cursor() as cursor:
        cursor.execute(f'SET search_path to {schema}')
