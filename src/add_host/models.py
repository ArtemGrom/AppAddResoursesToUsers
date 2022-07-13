from django.db import models
from django.contrib.auth.models import User


class Host(models.Model):
    RESOURCES_CHOISES = [
        ('windows', 'Windows'),
        ('unix', 'Unix'),
        ('sql', 'SQL'),
    ]
    ip_address = models.GenericIPAddressField(verbose_name='IP-адрес')
    port = models.IntegerField(verbose_name='Порт', default=80)
    resources_list = models.CharField(
        verbose_name='Список ресурсов-хостов',
        max_length=10,
        choices=RESOURCES_CHOISES,
        default='unix')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Resources: {self.resources_list}'

    def get_absolute_url(self):
        return '/add_host/list_host/'

    class Meta:
        verbose_name = 'Хост'
        verbose_name_plural = 'Хосты'
