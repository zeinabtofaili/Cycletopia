from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import EventSerializer
from .models import Event
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
# Create your views here.
class CyclingEventsList(APIView):
    def get(self, request, format=None):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

class EventDetail(APIView):
    def get_object(self, event_slug):
        try:
            return Event.objects.filter(slug=event_slug)[0]
        except Event.DoesNotExist:
            raise Http404
    
    def get(self, request, event_slug, format=None):
        event = self.get_object(event_slug)
        serializer = EventSerializer(event)
        return Response(serializer.data)

@api_view(['PATCH'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def registerInEvent(request):
    name = request.data['name']
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        try:
            event = Event.objects.get(name=name)
            if request.user in event.attendees.all():
                return Response("User Already Registered!", status=status.HTTP_400_BAD_REQUEST) 
            event.attendees.add(request.user)
            event.save()
            return Response(EventSerializer(event).data, status=status.HTTP_200_OK)
        except Event.DoesNotExist:
            return Response({'error': 'Event not found'}, status=404)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)