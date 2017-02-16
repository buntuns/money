from django.conf.urls import url

from . import views
app_name = 'gold'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add_the_income/$', views.add_the_income, name='add_the_income'),
    url(r'^history/$', views.history, name='history'),
]
