# filters.py
import django_filters
from .models import Student

class StudentFilter(django_filters.FilterSet):
    min_ctc = django_filters.NumberFilter(field_name="Cost_To_Company", lookup_expr='gte')
    max_ctc = django_filters.NumberFilter(field_name="Cost_To_Company", lookup_expr='lte')

    class Meta:
        model = Student
        fields = ['min_ctc', 'max_ctc']
