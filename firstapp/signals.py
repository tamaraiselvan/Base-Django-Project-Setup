from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from social_django.models import UserSocialAuth

### This signal used to create the Profile once the users gets added into the User table
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

### This signal used to create the Social Profile once the users gets added into the User table
@receiver(post_save, sender=User)
def create_google_auth(sender, instance, created, **kwargs):
    if created:
        UserSocialAuth.objects.create(user=instance, provider='	google-oauth2', uid=instance.email)

### The profile created will be saved to the database.
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

### The Social profile created will be saved to the database.
@receiver(post_save, sender=create_google_auth)
def save_google_auth(sender, instance, **kwargs):
    instance.UserSocialAuth.save()