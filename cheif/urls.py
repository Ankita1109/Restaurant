from django.urls import path
from .views import chiefDashBoard,chief_Profile,chief_Update,List,View_List,ChiefLogin,ChiefLogout
urlpatterns = [

    path('',ChiefLogin,name='ChiefLogin'),
    path('ChiefLogout/',ChiefLogout,name='ChiefLogout'),


    path('chiefDashBoard/',chiefDashBoard,name='chiefDashBoard'),
    path('chief_Profile/',chief_Profile,name='chief_Profile'),
    path('chief_Update/<str:i>/',chief_Update,name='chief_Update'),

    path('List/',List,name='List'),
    path('View_List/<str:i>/',View_List,name='View_List'),
]
