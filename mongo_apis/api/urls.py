from django.urls import path
from .views import HaloList, HaloDetail

urlpatterns = [
   
   
    path('Halo/', HaloList.as_view()),

    path('Halo/<str:id>/', HaloDetail.as_view()),
]
