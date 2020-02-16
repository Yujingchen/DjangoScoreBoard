"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/',include('polls.urls'))
]

# when processing a request, django start searching at first pattern and makes it way down
# when it matches with "polls" it chop off from there and send the remain string to polls.urlconf

#question
#how to pass parameter to polls url? for example www.example/polls/?page=3
#route Patterns don’t search GET and POST parameters, or the domain name. no answered 