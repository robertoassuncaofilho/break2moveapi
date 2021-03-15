from django.contrib import admin
from .models import Challenge, Profile, CompletedChallenge
# Register your models here.
@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(CompletedChallenge)
class CompletedChallengeAdmin(admin.ModelAdmin):
    pass