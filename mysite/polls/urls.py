from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
]

# views.index is called with httprequest and the parameter catched in url 