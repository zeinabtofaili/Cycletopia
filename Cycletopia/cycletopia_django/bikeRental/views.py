import stripe

from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.core.mail import send_mail
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RentalProductSerializer
from .models import RentalProduct
from django.http import Http404
from datetime import date

# Create your views here.
class RentalBikesList(APIView):

    def get(self, request, format=None):
        bikes = RentalProduct.objects.all()

        today = date.today()
        for bike in bikes:
            if bike.return_date and bike.return_date < today and bike.is_rented:
                bike.is_rented = False
                bike.return_date = None
                bike.rented_date = None
                bike.stripe_token =""
                bike.renter_email=""
                bike.renter_id=""
                bike.user = None
                bike.save()
        bikes = RentalProduct.objects.all()
        serializer = RentalProductSerializer(bikes, many=True)

        return Response(serializer.data)

class BikeDetail(APIView):
    def get_object(self, bike_slug):
        try:
            return RentalProduct.objects.filter(slug=bike_slug)[0]
        except RentalProduct.DoesNotExist:
            raise Http404
    
    def get(self, request, bike_slug, format=None):
        bike = self.get_object(bike_slug)
        serializer = RentalProductSerializer(bike)
        return Response(serializer.data)

@api_view(['PATCH'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def rentBike(request):
    name = request.data['name']
    serializer = RentalProductSerializer(data=request.data)
    amount_paid = request.data['amount_paid']
    
    if serializer.is_valid():
        stripe.api_key = settings.STRIPE_SECRET_KEY
        paid_amount = request.data['amount_paid']

        try:
            product = RentalProduct.objects.get(name=name)
            if(product.return_date):
                if(product.return_date > date.today()):
                    return Response("Bike already rented!", status=status.HTTP_400_BAD_REQUEST) 
            product.user = request.user
            product.rented_date=request.data['rented_date']
            product.return_date=request.data['return_date']
            product.renter_email = request.data['renter_email']
            product.renter_id=request.data['renter_id']
            product.name=request.data['name']
            product.stripe_token=request.data['stripe_token']
            product.rent_duration_and_price= request.data['rent_duration_and_price']
            product.is_rented = True
            product.save()
        except RentalProduct.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)
        try:
            charge = stripe.Charge.create(
                amount=int(paid_amount * 100),
                currency='USD',
                description='Charge from Cycletopia',
                source=serializer.validated_data['stripe_token']
            )
            try: 
                send_mail(
                    'Payment Succeeded!',
                    'Thank you for renting a bike at Cycletopia. You paid a total of ' + str(amount_paid) +'$. Please do not reply to this email.',
                    settings.EMAIL_HOST_USER,
                    [request.data['renter_email']],
                    fail_silently=False,
                    auth_user=None,
                    auth_password=None, 
                    connection=None, 
                    html_message=None
                )
            except Exception as e:
                print(e)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    print(serializer.errors)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)