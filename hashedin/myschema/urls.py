from django.contrib import admin
from django.urls import path, include
from .import views
from myschema.views import ProjectViewSet,IssueViewSet,CommentViewSet
from rest_framework  import routers
router= routers.DefaultRouter()
router.register(r'projects',ProjectViewSet),
router.register(r'issues',IssueViewSet),
router.register(r'comments',CommentViewSet)
urlpatterns = [
    path('',views.index, name='index'),
    path('',views.index,name='form'),
    path('', include(router.urls)),

]


