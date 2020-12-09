from django.conf.urls import url, include
from apps.dato.views import index

urlpatterns = [
    url(r'^$', index),

    
]