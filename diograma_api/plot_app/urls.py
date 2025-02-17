from django.urls import path
from .views import PlotAPIView

urlpatterns = [
    path('plot/', PlotAPIView.as_view(), name='plot_api'),
]
