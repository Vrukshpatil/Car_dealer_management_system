from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import NewUser,CarDetails,CarOrders,Contacts
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.http import JsonResponse
from django.http import HttpResponse
# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_no= request.POST.get('phone_no')
        email = request.POST.get('email')
        msg = request.POST.get('msg')
       
        user = Contacts.objects.create(Name=name,
            email=email,phone_no=phone_no,
            msg=msg)
    return render(request,'index.html')


def user_dashboard(request):
   
    data=CarDetails.objects.all()
    username=request.user.username
    
    context={'data':data,'username':username}
    return render(request,'user_dashboard.html',context)

def purchase(request):
    if request.method == 'POST':
        # Get form data
        car_id = request.POST.get('carId')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        # Create a new CarOrders object and save it to the database
        CarOrders.objects.create(
            car_id_id=car_id,
            Name=name,
            email=email,
            phone_no=phone,
            address=address
        )

        # Return a success message
        return JsonResponse({'message': 'Form submitted successfully'})
    else:
        # If the request method is not POST, handle accordingly
        return JsonResponse({'error': 'Invalid request method'})

def cars(request):
    return render(request,'cars.html')

def single_car_details(request,id):
    print(id)
    return render(request,'single_car_details.html')

def admin_logout(request):
    logout(request)
    # Redirect to a specific page after logout (optional)
    return redirect('admin_login')

def user_logout(request):
    logout(request)
    # Redirect to a specific page after logout (optional)
    return redirect('index')

def add_car_details(request):
    username=request.user.username
    if request.method == 'POST':
        modal = request.POST.get('model_name')
        year = request.POST.get('year')
        price = request.POST.get('price')
        engine = request.POST.get('engine')
        mileage = request.POST.get('mileage')
        car_img1=request.FILES.get('car_img')
        car_img2=request.FILES.get('car_img2')
        car_img3=request.FILES.get('car_img3')
        car_details=CarDetails.objects.create(modal=modal,price=price,Mileage=mileage,year=year,
                                          Engine=engine,car_img1=car_img1,car_img2=car_img2,car_img3=car_img3)
    context={'username':username}
    return render(request,'add_car_details.html',context)

def admin_dashboard(request):
    username=request.user.username
    data=CarOrders.objects.all().select_related('car_id')
    for x in data:
        print(x.car_id.modal)
    context={'data':data,'username':username}
    return render(request,'admin_dashboard.html',context)

def admin_login(request):
    print("hiiiii")
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            print(request.user)
            return redirect('/admin_dashboard')
        else:
            messages.error(request,'Wrong Credentials')
            return redirect('/admin_login')
    return render(request,'admin_login.html')

def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        phone_no = request.POST.get('phone')
        password = request.POST.get('password')
        email = request.POST.get('email')
        address = request.POST.get('address')
        passw = make_password(password)
        user = NewUser.objects.create(
            username=username,
            password=passw,
            email=email,
            phone_no=phone_no,
            address=address
        )
        # Return JSON response indicating successful registration
        return JsonResponse({'success': True})
    return render(request, "registration.html")




def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('user_dashboard')  # Replace 'user_dashboard' with the name of your success URL
        else:
            # Return an 'invalid login' error message.
            error_message = "Invalid username or password."
            messages.error(request, error_message)
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

    
def contact_details(request):
    username=request.user.username
    data=Contacts.objects.all()
    context={'data':data,'username':username}
    return render(request, 'contact_details.html',context)

def available_cars(request):
    data=CarDetails.objects.all()
    context={'data':data}
    return render(request,'available_cars.html',context)