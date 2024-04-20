from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes, renderer_classes
from .serializers import AppointmentSerializer
from rest_framework.response import Response
from .models import TrainingAppointment
from django.http import Http404
from django.http import JsonResponse


# Create your views here.

'''
First API: add an appointment, post method

Second API: get available times in a specific date
take date, get all times there, remove from the list the taken times, return list to front end
if date does not exist, then return list as is
'''

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def makeAppointment(request):
    data = request.data.copy()  # create a mutable copy of the request data
    data['user'] = request.user.id
    serializer = AppointmentSerializer(data=data)
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

class GetTimesInADate(APIView):
    def get(self, request, date, format=None): 
        allAppointmentTimes = ['08:00 AM', '10:00 AM', '12:00 PM', '02:00 PM', '04:00 PM']
        appointments = TrainingAppointment.objects.filter(date=date)
        if appointments.exists():
            for appointment in appointments:
                if appointment.time in allAppointmentTimes:
                    allAppointmentTimes.remove(appointment.time)
        return JsonResponse({'available_times': allAppointmentTimes})



