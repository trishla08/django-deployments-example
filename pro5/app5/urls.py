from django.conf.urls import url
from app5 import views

app_name = 'app5'

urlpatterns=[

      url(r'^register/', views.register, name='register'),
      url(r'^user_login/', views.user_login, name='user_login'),
      url(r'myprofile/(?P<username>[a-zA-Z0-9]+)$', views.profilepage, name='profilepage'),


]