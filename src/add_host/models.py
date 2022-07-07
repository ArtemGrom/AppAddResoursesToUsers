from django.db import models
from django.contrib.auth.models import User


class Host(models.Model):
    RESOURCES_CHOISES = [
        ('windows', 'Windows'),
        ('unix', 'Unix'),
        ('sql', 'SQL'),
    ]
    ip_address = models.GenericIPAddressField()
    port = models.CharField(max_length=10)
    resources_list = models.CharField(max_length=10, choices=RESOURCES_CHOISES, default='unix')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
