from django.db import models
from common.models import BaseModel

class Role(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name