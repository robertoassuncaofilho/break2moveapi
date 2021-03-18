from django.test import TestCase
from game.models import Challenge, Profile, CompletedChallenge, CHALLENGE_TYPE_CHOICES
from django.contrib.auth.models import User

CHALLENGE_DESCRIPTION_1 = 'Test Challenge'

class GameTestCase(TestCase):
    def setUp(self):
        challenge = Challenge.objects.create(type=CHALLENGE_TYPE_CHOICES[0][1], description=CHALLENGE_DESCRIPTION_1, points=50)
        testino = User.objects.create_user(username='testino', first_name='Testino', last_name='Silva',password='testinospassword')
        profile = Profile.objects.create(user=testino)
        CompletedChallenge.objects.create(challenge=challenge, profile=profile)

class ChallengeTest(GameTestCase):

    def test_challenge_str(self):
        test_challenge = Challenge.objects.get(description=CHALLENGE_DESCRIPTION_1)
        self.assertEqual(test_challenge.__str__(), CHALLENGE_DESCRIPTION_1)

class ProfileTest(GameTestCase):

    def test_profile_str(self):
        test_profile = Profile.objects.get(user__username='testino')
        self.assertEqual(test_profile.__str__(), test_profile.user.get_full_name())

class CompletedChallengeTest(GameTestCase):
    
    def test_completed_challenge_str(self):
        completed_challenge = CompletedChallenge.objects.get(challenge__description=CHALLENGE_DESCRIPTION_1, profile__user__username='testino')
        self.assertEqual(completed_challenge.__str__(), "Challenge completed by %s at %s" % ('Testino', completed_challenge.completed_at.strftime('%d/%m/%Y')))
        

    