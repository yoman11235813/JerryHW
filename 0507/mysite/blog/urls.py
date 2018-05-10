from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^new/', views.new, name="new"),
    url(r'^edit/', views.edit, name="edit"),
    url(r'^delete/', views.delete, name="delete"), 
]