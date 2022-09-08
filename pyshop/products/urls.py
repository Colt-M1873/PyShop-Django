from django.urls import path
from . import views

urlpatterns = [
    path('',views.index), # root of this app, i.e products/
    path('testnew/',views.testnewResponse), # products/testnew/

]