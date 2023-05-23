from django.urls import path
from . import views

urlpatterns = [
    path('',views.AudioCreateApiView.as_view(),name='VideoMakerpage'),
    path('<int:pk>',views.AudioListApiView.as_view(),name='VideoMakerList'),
    path('<int:pk>/update',views.AudioUpdateApiView.as_view(),name='VideoMakerUpdate'),
    path('<int:pk>/delete',views.AudioDeleteApiView.as_view(),name='VideoMakerUpdate'),
    path('all',views.AudioListApiView.as_view(),name='VideoMakerViewAll'),
]