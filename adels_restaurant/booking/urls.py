from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.booking_create, name='booking_create'),
    path('list/', views.booking_list, name='booking_list'),
    path('<int:pk>/', views.booking_detail, name='booking_detail'),
    path('<int:pk>/update/', views.booking_update, name='booking_update'),
    path('<int:pk>/delete/', views.booking_delete, name='booking_delete'),
]

