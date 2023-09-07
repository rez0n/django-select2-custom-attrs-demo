from django.db import models
from django.utils.translation import gettext_lazy as _


class Location(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    timezone = models.CharField(_("Timezone"), null=True, max_length=50)
    some_bool = models.BooleanField(_("Some Bool"), default=False)


class Booking(models.Model):
    location = models.ForeignKey("demo.Location", verbose_name=_("Location"),
                                 related_name='bookings',
                                 on_delete=models.CASCADE)
