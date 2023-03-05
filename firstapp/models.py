from django.db import models
from django.contrib.auth.models import User
# Create your models here.
themes = (
    ("dark", "dark"),
    ("light", "light"),
)
class Theme(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    color = models.CharField(choices=themes, default="light", max_length=15)

    def __str__(self):
        return self.user.username