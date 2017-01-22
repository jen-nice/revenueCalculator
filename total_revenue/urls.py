from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^money_view/$', views.money_view, name='money_view'),
]
