from django.conf.urls import url
from vwp_app import views

# Template Tagging
app_name = 'vwp_app'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^help/',views.help,name='help'),
    url(r'^mainvwp/',views.mainvwp,name='mainvwp'),
    url(r'^adduser/',views.adduser,name='adduser'),
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^registration/$',views.registration,name='registration'),
    url(r'^logout/$',views.user_logout,name='user_logout'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]
