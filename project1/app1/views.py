from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializers import RegisterUserSerializer,ObadaSerailizer,ApplicationFormSerailizer
from rest_framework.response import Response
from rest_framework import status
from .models import Obada
from django.core.mail import send_mail
from django.conf import settings
import hmac
import hashlib
import subprocess
from django.http import HttpResponseBadRequest, HttpResponse
# Create your views here.


class UserRegistration(generics.CreateAPIView):
    serializer_class=RegisterUserSerializer


@api_view(['POST','GET'])
def f(request):
    if request.method=='POST':
        x=ObadaSerailizer(data=request.data)
        x.is_valid(raise_exception=True)
        x.save()
        return Response(x.data,status.HTTP_201_CREATED,headers={
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true',
    })
    items=Obada.objects.all()
    serialized_item=ObadaSerailizer(items,many=True)
    return Response(serialized_item.data,headers={
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true',
    })

class RegistrationEntity(generics.CreateAPIView):
    serializer_class=ApplicationFormSerailizer



@api_view(['POST'])
def index(request):
    message="Hii how are you"
    send_mail(
        'Contract Form',
        message,
        'settings.EMAIL_HOST_USER',
        ['ali.dib.99.r@gmail.com'],
        fail_silently=False
    )
    return Response('OK')

api_view()
def husseinHosting(request):
    return Response('hhhhhhhhhh')


def github_webhook(request):
    # Verify the signature of the webhook
    secret = b"your-webhook-secret"
    signature = request.headers.get("X-Hub-Signature").replace("sha1=", "").encode()
    body = request.body
    mac = hmac.new(secret, msg=body, digestmod=hashlib.sha1)
    if not hmac.compare_digest(mac.hexdigest(), signature):
        return HttpResponseBadRequest("Invalid signature")

    # Execute the deployment script
    subprocess.run(["/home/alideeb99r/script.sh"])

    # Return a success response
    return HttpResponse("OK")