from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Challenge, CompletedChallenge, Profile
from .serializers import ChallengeSerializer, CompletedChallengeSerializer
from django.db.models.aggregates import Count
from random import randint
from datetime import datetime

class NextChallengeView(APIView):

    def get(self, request, format=None):
        count = Challenge.objects.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        challenge = Challenge.objects.all()[random_index]
        return Response(ChallengeSerializer(challenge).data)

class CompleteChallengeView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        profile = Profile.objects.get(user=request.user)
        challenge = Challenge.objects.get(id=int(request.data['challenge']))
        completed_challenge = CompletedChallenge(profile=profile, completed_at=datetime.now(), challenge=challenge)
        completed_challenge.save()
        return Response(CompletedChallengeSerializer(completed_challenge).data)


