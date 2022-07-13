from django.forms import ModelForm, HiddenInput
from .models import Host


class HostForm(ModelForm):
    class Meta:
        model = Host
        fields = ['ip_address', 'port', 'resources_list']

