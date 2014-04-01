from datetime import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin

# Create your models here.

class Quote(CMSPlugin):
    """
    A quote or testimonial
    """
    created_at = models.DateTimeField(_('Created at'), default=datetime.now)
    content = models.CharField(_('Quote'), max_length=255, default='')
    footer = models.CharField(_('Footer'), max_length=255, blank=True)
    url = models.URLField(_('Link'), blank=True)

    def __unicode__(self):
        return self.content[:50]
