from django import forms
from django_select2 import forms as s2forms

from demo.models import Booking


class LocationPickWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "name__icontains",
    ]

    def __init__(self, *args, **kwargs):
        kwargs['data_view'] = 'location_widget'
        super().__init__(*args, **kwargs)

    def label_from_instance(self, obj):
        return str(f'{obj.name}')


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = [
            'location',
        ]
        widgets = {
            "location": LocationPickWidget(attrs={
                'class': 'form-control',
                'data-minimum-input-length': 0,
            }),
        }
