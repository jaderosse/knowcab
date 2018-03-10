from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name="home"),
    url(r'^index', views.index, name="index"),
    url(r'^guide', views.guide, name="guide"),
    url(r'^signup', views.signup, name="signup"),
    url(r'^login', views.login, name="login"),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^guess', views.index, name="guess"),
    url(r'^reset', views.reset, name="reset")
]