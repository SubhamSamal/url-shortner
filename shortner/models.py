from django.db import models
from .utils import assignCode

class urlShortner(models.Model):
    url = models.CharField(max_length=200)
    output = models.CharField(max_length=10, blank=True, unique=True)
    time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.output=='' or self.output is None:
            self.output = assignCode(self)
        super(urlShortner, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)