from django.shortcuts import render ,redirect
from CustomerApp.models import Starter,Main_CourceModel,RiceChapati,Chinese_Snacks,SweetCornerModel
from .form import MainCourceForm,RiceChapatiForm,SweetCornerModelForm,StarterForm,Chinese_SnacksForm

#Main cource

def Main_CourceAdmin(request):
    if 'ManagerUserid' not in request.session:
        return redirect("MangerLogin")

    if request.method=="POST":
        if 'Delete' in request.POST:
            pk=Main_CourceModel.objects.get(pk=request.POST['id'])
            pk.delete()
            return redirect("Main_CourceAdmin")
        elif 'view' in request.POST:
            print(request.POST['id'])
            return redirect("MainCourceFormUpdateAdmin",i=request.POST['id'])
        elif 'AddItems' in request.POST:
            return redirect("MainCourceFormAdmin")
    obj=Main_CourceModel.objects.filter(Check='veg')
    obj1=Main_CourceModel.objects.filter(Check='nonveg')
    obj=list(obj.values('id','categories','MaincourceName','MaincourceCost','Check'))+list(obj1.values('id','categories','MaincourceName','MaincourceCost','Check'))
    
    table=('id','categories','MaincourceName','MaincourceCost','Check')
    return render(request,"manager/MainMenuList.html",{'table':{'column':table,'data':obj,'header':'Main Cource List','btn':'Add MainCource'}})    


def MainCourceFormAdmin(request):
    if 'ManagerUserid' not in request.session:
        return redirect("MangerLogin")

    if request.method=='POST':
        fm=MainCourceForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            return redirect("beveragesIistAdmin")

    form=MainCourceForm()
    return render(request,"manager/Form.html",{'form':form,'header':' MainCource Add Form 😉'})
def MainCourceFormUpdateAdmin(request,i):
    if 'ManagerUserid' not in request.session:
        return redirect("MangerLogin")

    pk=Main_CourceModel.objects.get(pk=i)
    if request.method=='POST':
        if 'Submit' in request.POST:
            fm=MainCourceForm(request.POST,request.FILES,instance=pk)  
            if fm.is_valid():
                if request.FILES:
                    try:
                        fm.save()
                    except Exception as x:
                        print("not deleted",x)
                else:
                    fm.save()
                return redirect("Main_CourceAdmin")

    form=MainCourceForm(instance=pk)
    return render(request,"manager/Form.html",{'form':form,'header':' MainCource Add Form 😉'})

#RiceChapatisection
def RiceChapatiList(request):
    if 'ManagerUserid' not in request.session:
        return redirect("MangerLogin")

    if request.method=='POST':
        if 'AddItems' in request.POST:
            print(request.POST['AddItems'])
            return redirect("RiceChapatiFormAdmin")
        elif 'view' in request.POST:
            return redirect("RiceChapatiFormUpdateAdmin",i=request.POST['id'])
        elif 'Delete' in request.POST:
            obj=RiceChapati.objects.get(pk=request.POST['id'])
            obj.delete()
            return redirect("RiceChapatiList")
    obj=RiceChapati.objects.all()
    obj=obj.values('id','ItemName','ItemCost','Check')
    table=('id','ItemName','ItemCost','Check')
    return render(request,"manager/MainMenuList.html",{'table':{'column':table,'data':obj,'header':'Rice & Chapti List','btn':'Add Rice & Chapti'}}) 

def RiceChapatiFormAdmin(request):
    if 'ManagerUserid' not in request.session:
        return redirect("MangerLogin")

    if request.method=='POST':
        fm=RiceChapatiForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            return redirect("RiceChapatiList")

    form=RiceChapatiForm()
    return render(request,"manager/Form.html",{'form':form,'header':' Rice & Chapati Form 😉'})

def RiceChapatiFormUpdateAdmin(request,i):
    if 'ManagerUserid' not in request.session:
        return redirect("MangerLogin")

    pk=RiceChapati.objects.get(pk=i)
    if request.method=='POST':
        if 'Submit' in request.POST:
            fm=RiceChapatiForm(request.POST,request.FILES,instance=pk) 
            if fm.is_valid():
                if request.FILES:
                    try:
                        fm.save()
                    except Exception as x:
                        print("not deleted",x)
                else:
                    fm.save()
                return redirect("RiceChapatiList")      
    form=RiceChapatiForm(instance=pk)
    return render(request,"manager/Form.html",{'form':form,'header':' Rice & Chapati Form 😉'})




#sweet Corner
def SweetCornerListAdmin(request):
    if 'ManagerUserid' not in request.session:
        return redirect("MangerLogin")

    if request.method=='POST':
        if 'AddItems' in request.POST:
            print(request.POST['AddItems'])
            return redirect("SweetCornerFormAdmin")            
        elif 'view' in request.POST:
            return redirect("SweetCornerUpdateAdmin",i=request.POST['id'])
        elif 'Delete' in request.POST:
            obj=SweetCornerModel.objects.get(pk=request.POST['id'])
            obj.delete()
            return redirect("SweetCornerListAdmin")    
    obj=SweetCornerModel.objects.all()
    obj=obj.values('id','DessertType','DessertName','DessertCost')
    table=('id','DessertType','DessertName','DessertCost')
    return render(request,"manager/MainMenuList.html",{'table':{'column':table,'data':obj,'header':'Sweet Corner List','btn':'Add Desert'}}) 

def SweetCornerFormAdmin(request):
    if 'ManagerUserid' not in request.session:
        return redirect("MangerLogin")

    if request.method=='POST':
        fm=SweetCornerModelForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            return redirect("SweetCornerListAdmin")

    form=SweetCornerModelForm()
    return render(request,"manager/Form.html",{'form':form,'header':' Add Dessert Form .'})
def SweetCornerUpdateAdmin(request,i):
    if 'ManagerUserid' not in request.session:
        return redirect("MangerLogin")

    pk=SweetCornerModel.objects.get(pk=i)
    if request.method=='POST':
        if 'Submit' in request.POST:
            fm=SweetCornerModelForm(request.POST,request.FILES,instance=pk) 
            if fm.is_valid():
                if request.FILES:
                    try:
                        fm.save()
                    except Exception as x:
                        print("not deleted",x)
                else:
                    fm.save()
                return redirect("SweetCornerListAdmin")      
    form=SweetCornerModelForm(instance=pk)
    return render(request,"manager/Form.html",{'form':form,'header':' Update Dessert Form 😉'})


#starter

def starterListAdmin(request):
    if 'ManagerUserid' not in request.session:
        return redirect("MangerLogin")

    if request.method=='POST':
        if 'AddItems' in request.POST:
            print(request.POST['AddItems'])  
            return redirect("StarterFormAdmin")          
        elif 'view' in request.POST:
            return redirect("StarterFormUpdateAdmin",i=request.POST['id'])
        elif 'Delete' in request.POST:
            obj=Starter.objects.get(pk=request.POST['id'])
            obj.delete()
            return redirect("starterListAdmin")    
    obj=Starter.objects.all()
    obj=obj.values('id','categories','StarterName','Startercost','Check')
    table=('id','categoriesd','StarterName','Startercost','Check')
    return render(request,"manager/MainMenuList.html",{'table':{'column':table,'data':obj,'header':'Starter List','btn':'Add Starter'}}) 

#StarterForm
def StarterFormAdmin(request):
    if 'ManagerUserid' not in request.session:
        return redirect("MangerLogin")

    if request.method=='POST':
        fm=StarterForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            return redirect("starterListAdmin")

    form=StarterForm()
    return render(request,"manager/Form.html",{'form':form,'header':' Add Starter Form .'})

def StarterFormUpdateAdmin(request,i): 
    if 'ManagerUserid' not in request.session:
        return redirect("MangerLogin")

    pk=Starter.objects.get(pk=i)
    if request.method=='POST':
        if 'Submit' in request.POST:
            fm=StarterForm(request.POST,request.FILES,instance=pk) 
            if fm.is_valid():
                if request.FILES:
                    try:
                        fm.save()
                    except Exception as x:
                        print("not deleted",x)
                else:
                    fm.save()
                return redirect("starterListAdmin")      
    form=StarterForm(instance=pk)
    return render(request,"manager/Form.html",{'form':form,'header':' Update Dessert Form 😉'})




#ChineseSnacks
def ChineseSnacksListAdmin(request):
    if 'ManagerUserid' not in request.session:
        return redirect("MangerLogin")

    if request.method=='POST':
        if 'AddItems'  in request.POST:
            print(request.POST['AddItems'])  
            return redirect("ChineseSnacksFormAdmin")          
        elif 'view' in request.POST:
            return redirect("ChineseSnacksFormUpdateAdmin",i=request.POST['id'])
        elif 'Delete' in request.POST:
            obj=Chinese_Snacks.objects.get(pk=request.POST['id'])
            obj.delete()
            return redirect("ChineseSnacksListAdmin")    
    obj=Chinese_Snacks.objects.all()
    obj=obj.values('id','ItemName','ItemCost','Check')
    table=('id','ItemName','ItemCost','Check')
    return render(request,"manager/MainMenuList.html",{'table':{'column':table,'data':obj,'header':'Chinese-Snacks List','btn':'Add Chinese-Snacks'}}) 

#StarterForm
def ChineseSnacksFormAdmin(request):
    if 'ManagerUserid' not in request.session:
        return redirect("MangerLogin")

    if request.method=='POST':
        fm=Chinese_SnacksForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            return redirect("ChineseSnacksListAdmin")

    form=Chinese_SnacksForm()
    return render(request,"manager/Form.html",{'form':form,'header':' Add Chinese-Snacks Form .'})

def ChineseSnacksFormUpdateAdmin(request,i): 
    if 'ManagerUserid' not in request.session:
        return redirect("MangerLogin")
        
    pk=Chinese_Snacks.objects.get(pk=i)
    if request.method=='POST':
        if 'Submit' in request.POST:
            fm=Chinese_SnacksForm(request.POST,request.FILES,instance=pk) 
            if fm.is_valid():
                if request.FILES:
                    try:
                        fm.save()
                    except Exception as x:
                        print("not deleted",x)
                else:
                    fm.save()
                return redirect("ChineseSnacksListAdmin")      
    form=Chinese_SnacksForm(instance=pk)
    return render(request,"manager/Form.html",{'form':form,'header':' Update Dessert Form 😉'})
