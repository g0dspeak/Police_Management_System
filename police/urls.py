from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^signup/$', views.signuppage,name='signup_page'),
    url(r'^fill_details/$',views.signup_detail,name='signup_detail'),
    url(r'^$', views.index,name='index'),
    url(r'^login/$', views.loginpage,name='loginpage'),
    url(r'^police/(?P<username>\w+)/$', views.welcomepolice,name='welcomepolice'),
    url(r'^police/(?P<username>\w+)/edit/$', views.editpolice,name='editpolice'),
    url(r'^civilian/(?P<username>\w+)/$', views.welcomecivilian,name='welcomecivilian'),
    url(r'^civilian/(?P<username>\w+)/edit/$', views.editcivilian,name='editcivilian'),
    url(r'^logout/$',views.logout_user,name='logout'),
]