from django.core.checks import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import BeveragesModel,CusDashboard
from ManagerApp.models import CustomerBill,CustomerItems

#LoginCheck
def LoginCheck(request):
    if request.method=='POST':
        if 'Login' in request.POST:
            try:
                obj=CustomerBill.objects.get(pk=request.POST['loginUser'])
                if obj:
                    if obj.password ==request.POST['loginPassword']: 
                        request.session['CustomerUserid']=request.POST['loginUser']
                        messages.Info('request',"Login Successfull")
                        print(request.session['CustomerUserid'])
                        return redirect("UserDashboard")
                    else:
                        print("pls enter correct password")
                        messages.Info('request',"Login Successfull")
            except:
                print("Userid was not correct")
        if 'Register' in request.POST:
            pass
    return render(request,"login_form/index.html")
def LogOut(request):
    try:
        request.session.flush()
    except:
        pass
    return redirect("LoginCheck")
#check is authenticated

# Create your views here.

def CustomerDashBoard(request):
    if 'CustomerUserid' not in request.session:
        return redirect("LoginCheck")
    if request.method=='POST':
        if 'CardSubmit' in request.POST:
            print(request.POST)
    card=CusDashboard.objects.filter(BannerOfdata='card')
    if card:
        card=card.values()
        
    return render(request,"Customer/CusDashboard.html",{'card':card})






#BeveragesMenu_list.html
def BeveragesMenu_list(request):
    if 'CustomerUserid' not in request.session:
        return redirect("LoginCheck")


    if request.method=='POST':
        if 'Beverages' in request.POST:
            cart=CustomerItems(userid_id=request.session['CustomerUserid'],ItemName=request.POST['DrinkName'],itemCost=request.POST['BeveragesDrinkCost'],orginalCost=request.POST['BeveragesDrinkCost'])
            if cart:
                cart.save()
                return redirect("CartCorner")
            return redirect("BeveragesMenu_list")
    obj=CusDashboard.objects.filter(blockname="AllDrinksCorner")
    if obj.exists:
        obj=obj[0].BannerImage
    else:
        obj=None
    colddrink=BeveragesModel.objects.filter(DrinkType='colddrink')
    mocktail=BeveragesModel.objects.filter(DrinkType='mocktail')
    cocktail=BeveragesModel.objects.filter(DrinkType='cocktail')
    beer=BeveragesModel.objects.filter(DrinkType='beer')
    vodka=BeveragesModel.objects.filter(DrinkType='vodka')
    wine=BeveragesModel.objects.filter(DrinkType='wine')
    if colddrink:
        colddrink=colddrink.values()
        colddrink=[colddrink[i:i+3] for i in range(0,len(colddrink),3)]
    if mocktail:
        mocktail=mocktail.values()
        mocktail=[mocktail[i:i+3] for i in range(0,len(mocktail),3)]        
    if cocktail:
        cocktail= cocktail.values()
        cocktail=[cocktail[i:i+3] for i in range(0,len(cocktail),3)]
    if wine:
        wine=wine.values()
        wine=[wine[i:i+3] for i in range(0,len(wine),3)]
    if beer:
        beer=beer.values()
        beer=[beer[i:i+3] for i in range(0,len(beer),3)]
    if vodka:
        vodka=vodka.values()
        vodka=[vodka[i:i+3] for i in range(0,len(vodka),3)]
    return render(request,"Customer/BeveragesMenu_list.html",{'BevergesHeader':'All Drinks','colddrink':colddrink,'mocktail':mocktail,'cocktail':cocktail,'wine':wine,'vodka':vodka,'beer':beer,'obj':obj,'Beverages':'Beverages'})

def colddrinkCorner(request):
    if 'CustomerUserid' not in request.session:
        return redirect("LoginCheck")


    if request.method=='POST':
        if 'Beverages' in request.POST:
            cart=CustomerItems(userid_id=request.session['CustomerUserid'],ItemName=request.POST['DrinkName'],itemCost=request.POST['BeveragesDrinkCost'],orginalCost=request.POST['BeveragesDrinkCost'])
            if cart:
                cart.save()
                return redirect("CartCorner")
            return redirect("BeveragesMenu_list")
    obj=CusDashboard.objects.filter(blockname="colddrinkCorner")
    if obj.exists:
        obj=obj[0].BannerImage
    else:
        obj=None
    colddrink=BeveragesModel.objects.filter(DrinkType='colddrink')
    if colddrink:
        colddrink=colddrink.values()
        colddrink=[colddrink[i:i+3] for i in range(0,len(colddrink),3)]
    return render(request,"Customer/BeveragesMenu_list.html",{'BevergesHeader':'Cold Drinks Corner','colddrink':colddrink,'obj':obj,'Beverages':'ColdDrink'})

def MocktailCorner(request):
    if 'CustomerUserid' not in request.session:
        return redirect("LoginCheck")


    if request.method=='POST':
        if 'Beverages' in request.POST:
            cart=CustomerItems(userid_id=request.session['CustomerUserid'],ItemName=request.POST['DrinkName'],itemCost=request.POST['BeveragesDrinkCost'],orginalCost=request.POST['BeveragesDrinkCost'])
            if cart:
                cart.save()
                return redirect("CartCorner")
            return redirect("BeveragesMenu_list")

    obj=CusDashboard.objects.filter(blockname="MocktailCorner")
    if obj.exists:
        obj=obj[0].BannerImage
    else:
        obj=None
    mocktail=BeveragesModel.objects.filter(DrinkType='mocktail')
    if mocktail:
        mocktail=mocktail.values()
        mocktail=[mocktail[i:i+3] for i in range(0,len(mocktail),3)] 
    return render(request,"Customer/BeveragesMenu_list.html",{'BevergesHeader':'Mocktail Corner','mocktail':mocktail,'obj':obj,'Beverages':'Mocktail'})


def CocktailCorner(request):
    if 'CustomerUserid' not in request.session:
        return redirect("LoginCheck")


    if request.method=='POST':
        if 'Beverages' in request.POST:
            cart=CustomerItems(userid_id=request.session['CustomerUserid'],ItemName=request.POST['DrinkName'],itemCost=request.POST['BeveragesDrinkCost'],orginalCost=request.POST['BeveragesDrinkCost'])
            if cart:
                cart.save()
                return redirect("CartCorner")
            return redirect("BeveragesMenu_list")

    obj=CusDashboard.objects.filter(blockname="CocktailCorner")
    if obj.exists:
        obj=obj[0].BannerImage
    else:
        obj=None
    cocktail=BeveragesModel.objects.filter(DrinkType='cocktail')
    if cocktail:
        cocktail=cocktail.values()
        cocktail=[cocktail[i:i+3] for i in range(0,len(cocktail),3)]
    return render(request,"Customer/BeveragesMenu_list.html",{'BevergesHeader':'Cocktail Corner','cocktail':cocktail,'obj':obj,'Beverages':'Cocktail'})

def VodkaCorner(request):
    if 'CustomerUserid' not in request.session:
        return redirect("LoginCheck")


    if request.method=='POST':
        if 'Beverages' in request.POST:
            cart=CustomerItems(userid_id=request.session['CustomerUserid'],ItemName=request.POST['DrinkName'],itemCost=request.POST['BeveragesDrinkCost'],orginalCost=request.POST['BeveragesDrinkCost'])
            if cart:
                cart.save()
                return redirect("CartCorner")
            return redirect("BeveragesMenu_list")

    obj=CusDashboard.objects.filter(blockname="VodkaCorner")
    if obj.exists:
        obj=obj[0].BannerImage
    else:
        obj=None
    vodka=BeveragesModel.objects.filter(DrinkType='vodka')
    if vodka:
        vodka=vodka.values()
        vodka=[vodka[i:i+3] for i in range(0,len(vodka),3)]
    return render(request,"Customer/BeveragesMenu_list.html",{'BevergesHeader':'Vodka Corner','vodka':vodka,'obj':obj,'Beverages':'Vodka'})

def BeerCorner(request):
    if 'CustomerUserid' not in request.session:
        return redirect("LoginCheck")


    if request.method=='POST':
        if 'Beverages' in request.POST:
            cart=CustomerItems(userid_id=request.session['CustomerUserid'],ItemName=request.POST['DrinkName'],itemCost=request.POST['BeveragesDrinkCost'],orginalCost=request.POST['BeveragesDrinkCost'])
            if cart:
                cart.save()
                return redirect("CartCorner")
            return redirect("BeveragesMenu_list")

    obj=CusDashboard.objects.filter(blockname="BeerCorner")
    if obj.exists:
        obj=obj[0].BannerImage
    else:
        obj=None
    beer=BeveragesModel.objects.filter(DrinkType='beer')
    if beer:
        beer=beer.values()
        beer=[beer[i:i+3] for i in range(0,len(beer),3)]
    return render(request,"Customer/BeveragesMenu_list.html",{'BevergesHeader':'Beer Corner','beer':beer,'obj':obj,'Beverages':'BEER'})

def WineCorner(request):
    if 'CustomerUserid' not in request.session:
        return redirect("LoginCheck")

        
    if request.method=='POST':
        if 'Beverages' in request.POST:
            cart=CustomerItems(userid_id=request.session['CustomerUserid'],ItemName=request.POST['DrinkName'],itemCost=request.POST['BeveragesDrinkCost'],orginalCost=request.POST['BeveragesDrinkCost'])
            if cart:
                cart.save()
                return redirect("CartCorner")
            return redirect("BeveragesMenu_list")

    obj=CusDashboard.objects.filter(blockname="WineCorner")
    if obj.exists:
        obj=obj[0].BannerImage
    else:
        obj=None           
    wine=BeveragesModel.objects.filter(DrinkType='wine')
    if wine:
        wine=wine.values()
        wine=[wine[i:i+3] for i in range(0,len(wine),3)]
    return render(request,"Customer/BeveragesMenu_list.html",{'BevergesHeader':'Wine Corner','wine':wine,'obj':obj,'Beverages':'WINE'})


