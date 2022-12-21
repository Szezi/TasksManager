import django_filters
from django_filters import CharFilter, DateFilter, ChoiceFilter, MultipleChoiceFilter, ModelChoiceFilter

from .models import *


class TaskFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    description = CharFilter(field_name='description', lookup_expr='icontains')
    notes = CharFilter(field_name='notes', lookup_expr='icontains')

    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['board', 'created', 'state', 'deadline']