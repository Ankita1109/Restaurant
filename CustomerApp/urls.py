from django.urls import path
from .views import CustomerDashBoard,BeveragesMenu_list
from .views import colddrinkCorner,MocktailCorner,CocktailCorner,VodkaCorner,BeerCorner,WineCorner
from .view2 import SweetCorner,ChocloteCorner,IcecreamCorner,SweetdishCorner
from .view2 import ChineseDish,SnacksDish,CartCorner
from .veiws3 import MenuList,ThaiMenuList,ContentailMenuList,ItalianMenuList,NonVegetraianList,VegetraianList,StarterMenuList
from .views import LoginCheck,LogOut
from .view2 import CartItemDel,CartItemFormEdit,OrderItem,PaymentOrder
from .view2 import Itemcheck

urlpatterns = [
    path('',LoginCheck,name='LoginCheck'),
    path('LogOut/',LogOut,name='LogOut'),

    
    path('UserDashboard/',CustomerDashBoard,name='UserDashboard'),

    #menu urls
    path('MenuList/',MenuList,name='MenuList'),
    path('ThaiMenuList/',ThaiMenuList,name='ThaiMenuList'),
    path('StarterMenuList/',StarterMenuList,name='StarterMenuList'),
    path('ContentailMenuList/',ContentailMenuList,name='ContentailMenuList'),
    path('ItalianMenuList/',ItalianMenuList,name='ItalianMenuList'),
    path('NonVegetraianList/',NonVegetraianList,name='NonVegetraianList'),
    path('VegetraianList/',VegetraianList,name='VegetraianList'),

    #beverages urls
    path('BeveragesMenu_list/',BeveragesMenu_list,name='BeveragesMenu_list'),
    path('colddrinkCorner/',colddrinkCorner,name='colddrinkCorner'),
    path('MocktailCorner/',MocktailCorner,name='MocktailCorner'),
    path('CocktailCorner/',CocktailCorner,name='CocktailCorner'),
    path('VodkaCorner/',VodkaCorner,name='VodkaCorner'),
    path('BeerCorner/',BeerCorner,name='BeerCorner'),
    path('WineCorner/',WineCorner,name='WineCorner'),

    #sweet corner urls
    path('SweetCorner/',SweetCorner,name='SweetCorner'),
    path('ChocloteCorner/',ChocloteCorner,name='ChocloteCorner'),
    path('IcecreamCorner/',IcecreamCorner,name='IcecreamCorner'),
    path('SweetdishCorner/',SweetdishCorner,name='SweetdishCorner'),

    #ChineseDish,snacks
    path('ChineseDish/',ChineseDish,name='ChineseDish'),
    path('SnacksDish/',SnacksDish,name='SnacksDish'),

    #CartCorner CartItemDel  
    path('CartCorner/',CartCorner,name='CartCorner'),
    path('CartItemDel/<str:i>/',CartItemDel,name='CartItemDel'),
    path('CartItemFormEdit/<str:i>/',CartItemFormEdit,name='CartItemFormEdit'),
    path('Itemcheck/<str:i>/',Itemcheck,name='Itemcheck'),
    path('OrderItem/<str:i>/<str:check>',OrderItem,name='OrderItem'),
    path('PaymentOrder/<str:i>/<str:check>',PaymentOrder,name='PaymentOrder'),


]
