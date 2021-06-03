from django.urls import path
from . import user
urlpatterns = [
    path('login', user.login),
    # path('test/',urls.urls)
]