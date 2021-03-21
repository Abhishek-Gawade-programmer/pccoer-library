from django.urls import path
from .views import (home,about,event,rules_regulation,services,collection
                    )

app_name='base'


urlpatterns = [

    path('',home,name ='home'),
     path('about/',about,name ='about'),

    path('event/',event,name ='event'),
    path('rules_regulation/',rules_regulation,name ='rules_regulation'),
    path('services/',services,name ='services'),
    path('collection/',collection,name ='collection'),
    
    
]
