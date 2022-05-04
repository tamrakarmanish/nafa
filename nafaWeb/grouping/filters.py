import django_filters
from django_filters import CharFilter

from .models import *
from  accounts.models import *

class GroupFilter(django_filters.FilterSet):
    note = CharFilter(field_name='name',lookup_expr='icontains')
    class Meta:
        model = Group
        fields= ['name']

class UserFilter(django_filters.FilterSet):
    note = CharFilter(field_name='username',lookup_expr='icontains')

    class Meta:
        model = Profile
        fields= ['email','first_name','last_name']
