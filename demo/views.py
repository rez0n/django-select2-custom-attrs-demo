from django.http import JsonResponse
from django.views.generic import UpdateView
from django_select2.views import AutoResponseView

from demo.forms import BookingForm
from demo.models import Booking


class IndexView(UpdateView):
    template_name = 'index.html'
    form_class = BookingForm
    model = Booking

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')

    def get_object(self, queryset=None):
        obj, created = Booking.objects.get_or_create(pk=1, defaults={'location_id': 1})
        return obj


class LocationSelect2View(AutoResponseView):

    widget = None
    term = ''
    object_list = []

    def get(self, request, *args, **kwargs):
        self.widget = self.get_widget_or_404()
        self.term = kwargs.get("term", request.GET.get("term", ""))
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        return JsonResponse(
            {
                "results": [
                    {"text": self.widget.label_from_instance(obj),
                     "id": obj.pk,
                     "is_tz_available": "Yes" if obj.timezone else "No",
                     }
                    for obj in context["object_list"]
                ],
                "more": context["page_obj"].has_next(),
            }
        )
