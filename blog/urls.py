from django.conf.urls import url
from . import views #importing djangos methods and all of our views from blog application

urlpatterns = [
    url(r'^$',views.post_list, name='post_list'),
]
