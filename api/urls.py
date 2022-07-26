from django.urls import path
from api import views
from . import views
from .views import StudioList
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path("", views.getRoutes),
    # path("musicians/", views.getMusicians),
    # path("musician/<str:pk>/", views.getMusician),
    # path("album/", views.getAlbum),
    path("musicians/", views.StudioList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
