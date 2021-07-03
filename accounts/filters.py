import django_filters
from django_filters.filters import ChoiceFilter
from django_filters import DateTimeFromToRangeFilter

from .models import Order

STATUS = (
    ('Pending', 'Pending'),
    ('Out for delivery', 'Out for delivery'),
    ('Delivered', 'Delivered'),
)

CATEGORY = (
    ('Indoor', 'Indoor'),
    ('Outdoor', 'Outdoor'),
)


class OrderFilter(django_filters.FilterSet):
    date_created = django_filters.DateTimeFromToRangeFilter(widget=django_filters.widgets.RangeWidget(
        attrs={'type': 'date'}
    )
    )
    status = ChoiceFilter(choices=STATUS)
    category = ChoiceFilter(choices=CATEGORY)

    class Meta:
        model = Order
        fields = [
            'customer',
            'product',
            'category',
            'status',
            'date_created'
        ]
