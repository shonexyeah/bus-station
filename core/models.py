from django.db import models

class DateModelMixin(models.Model):
    # date info
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

