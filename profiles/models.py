from django.db import models
from django.conf import settings
from allauth.account.signals import user_logged_in, user_signed_up
# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=1024)
    description = models.TextField(null=True, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)

    def __str__(self):
        return self.name


class UserStripe(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    stripe_id = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        if self.stripe_id:
            return str(self.stripe_id)
        else:
            return self.user.username

def my_callback(sender, request, user, **kwargs):
    is_stripe, created = UserStripe.objects.get_or_create(user=user)

    if created:
        print("created for {}".format(user.username))

    user_profile, is_created = Profile.objects.get_or_create(user=user)
    if is_created:
        user_profile.name = user.get_full_name()
        user_profile.save()

user_logged_in.connect(my_callback)