from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add/<int:arg_1>/<int:arg_2>/', views.add, name='add'),
    path('subtract/<int:arg_1>/<int:arg_2>/', views.subtract, name='subtract')
]
