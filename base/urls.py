from django.urls import path
from .views import (home,about,event
                    )

app_name='base'


urlpatterns = [

    path('',home,name ='home'),
     path('about/',about,name ='about'),

    path('event/',event,name ='event'),
    
    
]
