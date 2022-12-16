from django.urls import path
from .views import HomeTemplateView, AboutusTemplateView


urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('aboutus', AboutusTemplateView.as_view(), name='aboutus'),

]