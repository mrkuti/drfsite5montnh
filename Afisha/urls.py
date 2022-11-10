from django.contrib import admin
from django.urls import path
from movie_app import views
from user import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),


    path('api/v1/directors/', views.directors),
    path('api/v1/directors/<int:id>/', views.director_item),



    path('api/v1/movies/', views.movies),
    path('api/v1/movies/<int:id>/', views.movie_item),


    path('api/v1/revies/', views.reviews),
    path('api/v1/revies/<int:id>/', views.review_item),


    path('api/v1/authorization/', user_views.authorization),
    path('api/v1/registration/', user_views.registration),

]