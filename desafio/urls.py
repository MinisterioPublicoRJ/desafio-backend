from django.urls import path

from desafio.views import (
    LocalRegistradoView,
)


urlpatterns = [
    path('locais/', LocalRegistradoView.as_view(), name='locais-view')
]
