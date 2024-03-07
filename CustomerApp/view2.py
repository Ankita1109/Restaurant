from django.shortcuts import render ,redirect
from .models import SweetCornerModel,CusDashboard,Chinese_Snacks
from ManagerApp.models import CustomerItems,RecordsManger
from .form import ItemEdit,Check_TableORdelivery
from cheif.models import CheifFood

def SweetCorner(request):
    if 'CustomerUserid' not in request.session:
        return redirect("LoginCheck")
    if request.method=='POST':
        #, 'DessertId': ['2'], 'DessertType': ['sweetdish'], 'DessertCost': ['300'], 'Dessert': ['Add To Cart']}>
        if 'Dessert' in request.POST:
            cart=CustomerItems(userid_id=request.session['CustomerUserid'],ItemName=request.POST['DessertName'],itemCost=request.POST['DessertCost'],orginalCost=request.POST['DessertCost'])
            if cart:
                cart.save()
                return redirect("CartCorner")
    obj=CusDashboard.objects.filter(blockname="SweetCorner")
    if obj.exists:
        obj=obj[0].BannerImage
    else:
        obj=None
    chocolate=SweetCornerModel.objects.filter(DessertType='chocolate')
    icecream=SweetCornerModel.objects.filter(DessertType='icecream')
    sweetdish=SweetCornerModel.objects.filter(DessertType='sweetdish')
    if sweetdish:
        sweetdish=sweetdish.values()
        sweetdish=[sweetdish[i:i+3] for i in range(0,len(sweetdish),3)]
    if chocolate:
        chocolate=chocolate.values()
        chocolate=[chocolate[i:i+3] for i in range(0,len(chocolate),3)]
    if icecream:
        icecream=icecream.values()
        icecream=[icecream[i:i+3] for i in range(0,len(icecream),3)]

    return render(request,"Customer/SweetCorner.html",{'icecream':icecream,'chocolate':chocolate,'sweetdish':sweetdish,'obj':obj})


def ChocloteCorner(request):
    if 'CustomerUserid' not in request.session:
        return redirect("LoginCheck") 
    if request.method=='POST':
        
        if 'Dessert' in request.POST:
            cart=CustomerItems(userid_id=request.session['CustomerUserid'],ItemName=request.POST['DessertName'],itemCost=request.POST['DessertCost'],orginalCost=request.POST['DessertCost'])
            if cart:
                cart.save()
                return redirect("CartCorner")
    obj=CusDashboard.objects.filter(blockname="ChocolateCorner")
    if obj.exists:
        obj=obj[0].BannerImage
    else:
        obj=None
    chocolate=SweetCornerModel.objects.filter(DessertType='chocolate')
    if chocolate:
        chocolate=chocolate.values()
        chocolate=[chocolate[i:i+3] for i in range(0,len(chocolate),3)]
    return render(request,"Customer/SweetCorner.html",{'chocolate':chocolate,'obj':obj})

def IcecreamCorner(request):
    if 'CustomerUserid' not in request.session:
        return redirect("LoginCheck") 
    if request.method=='POST':
        
        if 'Dessert' in request.POST:
            cart=CustomerItems(userid_id=request.session['CustomerUserid'],ItemName=request.POST['DessertName'],itemCost=request.POST['DessertCost'],orginalCost=request.POST['DessertCost'])
            if cart:
                cart.save()
                return redirect("CartCorner")


    obj=CusDashboard.objects.filter(blockname="IceCreamCorner")
    if obj.exists:
        obj=obj[0].BannerImage
    else:
        obj=None
    icecream=SweetCornerModel.objects.filter(DessertType='icecream')
    if icecream:
        icecream=icecream.values()
        icecream=[icecream[i:i+3] for i in range(0,len(icecream),3)]
    return render(request,"Customer/SweetCorner.html",{'icecream':icecream,'obj':obj})

def SweetdishCorner(request):
    if 'CustomerUserid' not in request.session:
        return redirect("LoginCheck") 
        
    if request.method=='POST':
        
        if 'Dessert' in request.POST:
            cart=CustomerItems(userid_id=request.session['CustomerUserid'],ItemName=request.POST['DessertName'],itemCost=request.POST['DessertCost'],orginalCost=request.POST['DessertCost'])
            if cart:
                cart.save()
                return redirect("CartCorner")
    obj=CusDashboard.objects.filter(blockname="IceCreamCorner")
    if obj.exists:
        obj=obj[0].BannerImage
    else:
        obj=None
    sweetdish=SweetCornerModel.objects.filter(DessertType='sweetdish')
    if sweetdish:
        sweetdish=sweetdish.values()
        sweetdish=[sweetdish[i:i+3] for i in range(0,len(sweetdish),3)]
    return render(request,"Customer/SweetCorner.html",{'sweetdish':sweetdish,'obj':obj})




#Chinese or snacks
def ChineseDish(request):
    if 'CustomerUserid' not in request.session:
        return redirect("LoginCheck")

    banner=CusDashboard.objects.filter(blockname="ChineseDish")
    if banner.exists:
        banner=banner[0].BannerImage
    else:
        banner=None
        
    obj=Chinese_Snacks.objects.filter(Check='chinese')
    if obj:
        obj=obj.values()
        obj=[obj[i:i+3] for i in range(0,len(obj),3)]
    return render(request,"Customer/Chinese_snacks.html",{'dish':{'obj':obj,'banner':banner,'header':'Chinese Dish','title':'Chinese Dish'}})


def SnacksDish(request):
    if 'CustomerUserid' not in request.session:
        return redirect("LoginCheck")

    banner=CusDashboard.objects.filter(blockname="SnacksDish")
    if banner.exists:
        banner=banner[0].BannerImage
    else:
        banner=None
    obj=Chinese_Snacks.objects.filter(Check='snacks')
    if obj:
        obj=obj.values()
        obj=[obj[i:i+3] for i in range(0,len(obj),3)]
    return render(request,"Customer/Chinese_snacks.html",{'dish':{'obj':obj,'banner':banner,'header':'Snacks Dish','title':'Snacks Dish'}})












'''CART SECTION START FROM HERE'''

def CartCorner(request):
    if 'CustomerUserid' not in request.session:
        return redirect("LoginCheck")
    try:
        obj= CustomerItems.objects.filter(userid_id=request.session['CustomerUserid'])
        if obj:
            obj=obj.values('id','ItemName','quantity','itemCost')
            totalvalue=0
            for i in obj:
                totalvalue+=(int(i['itemCost']))
            gst=((8/100) * totalvalue)+totalvalue
            service=((5/100) * gst)+gst
            cart=True
        else:
            cart =False
            
        return render(request,"Customer/Add_Cart.html",{'cart':cart,'obj':obj,'Amount':{'totalvalue':totalvalue,'gst':gst,'service':service}})
    except:
        return render(request,"Customer/Add_Cart.html",{'cart':cart,'obj':obj,'Amount':''})
def CartItemDel(request,i):
    try:
        obj=CustomerItems.objects.get(pk=i)
        obj.delete()        
    except:
        pass
    return redirect("CartCorner")
def CartItemFormEdit(request,i):
    obj=CustomerItems.objects.get(pk=i)
    if request.method=='POST':
        if int(request.POST['quantity'])>0:
            fm=ItemEdit(request.POST,instance=obj)
            if fm.is_valid():
                fm.save()                
                CustomerItems.objects.filter(pk=i).update(itemCost=(int(obj.orginalCost)*int(request.POST['quantity'])))
                
                return redirect("CartCorner")
    print(list(i))
    form=ItemEdit(instance=obj)
    return render(request,"Customer/form.html",{'form':form,'header':'quatity edit .'})
def Itemcheck(request,i):
    if request.method=='POST':
        if 'Submit' in request.POST:
            if (request.POST['Select'])=='Table':
                print(request.POST)
                return redirect("OrderItem",i,request.POST['Select'])
    form=Check_TableORdelivery()
    return render(request,"Customer/form.html",{'form':form,'header':'quatity edit .'})

def OrderItem(request,i,check):  
    print(i,check)  
    return render(request,"Customer/previewPage.html",{'user':{'userid':request.session['CustomerUserid'],'total':i,'check':check}})






def PaymentOrder(request,i,check):
    obj=RecordsManger(userid_id=request.session['CustomerUserid'],Check=check,TotalCost=i)
    if obj:
        obj.save()
        obj1= CustomerItems.objects.filter(userid_id=request.session['CustomerUserid'])
        if obj1:
            for i in obj1:
                o=CheifFood(userid=request.session['CustomerUserid'],dishname =i.ItemName,quantity=i.quantity)
                if o:
                    o.save()
                i.delete()
    return redirect("OrderItem",i,check)