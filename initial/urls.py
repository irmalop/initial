from django.urls import path
from .views import InitialViewList



urlpatterns = [
    path('', InitialViewList.as_view()),

]