from django.urls import path
from .views import CustomUserCreate, BlacklistTokenUpdateView,PredictionRead,SklearnPrediction

app_name = 'users'

urlpatterns = [
    path('get/',CustomUserCreate.as_view(),name='getallusers'),
    path('create/', CustomUserCreate.as_view(), name="create_user"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist'),
    path('predict/',PredictionRead.as_view(),name='prediction'),
    path('sklearnpredict/',SklearnPrediction.as_view(),name='sklearnpredict')
]