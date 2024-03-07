from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import ChiefProfile,ChiefProfileUpdate
from ManagerApp.models import ChiefModel,RecordsManger
from .models import CheifFood
# Create your views here.
def ChiefLogin(request):
    if request.method=='POST':
        if 'Login' in request.POST:
            
            try:
                obj=ChiefModel.objects.get(pk=request.POST['UserId'])
                if obj:
                    if(obj.Password==request.POST['Password']):
                       request.session['ChiefUserId']=request.POST['UserId']
                       return redirect("chiefDashBoard") 
                else:
                    print("Pls Enter Correct Password")
            except Exception as x:
                (print("User id does not exits",x))
    return render(request,'login_form/ChiefLogin.html')

def ChiefLogout(request):
    try:
        request.session.flush()
    except Exception as x:
        print(x)
    return redirect("ChiefLogin")

def chiefDashBoard(request):
    if 'ChiefUserId' not in request.session:
        return redirect("ChiefLogin")
    print(request.session['ChiefUserId'])
    return render(request,"Chief/DashBoardcheif.html")

def chief_Profile(request):
    if 'ChiefUserId' not in request.session:
        return redirect("ChiefLogin")
    obj=ChiefModel.objects.get(pk=request.session['ChiefUserId'])
    form=ChiefProfile(instance=obj)
    return render(request,"Chief/Profile.html",{'form':form,'obj':obj,'update':'v'})

def chief_Update(request,i):
    if 'ChiefUserId' not in request.session:
        return redirect("ChiefLogin")
    obj=ChiefModel.objects.get(pk=i)
    if request.method=='POST':
        if 'Submit' in request.POST:
            form1=ChiefProfileUpdate(request.POST,request.FILES,instance=obj)
            if form1.is_valid():
                form1.save()
                return redirect("chief_Profile")
    form=ChiefProfileUpdate(instance=obj)
    return render(request,"Chief/Profile.html",{'form':form})

def List(request):
    if 'ChiefUserId' not in request.session:
        return redirect("ChiefLogin")

    column=['id','Customer']
    obj=RecordsManger.objects.filter(active='0')
    if request.method=='POST':
        
        if 'Delete'in request.POST:
            o=CheifFood.objects.filter(userid=request.POST['name'])
            o.delete()
            RecordsManger.objects.filter(pk=request.POST['id']).update(active='1')

            print(request.POST)
        elif 'View' in request.POST:
            return redirect("View_List",request.POST['name'])
            print(request.POST)
    if obj:
        obj= obj.values('id','userid_id')
            
    return render(request,"Chief/list.html",{'check':True,'table':{'column':column,'head':'List of Items Order By','data':obj}})


def View_List(request,i):
    if 'ChiefUserId' not in request.session:
        return redirect("ChiefLogin")

    column=['id','Dish Name','Quantity']    
    obj=CheifFood.objects.filter(userid=i)
    if obj:
        obj=obj.values('id','dishname','quantity')
                    
    return render(request,"Chief/list.html",{'check':False,'table':{'column':column,'head':'List of Items Order By %s'%(i),'data':obj}})
