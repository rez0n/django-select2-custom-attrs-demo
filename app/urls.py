from django.urls import path, include

from demo.views import IndexView, LocationSelect2View

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('location_widget/', LocationSelect2View.as_view(), name='location_widget'),
    path("select2/", include("django_select2.urls")),
]
