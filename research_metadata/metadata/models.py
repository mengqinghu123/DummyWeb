from django.db import models

# Create your models here.
from django.db import models

class ResearchMetadata(models.Model):
    data_provider = models.CharField(max_length=100)
    data_format = models.CharField(max_length=100)
    degree_of_aggregation = models.CharField(max_length=100)

    def __str__(self):
        return self.data_provider

