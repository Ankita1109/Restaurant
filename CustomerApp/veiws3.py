from django.shortcuts import redirect,render
from .models import Starter,Main_CourceModel,CusDashboard,RiceChapati
from ManagerApp.models import CustomerItems

def MenuList(request):
    if 'CustomerUserid' not in request.session:
        return redirect("LoginCheck")

    if request.method=='POST':
        if "Menusubmit" in request.POST:
            item_name=request.POST["itemname"]
            cost=request.POST['cost']
            cart=CustomerItems(userid_id=request.session['CustomerUserid'],ItemName=item_name,itemCost=cost,orginalCost=cost)
            if cart:
                cart.save()
                return redirect("CartCorner")
            
    banner=CusDashboard.objects.filter(blockname="FoodMenuList")
    if banner.exists:
        banner=banner[0].BannerImage
    else:
        banner=None
    st_veg=Starter.objects.filter(Check='veg')
    st_nonveg=Starter.objects.filter(Check='nonveg')
    main_veg=Main_CourceModel.objects.filter(Check='veg')
    main_nonveg=Main_CourceModel.objects.filter(Check='nonveg')
    chapati=RiceChapati.objects.filter(Check='chapati')
    rice=RiceChapati.objects.filter(Check='rice')
    if rice:
        rice=rice.values()
        rice=[rice[i:i+3] for i in range(0,len(rice),3)]
    if chapati:
        chapati=chapati.values()
        chapati=[chapati[i:i+3] for i in range(0,len(chapati),3)]

    if st_veg:
        st_veg=st_veg.values()
        st_veg=[st_veg[i:i+3] for i in range(0,len(st_veg),3)]
    if st_nonveg:
        st_nonveg=st_nonveg.values()
        st_nonveg=[st_nonveg[i:i+3] for i in range(0,len(st_nonveg),3)]
    if main_veg:
        main_veg=main_veg.values()
        main_veg=[main_veg[i:i+3] for i in range(0,len(main_veg),3)]
    if main_nonveg:
        main_nonveg=main_nonveg.values()
        main_nonveg=[main_nonveg[i:i+3] for i in range(0,len(main_nonveg),3)]
    return render(request,"Customer/Menu_list.html",{'starter':{'veg':st_veg,'nonveg':st_nonveg},"maincource":{'veg':main_veg,'nonveg':main_nonveg},'ricechapti':{'chapati':chapati,'rice':rice} ,'HeaderName':{'name':'Welcome To Foodcot','para':'Feel fresh to Eat','menu':'Main Menu','profile':banner} })

def StarterMenuList(request):
    if 'CustomerUserid' not in request.session:
        return redirect("LoginCheck")

    if request.method=='POST':
        if "Menusubmit" in request.POST:
            item_name=request.POST["itemname"]
            cost=request.POST['cost']
            cart=CustomerItems(userid_id=request.session['CustomerUserid'],ItemName=item_name,itemCost=cost,orginalCost=cost)
            if cart:
                cart.save()
                return redirect("CartCorner")
            
    banner=CusDashboard.objects.filter(blockname="StarterMenuList")
    if banner.exists:
        banner=banner[0].BannerImage
    else:
        banner=None       
    st_veg=Starter.objects.filter(Check='veg')
    st_nonveg=Starter.objects.filter(Check='nonveg')
    
    
    if st_veg:
        st_veg=st_veg.values()
        st_veg=[st_veg[i:i+3] for i in range(0,len(st_veg),3)]
    if st_nonveg:
        st_nonveg=st_nonveg.values()
        st_nonveg=[st_nonveg[i:i+3] for i in range(0,len(st_nonveg),3)]
  
    return render(request,"Customer/Menu_list.html",{'starter':{'veg':st_veg,'nonveg':st_nonveg} ,'HeaderName':{'name':'Welcome To Foodcot','para':'Feel fresh to Eat','menu':'Starter Menu','profile':banner} })


def VegetraianList(request):
    if 'CustomerUserid' not in request.session:
        return redirect("LoginCheck")

    if request.method=='POST':
        if "Menusubmit" in request.POST:
            item_name=request.POST["itemname"]
            cost=request.POST['cost']
            cart=CustomerItems(userid_id=request.session['CustomerUserid'],ItemName=item_name,itemCost=cost,orginalCost=cost)
            if cart:
                cart.save()
                return redirect("CartCorner")
            
    banner=CusDashboard.objects.filter(blockname="VegetraianList")
    if banner.exists:
        banner=banner[0].BannerImage
    else:
        banner=None
    st_veg=Starter.objects.filter(Check='veg')    
    main_veg=Main_CourceModel.objects.filter(Check='veg') 
    chapati=RiceChapati.objects.filter(Check='chapati')
    rice=RiceChapati.objects.filter(Check='rice')
    if rice:
        rice=rice.values()
        rice=[rice[i:i+3] for i in range(0,len(rice),3)]
    if chapati:
        chapati=chapati.values()
        chapati=[chapati[i:i+3] for i in range(0,len(chapati),3)]   
    if st_veg:
        st_veg=st_veg.values()
        st_veg=[st_veg[i:i+3] for i in range(0,len(st_veg),3)]
    if main_veg:
        main_veg=main_veg.values()
        main_veg=[main_veg[i:i+3] for i in range(0,len(main_veg),3)]
    return render(request,"Customer/Menu_list.html",{'starter':{'veg':st_veg,'nonveg':''},"maincource":{'veg':main_veg,'nonveg':''} ,'ricechapti':{'chapati':chapati,'rice':rice},'HeaderName':{'name':'Welcome To Foodcot','para':'Feel fresh to Eat','menu':'Vegetraian Menu','profile':banner} })


def NonVegetraianList(request):
    if 'CustomerUserid' not in request.session:
        return redirect("LoginCheck")


    if request.method=='POST':
        if "Menusubmit" in request.POST:
            item_name=request.POST["itemname"]
            cost=request.POST['cost']
            cart=CustomerItems(userid_id=request.session['CustomerUserid'],ItemName=item_name,itemCost=cost,orginalCost=cost)
            if cart:
                cart.save()
                return redirect("CartCorner")
                     
    banner=CusDashboard.objects.filter(blockname="NonVegetraianList")
    if banner.exists:
        banner=banner[0].BannerImage
    else:
        banner=None
    st_nonveg=Starter.objects.filter(Check='nonveg')
    main_nonveg=Main_CourceModel.objects.filter(Check='nonveg')
    chapati=RiceChapati.objects.filter(Check='chapati')
    rice=RiceChapati.objects.filter(Check='rice')
    if rice:
        rice=rice.values()
        rice=[rice[i:i+3] for i in range(0,len(rice),3)]
    if chapati:
        chapati=chapati.values()
        chapati=[chapati[i:i+3] for i in range(0,len(chapati),3)]
    if st_nonveg:
        st_nonveg=st_nonveg.values()
        st_nonveg=[st_nonveg[i:i+3] for i in range(0,len(st_nonveg),3)]
    if main_nonveg:
        main_nonveg=main_nonveg.values()
        main_nonveg=[main_nonveg[i:i+3] for i in range(0,len(main_nonveg),3)]
    return render(request,"Customer/Menu_list.html",{'starter':{'veg':'','nonveg':st_nonveg},"maincource":{'veg':'','nonveg':main_nonveg},'ricechapti':{'chapati':chapati,'rice':rice} ,'HeaderName':{'name':'Welcome To Foodcot','para':'Feel fresh to Eat','menu':'Non Vegetraian Menu','profile':banner} })


def ItalianMenuList(request):
    if 'CustomerUserid' not in request.session:
        return redirect("LoginCheck")


    if request.method=='POST':
        if "Menusubmit" in request.POST:
            item_name=request.POST["itemname"]
            cost=request.POST['cost']
            cart=CustomerItems(userid_id=request.session['CustomerUserid'],ItemName=item_name,itemCost=cost,orginalCost=cost)
            if cart:
                cart.save()
                return redirect("CartCorner")
            
    banner=CusDashboard.objects.filter(blockname="ItalianMenuList")
    if banner.exists:
        banner=banner[0].BannerImage
    else:
        banner=None       
    st_veg=Starter.objects.filter(Check='veg',categories_id='italian')
    st_nonveg=Starter.objects.filter(Check='nonveg',categories_id='italian')
    main_veg=Main_CourceModel.objects.filter(Check='veg',categories_id='italian')
    main_nonveg=Main_CourceModel.objects.filter(Check='nonveg',categories_id='italian')
    chapati=RiceChapati.objects.filter(Check='chapati')
    rice=RiceChapati.objects.filter(Check='rice')
    if rice:
        rice=rice.values()
        rice=[rice[i:i+3] for i in range(0,len(rice),3)]
    if chapati:
        chapati=chapati.values()
        chapati=[chapati[i:i+3] for i in range(0,len(chapati),3)]
    if st_veg:
        st_veg=st_veg.values()
        st_veg=[st_veg[i:i+3] for i in range(0,len(st_veg),3)]
    if st_nonveg:
        st_nonveg=st_nonveg.values()
        st_nonveg=[st_nonveg[i:i+3] for i in range(0,len(st_nonveg),3)]
    if main_veg:
        main_veg=main_veg.values()
        main_veg=[main_veg[i:i+3] for i in range(0,len(main_veg),3)]
    if main_nonveg:
        main_nonveg=main_nonveg.values()
        main_nonveg=[main_nonveg[i:i+3] for i in range(0,len(main_nonveg),3)]
    return render(request,"Customer/Menu_list.html",{'starter':{'veg':st_veg,'nonveg':st_nonveg},"maincource":{'veg':main_veg,'nonveg':main_nonveg} ,'ricechapti':{'chapati':chapati,'rice':rice},'HeaderName':{'name':'Welcome To Foodcot','para':'Feel fresh to Eat','menu':'Italian Menu','profile':banner} })


def ContentailMenuList(request):
    if 'CustomerUserid' not in request.session:
        return redirect("LoginCheck")


    if request.method=='POST':
        if "Menusubmit" in request.POST:
            item_name=request.POST["itemname"]
            cost=request.POST['cost']
            cart=CustomerItems(userid_id=request.session['CustomerUserid'],ItemName=item_name,itemCost=cost,orginalCost=cost)
            if cart:
                cart.save()
                return redirect("CartCorner")
            
    banner=CusDashboard.objects.filter(blockname="ContentailMenuList")
    if banner.exists:
        banner=banner[0].BannerImage
    else:
        banner=None        
    st_veg=Starter.objects.filter(Check='veg',categories_id='continenetal')
    st_nonveg=Starter.objects.filter(Check='nonveg',categories_id='continenetal')
    main_veg=Main_CourceModel.objects.filter(Check='veg',categories_id='continenetal')
    main_nonveg=Main_CourceModel.objects.filter(Check='nonveg',categories_id='continenetal')
    chapati=RiceChapati.objects.filter(Check='chapati')
    rice=RiceChapati.objects.filter(Check='rice')
    if rice:
        rice=rice.values()
        rice=[rice[i:i+3] for i in range(0,len(rice),3)]
    if chapati:
        chapati=chapati.values()
        chapati=[chapati[i:i+3] for i in range(0,len(chapati),3)]
    if st_veg:
        st_veg=st_veg.values()
        st_veg=[st_veg[i:i+3] for i in range(0,len(st_veg),3)]
    if st_nonveg:
        st_nonveg=st_nonveg.values()
        st_nonveg=[st_nonveg[i:i+3] for i in range(0,len(st_nonveg),3)]
    if main_veg:
        main_veg=main_veg.values()
        main_veg=[main_veg[i:i+3] for i in range(0,len(main_veg),3)]
    if main_nonveg:
        main_nonveg=main_nonveg.values()
        main_nonveg=[main_nonveg[i:i+3] for i in range(0,len(main_nonveg),3)]
    return render(request,"Customer/Menu_list.html",{'starter':{'veg':st_veg,'nonveg':st_nonveg},"maincource":{'veg':main_veg,'nonveg':main_nonveg},'ricechapti':{'chapati':chapati,'rice':rice} ,'HeaderName':{'name':'Welcome To Foodcot','para':'Feel fresh to Eat','menu':'Contentail Menu','profile':banner} })


def ThaiMenuList(request):
    if 'CustomerUserid' not in request.session:
        return redirect("LoginCheck")

        
    if request.method=='POST':
        if "Menusubmit" in request.POST:
            item_name=request.POST["itemname"]
            cost=request.POST['cost']
            cart=CustomerItems(userid_id=request.session['CustomerUserid'],ItemName=item_name,itemCost=cost,orginalCost=cost)
            if cart:
                cart.save()
                return redirect("CartCorner")
            
    banner=CusDashboard.objects.filter(blockname="ThaiMenuList")
    if banner.exists:
        banner=banner[0].BannerImage
    else:
        banner=None       
    st_veg=Starter.objects.filter(Check='veg',categories_id='thai')
    st_nonveg=Starter.objects.filter(Check='nonveg',categories_id='thai')
    main_veg=Main_CourceModel.objects.filter(Check='veg',categories_id='thai')
    main_nonveg=Main_CourceModel.objects.filter(Check='nonveg',categories_id='thai')
    chapati=RiceChapati.objects.filter(Check='chapati')
    rice=RiceChapati.objects.filter(Check='rice')
    if rice:
        rice=rice.values()
        rice=[rice[i:i+3] for i in range(0,len(rice),3)]
    if chapati:
        chapati=chapati.values()
        chapati=[chapati[i:i+3] for i in range(0,len(chapati),3)]
    if st_veg:
        st_veg=st_veg.values()
        st_veg=[st_veg[i:i+3] for i in range(0,len(st_veg),3)]
    if st_nonveg:
        st_nonveg=st_nonveg.values()
        st_nonveg=[st_nonveg[i:i+3] for i in range(0,len(st_nonveg),3)]
    if main_veg:
        main_veg=main_veg.values()
        main_veg=[main_veg[i:i+3] for i in range(0,len(main_veg),3)]
    if main_nonveg:
        main_nonveg=main_nonveg.values()
        main_nonveg=[main_nonveg[i:i+3] for i in range(0,len(main_nonveg),3)]
    return render(request,"Customer/Menu_list.html",{'starter':{'veg':st_veg,'nonveg':st_nonveg},"maincource":{'veg':main_veg,'nonveg':main_nonveg},'ricechapti':{'chapati':chapati,'rice':rice} ,'HeaderName':{'name':'Welcome To Foodcot','para':'Feel fresh to Eat','menu':'Thai Menu','profile':banner} })
