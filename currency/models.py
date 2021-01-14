from django.db import models

class Currency(models.Model):
    name            = models.CharField(max_length=30, blank=True)  # name of that currency
    code            = models.CharField(max_length=10, unique=True)              # eg - USD, INR, BTC etc...

    value           = models.DecimalField(max_digits=25 ,decimal_places=9, default=1.0) #wrt 1 Rupee
    last_updated    = models.DateTimeField(auto_now=True)
    update_status   = models.BooleanField(default=False)

    def __str__(self):
        return self.name