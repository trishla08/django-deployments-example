from django.conf.urls import url, include
from app5 import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'app5'

urlpatterns=[


      url(r'^register/', views.register, name='register'),
      url(r'^search/', views.search, name='search'),
      url(r'^user_login/', views.user_login, name='user_login'),
      url(r'user_status/(?P<username>[a-zA-Z0-9]+)$', views.user_status, name='user_status'),
      url(r'myprofile/(?P<username>[a-zA-Z0-9]+)$', views.profilepage, name='profilepage'),
      

]

