from django.urls import path
from .views import (home,about,event,rules_regulation,
                services,collection,
                ebooks_list,hod_desk
                    )

app_name='base'


urlpatterns = [

    path('',home,name ='home'),
     path('about/',about,name ='about'),
     path('event/',event,name ='event'),
    # path('question_paper/',question_paper,name ='question_paper'),
    path('rules_regulation/',rules_regulation,name ='rules_regulation'),
    path('services/',services,name ='services'),
    path('collection/',collection,name ='collection'),
    path('ebooks_list/',ebooks_list,name ='ebooks_list'),
    path('hod_desk/',hod_desk,name ='hod_desk'),
    
    
]
