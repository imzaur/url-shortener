from django.conf import settings
from django.urls import reverse
from django.db import models

from .utils import create_shortcode
from .validators import validate_dot_com, validate_url

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

class KirrURLQueryset(models.QuerySet):
    def refresh_shortcodes(self):
        qs = self.filter(id__gte=1)
        new_codes = qs.count()
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.shortcode)
            q.save()
        return "New codes made {}".format(new_codes)


class KirrURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(KirrURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def get_queryset(self):
        return KirrURLQueryset(self.model, using=self._db)

    def refresh_shortcodes(self):
        return self.get_queryset().refresh_shortcodes()


class KirrURL(models.Model):
    url = models.CharField(
        max_length=220,
        validators=[validate_url, validate_dot_com]
    )
    shortcode = models.CharField(
        max_length=SHORTCODE_MAX,
        unique=True,
        blank=True,
        null=True,
    )
    updated = models.DateTimeField(
        auto_now=True,
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
    )
    active = models.BooleanField(
        default=True,
    )

    objects = KirrURLManager()

    def __str__(self):
        return self.url

    def save(self, *args, **kwargs):
        if not self.shortcode:
            self.shortcode = create_shortcode(self)

        if 'http' not in self.url:
            self.url = 'http://' + self.url

        super(KirrURL, self).save(*args, **kwargs)

    def get_short_url(self):
        url = reverse(
            'shortener:redir',
            kwargs={'shortcode':self.shortcode},
        )
        return url


