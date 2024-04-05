from django.urls import path
from . import views



urlpatterns = [
    path('',  views.QuestionDetail.as_view(),name='quest'),
    path('choice/',views.ChoiceDetail.as_view(),name='choice'),
    # path('add',views.addQuestion),
]