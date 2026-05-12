from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone

class MagicLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    usado = models.BooleanField(default=False)

    def is_valid(self):
        # Link válido por 15 minutos
        return not self.usado and (timezone.now() - self.criado_em).seconds < 900

    def __str__(self):
        return f"MagicLink para {self.user.username}"