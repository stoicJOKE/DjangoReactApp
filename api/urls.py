from django.urls import path
from . import views

urlpatterns = [
    path("", views.getRoutes),
    path("musicians/", views.getMusicians),
    path("musician/<str:pk>/", views.getMusician),
    path("album/", views.getAlbum),
]
