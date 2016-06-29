from django.contrib import admin
from .models import Profile, UserStripe
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name',)

    class Meta:
        model = Profile

admin.site.register(Profile, ProfileAdmin)

class UserStripeAdmin(admin.ModelAdmin):
    list_display = ('user','stripe_id')

    class Meta:
        model = UserStripe

admin.site.register(UserStripe, UserStripeAdmin)