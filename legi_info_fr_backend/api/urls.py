from django.urls import path
from . import views

urlpatterns = [
    path('deputes', views.deputeList, name="deputes"),
    path('deputes/<str:pk>/synthese', views.syntheseByDepute, name="synthesesByDepute"),
    path('groupes', views.groupeList, name="groupes"),
]