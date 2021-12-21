from django.conf.urls import include
from django.urls import path
from levelupapi.views import register_user, login_user

## Notice register & login are imported from views & that's imported from the __init__.py & auth.py(where you made it)
urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
