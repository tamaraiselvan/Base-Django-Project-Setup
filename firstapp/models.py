from django.db import models
from django.contrib.auth.models import User
# Create your models here.

## These are the options for the colors in Theme model.
themes = (
    ("dark", "dark"),
    ("light", "light"),
)
class Theme(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    color = models.CharField(choices=themes, default="light", max_length=15)

    def __str__(self):
        return self.user.username
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to="profile_img", default="profile_pic.png")
    # add extra which all you want
    def __str__(self):
        return self.user.username