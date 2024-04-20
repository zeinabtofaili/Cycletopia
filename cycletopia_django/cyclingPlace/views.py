from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PlaceSerializer
from .models import Place
from django.http import Http404
# Create your views here.
class CyclingPlacesList(APIView):
    def get(self, request, format=None):
        places = Place.objects.all()
        serializer = PlaceSerializer(places, many=True)
        return Response(serializer.data)

class PlaceDetail(APIView):
    def get_object(self, place_slug):
        try:
            return Place.objects.filter(slug=place_slug)[0]
        except Place.DoesNotExist:
            raise Http404
    
    def get(self, request, place_slug, format=None):
        place = self.get_object(place_slug)
        serializer = PlaceSerializer(place)
        return Response(serializer.data)