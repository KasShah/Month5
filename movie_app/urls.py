from django.urls import path
from . import views

urlpatterns = [
    path('directors/', views.directors_api_view),
    path('directors/<int:id>/', views.directors_detail_api_view),
    path('movies/', views.movies_api_view),
    path('movies/<int:id>', views.movies_detail_api_view),
    path('reviews/', views.reviews_api_view),
    path('reviews/<int:id>', views.reviews_detail_api_view),

]