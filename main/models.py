from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


class Course(TranslatableModel):
    translations = TranslatedFields (
        title = models.CharField(max_length = 90),
        description = models.TextField(),
        date = models.DateField(auto_now=True),
        price = models.DecimalField(max_digits=10, decimal_places=2)
    )

    def __str__(self):
        return self.title