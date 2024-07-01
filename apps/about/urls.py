from django.urls import path
from apps.about.views import about

urlpatterns = [
    path('about-us/', about, name = 'about')
]