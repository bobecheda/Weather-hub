from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('favorites/', views.favorite_locations, name='favorite_locations'),
    path('favorites/delete/<int:location_id>/', views.delete_favorite, name='delete_favorite'),
    path('history/', views.search_history, name='search_history'),
]