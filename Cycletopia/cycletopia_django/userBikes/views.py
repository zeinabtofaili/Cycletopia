from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes, renderer_classes
from django.core.mail import send_mail
from .serializers import UsedBikeSerializer
from .models import UsedBike
from django.http import Http404
from django.utils.text import slugify
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer


# Create your views here.

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def sellBike(request):
    data = request.data.copy()  # create a mutable copy of the request data
    data['user'] = request.user.id
    data['slug'] = slugify(data['name'])

    serializer = UsedBikeSerializer(data=data)
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

class UserSpecificBike(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        bikes = UsedBike.objects.filter(user=request.user)
        serializer = UsedBikeSerializer(bikes, many=True)
        return Response(serializer.data)


class AllBikes(APIView):
    def get(self, request, format=None):
        bikes = UsedBike.objects.all()
        serializer = UsedBikeSerializer(bikes, many=True)
        return Response(serializer.data)

class BikeDetail(APIView):
    def get_object(self, product_slug):
        try:
            return UsedBike.objects.get(slug=product_slug)
        except UsedBike.DoesNotExist:
            raise Http404
    
    def get(self, request, product_slug, format=None):
        product = self.get_object(product_slug)
        serializer = UsedBikeSerializer(product)
        return Response(serializer.data)

@api_view(['DELETE'])   
@renderer_classes([JSONRenderer])
@csrf_exempt
def delete_bike(request, bike_id):

    try:
        bike = UsedBike.objects.get(id=bike_id)
    except UsedBike.DoesNotExist:
        return Response({'error': 'Bike does not exist'}, status=404)
    try:
        bike.delete()
        return Response({'message': 'Bike deleted successfully'}, status=204)
    except Exception as e:
        print(e)
        return Response({'error': 'Invalid request method'}, status=405)
