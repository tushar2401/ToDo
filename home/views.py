from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
from home.models import Task,UserDetails
#from home.forms import AddTaskForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    users = User.objects.all()
    tasks = Task.objects.filter(assignto = request.user)
        #return render(request,"tasks.html",{'tasks':tasks,'form':form})
    return render(request,"home.html",{'tasks':tasks,'users':users})

    return render(request,'home.html')

def signup(request):
    if request.method == 'POST':
        success=1
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST.get('email')
        user_type = request.POST['ut']
        cont = request.POST['contact_no']

        if username=="":
            success=0
            messages.error(request,"Username required")
        elif cont=="":
            success=0
            messages.error(request,"Contact no required")
        elif cont.isalpha():
            success=0
            messages.error(request,"Contact No Must be Numeric")
        elif password=="" :
            success=0
            messages.error(request,"Password required")
        elif len(password)<4:
            success=0
            messages.error(request,"Password must be atleast 4 character long")
        if success==0:
            return render(request,'signup.html')
        try:
            user = User.objects.get(username=username)
            success=0
            messages.error(request,"Username alredy exists")
            return render(request,'signup.html')
        except :
            pass
        myuser = User.objects.create_user(username=username,email=email,password=password)
        if user_type == "admin":
            myuser.is_staff=True
        myuser.save()
        det = UserDetails(user=myuser, contact_no=cont)
        det.save()

        messages.success(request,"registered successfully")
        return redirect("user_login")

        #User(username=username,password=password,email=email).save()
        #msg = "Registred successfully"

        myuser = User.objects.create_user(username=username,email=email,password=password)
        #myuser.first_name = fname ---we can add fields
        myuser.save()
        messages.success(request,"registered successfully")
        return redirect("user_login")
    return render(request,'signup.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user) 
            name= user.username
            messages.success(request,"Logged in successfully")
            return redirect("tasks") 
        else:
            if username=="":
                messages.error(request,"Please enter username to login")
            elif password=="":
                messages.error(request,"Please enter password to login")
            else:
                messages.error(request,"Bad credentials....Incorrect username or password!")
            return redirect("user_login")


    return render(request,'login.html')   

def user_logout(request):
    logout(request)
    return redirect('home')

def tasks(request):
    if request.method=='POST':
        title = request.POST['title']
        name = "Bhava"
        desc = request.POST['desc']
        user = User.objects.get(username=request.user.username)
        if user.is_staff == True:
            to = request.POST['ass_to']
        else:
            to = user.username
        task = Task(taskTitle=title,taskDesc=desc,user=user,assignto=to)
        task.save()
        return redirect("tasks")


        '''
        #using django forms
        form = AddTaskForm(request.POST)  
        if form.is_valid():
            data = form.save(commit=False)
            data.user = User.objects.get(username=request.user.username)
            data.save()
            return redirect("tasks")
        '''
    else:
        #form = AddTaskForm()
        users = User.objects.all()
        tasks = Task.objects.filter(assignto = request.user)
        a_tasks = Task.objects.filter(user = request.user)
        #return render(request,"tasks.html",{'tasks':tasks,'form':form})
        return render(request,"tasks.html",{'tasks':tasks,'a_tasks':a_tasks,'users':users})

def delete(request):
    del_task_title= request.GET['title']
    Task.objects.filter(taskTitle=del_task_title).delete()
    messages.success(request,"Task deleted successfully")
    return HttpResponseRedirect("tasks")

def update(request):
    return HttpResponseRedirect("tasks")

def addtask(request):
    if request.method=='POST':
        ss=1
        title = request.POST['title']
        desc = request.POST['desc']
        user = User.objects.get(username=request.user.username)
        if user.is_staff == True:
            to = request.POST['ass_to']
        else:
            to = user.username
        if title=="":
            messages.error(request,"Task Title is Required")
            return redirect("addtask")
        else:
            if desc=="":
                desc = "No description for this task"
                messages.error(request,"We have added default desc to your newly added task")
            else:
                messages.success(request,"Task Created successfully")
        task = Task(taskTitle=title,taskDesc=desc,user=user,assignto=to)
        task.save()
        return redirect("tasks")
    users = User.objects.all()
    return render(request,'addtask.html',{'users':users})