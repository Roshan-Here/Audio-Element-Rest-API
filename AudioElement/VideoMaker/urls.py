from django.urls import path
from . import views

urlpatterns = [
    path('',views.AudioCreateApiView.as_view(),name='VideoMakerpage'),
    path('<int:pk>/detail',views.AudioListApiView.as_view(),name='VideoMakerList'),
]