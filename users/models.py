from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from tenants.models import Department, Tenant

USER_ROLES = [('Admin', 'Admin'), ('Staff', 'Staff')]


# Define a custom user manager
class UserAccountManager(UserManager):

    # override create user method to accept email as username
    def create_user(self, email=None, password=None, **extra_fields):
        return super().create_user(email,
                                   email=email,
                                   password=password,
                                   **extra_fields)

    # override createsuperuser method to accept email as username
    def create_superuser(self, email=None, password=None, **extra_fields):
        return super().create_superuser(email,
                                        email=email,
                                        password=password,
                                        **extra_fields)


# define our custom user model
class UserAccount(AbstractUser):
    organization = models.ForeignKey(Tenant,
                                     related_name='users',
                                     on_delete=models.CASCADE,
                                     null=True,
                                     blank=True)
    department = models.ForeignKey(Department,
                                   related_name='users',
                                   on_delete=models.PROTECT,
                                   null=True,
                                   blank=True)
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='users/photos', null=True, blank=True)
    employee_id = models.CharField(max_length=255)
    role = models.CharField(max_length=40, choices=USER_ROLES, default='Staff')

    USERNAME_FIELD = 'email'


    REQUIRED_FIELDS = ['first_name', 'last_name',]

    objects = UserAccountManager()

    class Meta:
        ordering = ['-date_joined']
