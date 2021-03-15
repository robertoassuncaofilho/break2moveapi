from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

CHALLENGE_TYPE_CHOICES = [('body','body'), ('eye', 'eye')]

class Challenge (models.Model):
    type = models.CharField(max_length=10,choices=CHALLENGE_TYPE_CHOICES)
    description = models.CharField(max_length=255)
    points = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.description

class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.user.get_full_name()

class CompletedChallenge(models.Model):
    challenge = models.ForeignKey('Challenge', on_delete=models.PROTECT)
    completed_at = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)

    def __str__(self):
        return "Challenge completed by %s at %s" % (self.profile.user.first_name, self.completed_at.strftime('%d/%m/%Y'))
