from django.urls import path
from .views import Bovino_Create

urlpatterns = [
    path('bovino/', Bovino_Create.as_view(), name="bovino_crear"),
]