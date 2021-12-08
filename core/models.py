import uuid
from django.db import models


class CompanyRelatedModel(models.Model):
    """Abstract class used by models that belong to a Company"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey('accounts.Company', related_name='%(class)s', on_delete=models.CASCADE, editable=False)

    class Meta:
        abstract = True
