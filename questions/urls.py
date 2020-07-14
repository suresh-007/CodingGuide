from django.urls import path
from .views import questions_list,display_question

app_name = 'questions'

urlpatterns = [
    path('', questions_list,name='questions_list'),
    path('question/<id>/',display_question,name='display_question'),
]
