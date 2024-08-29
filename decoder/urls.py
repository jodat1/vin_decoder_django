from django.urls import path
from .views import DecodeVINAPIView

urlpatterns = [
    path('decode-vin/', DecodeVINAPIView.as_view(), name='decode_vin_api'),
]
