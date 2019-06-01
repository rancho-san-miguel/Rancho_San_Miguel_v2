import django_filters
from .models import Ganado

class Ganado_filter(django_filters.FilterSet):

    f_start = django_filters.DateFilter()
    # f_end =

    class Meta:
        model = Ganado
        fields = {
            'f_nacimiento',
            'f_start'
        }
