from django.urls import path
from . import views

urlpatterns=[
    path('<int:spell_id>', views.index, name='index'),
    path('', views.index, name='index'),
    path('reset', views.reset, name='reset'),
    path('<str:class_type>', views.result, name='result'),
]