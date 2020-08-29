from django.db import models


class CommonInfo(models.Model):
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        abstract = True

# table housing the organizations (multiple tenants)
class Tenant(CommonInfo):
    name = models.CharField(max_length=255, unique=True)
    business_phone_number = models.CharField(max_length=250)
    business_email = models.EmailField()
    is_active = models.BooleanField(default=True)
    schema = models.CharField(max_length=255, blank=True)
    subdomain = models.CharField(max_length=255, blank=True)
    tenant_id = models.SlugField(blank=True)

    def __str__(self):
        return self.name

# organizational departments db table
class Department(CommonInfo):
    name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name
