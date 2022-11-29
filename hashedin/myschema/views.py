from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Project,Issues,Assigned,Comments
from .serializer import ProjectSerializer,IssueSerializer,AssignedSerializer,CommentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import HttpResponse
from django.core.mail import send_mail


# Create your views here.

def index(request):

    return render(request, 'index.html')


class ProjectViewSet(viewsets.ModelViewSet):
   authentication_classes=[JWTAuthentication]
   permission_classes=[IsAuthenticated]
   queryset= Project.objects.all()
   serializer_class= ProjectSerializer

class IssueViewSet(viewsets.ModelViewSet):
   authentication_classes=[JWTAuthentication]
   permission_classes=[IsAuthenticated]
   queryset= Issues.objects.all()
   serializer_class= IssueSerializer

class AssignedViewSet(viewsets.ModelViewSet):
   authentication_classes=[JWTAuthentication]
   permission_classes=[IsAuthenticated]
   queryset= Assigned.objects.all()
   serializer_class= AssignedSerializer

class CommentViewSet(viewsets.ModelViewSet):
   authentication_classes=[JWTAuthentication]
   permission_classes= [IsAuthenticated]
   queryset= Comments.objects.all()
   serializer_class= CommentSerializer


def index(request):

    if request.method =="POST":
        sub= request.POST.get('subject')
        msg= request.POST.get('message')
        email= request.POST.get('email')
        print (sub,msg,email)
        send_mail(
            sub,msg,'dipyaman.deb@gmail.com',
            [email]
        )
        return HttpResponse('email send that!')
    return render(request, 'form.html')



    



       

    