from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes, renderer_classes
from django.core.mail import send_mail
from .serializers import DonatedBikeSerializer
from .models import DonatedBike
from django.http import Http404
from django.utils.text import slugify
# Create your views here.

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def donateBike(request):
    data = request.data.copy()  # create a mutable copy of the request data
    data['user'] = request.user.id
    data['slug'] = slugify(data['name'])

    serializer = DonatedBikeSerializer(data=data)
    if serializer.is_valid():
        try:
            serializer.save()
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        print("Error here ",serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserSpecificDonatedBike(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        bikes = DonatedBike.objects.filter(user=request.user)
        serializer = DonatedBikeSerializer(bikes, many=True)
        return Response(serializer.data)

class AllDonatedBikes(APIView):
    def get(self, request, format=None):
        bikes = DonatedBike.objects.all()
        serializer = DonatedBikeSerializer(bikes, many=True)
        return Response(serializer.data)