from django.urls import path
from profiles_api import views


urlpatterns=[path("hello-view/",views.HelloWorldAPIView.as_view())] #After we hit/api/hello-view/ from browser this will convert heloworldaoiview to view n diaplay inn the UI
