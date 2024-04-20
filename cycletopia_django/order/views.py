import stripe

from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from .models import Order, OrderItem
from .serializers import OrderSerializer, MyOrderSerializer


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer = OrderSerializer(data=request.data)
    amount_paid = 0
    for item in request.data['items']:
        amount_paid+= item['price']
    
    if serializer.is_valid():
        stripe.api_key = settings.STRIPE_SECRET_KEY
        paid_amount = sum(item.get(
            'quantity') * item.get('product').price for item in serializer.validated_data['items'])
        try:
            charge = stripe.Charge.create(
                amount=int(paid_amount * 100),
                currency='USD',
                description='Charge from Cycletopia',
                source=serializer.validated_data['stripe_token']
            )
            serializer.save(user=request.user, paid_amount=paid_amount)
            try: 
                send_mail(
                    'Payment Succeeded!',
                    'Thank you for shopping at Cycletopia. You paid a total of ' + str(amount_paid) +'$. Please do not reply to this email.',
                    settings.EMAIL_HOST_USER,
                    [request.data['email']],
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
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrdersList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = MyOrderSerializer(orders, many=True)
        return Response(serializer.data)
