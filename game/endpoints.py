from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin
from .models import Challenge
from .serializers import ChallengeSerializer
from django.db.models.aggregates import Count
from random import randint

class NextChallengeView(APIView):

    def get(self, request, format=None):
        count = Challenge.objects.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        challenge = Challenge.objects.all()[random_index]
        return Response(ChallengeSerializer(challenge).data)

