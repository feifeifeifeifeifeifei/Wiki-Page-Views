from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('get-req/', views.GetRequest.as_view()),
    path('post-req/', views.PostRequest.as_view()),
    path('wikipage/', views.index)
]