from django.urls import path
from  .views import ManagerDashboard,ManagerChiefList,StaffAdd
from .views import Banner,bannerform,ProfileManger,RecordsManager,MainMenuItems
from .views import beveragesIistAdmin,BeveragesFormAdmin,BeveragesFormUpdateAdmin

from .view2 import Main_CourceAdmin,MainCourceFormAdmin,MainCourceFormUpdateAdmin,RiceChapatiList,RiceChapatiFormAdmin
from .view2 import RiceChapatiFormUpdateAdmin,SweetCornerListAdmin,SweetCornerFormAdmin,SweetCornerUpdateAdmin
from .view2 import starterListAdmin,StarterFormAdmin,StarterFormUpdateAdmin
from .view2 import ChineseSnacksListAdmin,ChineseSnacksFormAdmin,ChineseSnacksFormUpdateAdmin

from .views import MangerLogin,MangerLogOut,profileUpdate
urlpatterns = [
    path('',MangerLogin,name='MangerLogin'),
    path('MangerLogOut/',MangerLogOut,name='MangerLogOut'),
    path('ManagerDashboard',ManagerDashboard,name='Ma_Dashboard'),
    path('ManagerChiefList/',ManagerChiefList,name='ManagerChiefList'),
    path('StaffAdd/',StaffAdd,name='StaffAdd'),

    #banner
    path('Banner/',Banner,name='Banner'),
    path('bannerform/<str:i>/',bannerform,name='bannerform'),

    #Profile
    path('ProfileManger/',ProfileManger,name='ProfileManger'),
    path("ProfileUpdate/",profileUpdate,name="profileUpdate"),


    #records
    path('RecordsManager/',RecordsManager,name='RecordsManager'),

    #MainMenuItems
    path('MainMenuItems/',MainMenuItems,name='MainMenuItems'),
    path('beveragesIistAdmin/',beveragesIistAdmin,name='beveragesIistAdmin'),
    path('BeveragesFormAdmin/',BeveragesFormAdmin,name='BeveragesFormAdmin'),
    path('BeveragesFormUpdateAdmin/<str:i>/',BeveragesFormUpdateAdmin,name='BeveragesFormUpdateAdmin'),

        #main cource
    path('Main_CourceAdmin/',Main_CourceAdmin,name='Main_CourceAdmin'),
    path('MainCourceFormAdmin/',MainCourceFormAdmin,name='MainCourceFormAdmin'),
    path('MainCourceFormUpdateAdmin/<str:i>/',MainCourceFormUpdateAdmin,name='MainCourceFormUpdateAdmin'),

    #RiceChapatiList RiceChapatiFormAdmin, 
    path('RiceChapatiList/',RiceChapatiList,name='RiceChapatiList'),
    path('RiceChapatiFormAdmin/',RiceChapatiFormAdmin,name='RiceChapatiFormAdmin'),
    path('RiceChapatiFormUpdateAdmin/<str:i>/',RiceChapatiFormUpdateAdmin,name='RiceChapatiFormUpdateAdmin'),

    #Sweet Corner     SweetCornerFormAdmin 
    path('SweetCornerListAdmin/',SweetCornerListAdmin,name='SweetCornerListAdmin'),
    path('SweetCornerFormAdmin/',SweetCornerFormAdmin,name='SweetCornerFormAdmin'),
    path('SweetCornerUpdateAdmin/<str:i>/',SweetCornerUpdateAdmin,name='SweetCornerUpdateAdmin'),


    # starterListAdmin 
    path('starterListAdmin/',starterListAdmin,name='starterListAdmin'),
    path('StarterFormAdmin/',StarterFormAdmin,name='StarterFormAdmin'),
    path('StarterFormUpdateAdmin/<str:i>/',StarterFormUpdateAdmin,name='StarterFormUpdateAdmin'),


    #chinese 
    path('ChineseSnacksListAdmin/',ChineseSnacksListAdmin,name='ChineseSnacksListAdmin'),
    path('ChineseSnacksFormAdmin/',ChineseSnacksFormAdmin,name='ChineseSnacksFormAdmin'),
    path('ChineseSnacksFormUpdateAdmin/<str:i>/',ChineseSnacksFormUpdateAdmin,name='ChineseSnacksFormUpdateAdmin'),  

]
    #path  26 to 28

