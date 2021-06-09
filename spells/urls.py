from django.urls import path
from . import views

urlpatterns=[
    path('<int:spell_id>', views.quiz, name='quiz'),
    path('quiz', views.quiz, name='quiz'),
    path('reset', views.reset, name='reset'),
    path('<str:class_type>', views.result, name='result'),
]