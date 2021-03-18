from rest_framework.test import APIClient, APITestCase, APIRequestFactory
from game.models import Challenge, Profile, CompletedChallenge, CHALLENGE_TYPE_CHOICES
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class ClientTestCase(APITestCase):

    factory = APIRequestFactory()
    token = None
    challenge = None
    profile = None

    def setUp(self):
        self.challenge = Challenge.objects.create(type=CHALLENGE_TYPE_CHOICES[0][1], description='Test Challenge', points=50)
        testino = User.objects.create_user(username='testino@tests.com', first_name='Testino', last_name='Silva',password='testinospassword')
        self.profile = Profile.objects.create(user=testino)
        self.challenge = CompletedChallenge.objects.create(challenge=self.challenge, profile=self.profile)
        response = self.client.post('/api-token-auth/', {'username':'testino@tests.com', 'password':'testinospassword'})
        self.token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)


class NextChallengeViewTest(ClientTestCase):
    def test_get_next_challenge(self):
        response = self.client.get('/nextchallenge/')
        assert response.status_code == 200

class CompleteChallengeViewTest(ClientTestCase):
    def test_complete_challenge_success(self):
        response = self.client.post('/completechallenge/', {'challenge': self.challenge.id})
        assert response.status_code == 200
        self.assertIn('profile', response.data.keys())
        self.assertIn('challenge', response.data.keys())
        self.assertIn('completed_at', response.data.keys())
        self.assertIn('id', response.data.keys())
