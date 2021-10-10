from django.urls import path
from eduai import views
urlpatterns = [
    path("", views.home, name="home"),
]
#changegit commit -a -m "message"