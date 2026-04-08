from django.db import models
from common.models import BaseModel

class Tenant(BaseModel):
    name = models.CharField(max_length=255)
    subdomain = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
