from django.urls import path
from .views import index, contato, info, dados, dados2


urlpatterns = [
    path('', index),
    path('contato/', contato),
    path('info/', info),
    path('dados/<nome>/<int:idade>', dados),
    path('dados2/<nome>/<int:idade>', dados2)
]