from django.urls import path
from . import views

urlpatterns = [
    path('',views.AudioCreateApiView.as_view(),name='VideoMakerpage')
]