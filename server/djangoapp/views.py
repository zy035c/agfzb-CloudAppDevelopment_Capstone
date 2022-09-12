from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


# Create an `about` view to render a static about page
def about(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/about.html', context)

# Create a `contact` view to return a static contact page
def contact(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/contact.html', context)

# Create a `login_request` view to handle sign in request
def login_request(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['psw']

        user = authenticate(username=username, password=password)
        if user is not None:
            # if valid
            login(request, user)
            return redirect('djangoapp/index.html')
        else:
            return render(request, 'djangoapp/index.html', context)
    else:
        return render(request, 'djangoapp/index.html', context)


# Create a `logout_request` view to handle sign out request
def logout_request(request):
    print("Log out the user `{}`".format(request.user.username))
    logout(user)
    return redirect('djangoapp/index.html')


# Create a `registration_request` view to handle sign up request
def registration_request(request):
    context = {}
    if request.method == 'GET':
        print("here!!!")
        return render(request, 'djangoapp/registration.html', context)
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pwd']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        user_exist = False
        try:
            User.objects.get(username=username)
            user_exist = True
        except:
            logger.debug("{} is new user".format(request.username))

        if not user_exist:
            user = User.objects.create_user(
                username=username, 
                password=password, 
                last_name=lastname, 
                first_name=firstname
            )
            # log in the user
            login(request, user)
            return redirect('djangoapp/index.html')
        else:
            return render(request, 'djangoapp/registration.html', context)

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    if request.method == "GET":
        url = "https://eu-gb.functions.appdomain.cloud/api/v1/web/coursera-1c4_capstone-eu/dealership-package/get-dealership"
        # Get dealers from the URL
        dealerships = get_dealers_from_cf(url)
        # Concat all dealer's short name
        dealer_names = ' '.join([dealer.short_name for dealer in dealerships])
        # Return a list of dealer short name
        return HttpResponse(dealer_names)


# Create a `get_dealer_details` view to render the reviews of a dealer
def get_dealer_details(request, dealer_id):
    if request.METHOD == "GET":
        url = "https://eu-gb.functions.appdomain.cloud/api/v1/web/coursera-1c4_capstone-eu/dealership-package/get-review"
        reviews = get_dealer_reviews_from_cf(url, dealer_id)
        return HttpResponse(reviews) # also sentiment?

# Create a `add_review` view to submit a review
def add_review(request, dealer_id):
# ...
    context = {}
    url = "https://eu-gb.functions.appdomain.cloud/api/v1/web/coursera-1c4_capstone-eu/dealership-package/post-review"
    dealer = get_dealer_by_if_from_cf(dealer_
                                     )
    if request.METHOD == "POST":
        
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)
    
def add_review(request, dealer_id):    
    context = {}    
    dealer_url = "https://1be60b93.us-south.apigw.appdomain.cloud/api/dealership"   
    
    if !request.user.is_authenticated:
        redirect('djangoapp/registration.html')
    else:
        if (request.METHOD == "POST"):
            review = dict()
            review["time"] = datetime.utcnow().isoformat()
            review["dealership"] = dealer_id
            review["review"] = request.text
            json_payloar = dict()
            json_payloar = ["review"] = review
            post_request()
            
    
    dealer = get_dealer_by_id_from_cf(dealer_url, id=id)    
    context["dealer"] = dealer    
    if request.method == 'GET':        
        cars = CarModel.objects.all()        
        context["cars"] = cars        
        return render(request, 'djangoapp/add_review.html', context)   
    elif request.method == 'POST':        
        if request.user.is_authenticated:            
            username = request.user.username            
            print(request.POST)            
            payload = dict()            
            car_id = request.POST["car"]            
            car = CarModel.objects.get(pk=car_id)            
            payload["time"] = datetime.utcnow().isoformat()            
            payload["name"] = username            
            payload["dealership"] = id            
            payload["id"] = id            
            payload["review"] = request.POST["review"]            
            payload["purchase"] = False            
            if "purchasecheck" in request.POST:                
                if request.POST["purchasecheck"] == 'on':                    
                    payload["purchase"] = True            
                    payload["purchase_date"] = request.POST["purchase_date"]            
                    payload["car_make"] = car.make.name            
                    payload["car_model"] = car.name            
                    payload["car_year"] = int(car.year.strftime("%Y"))            
                    new_payload = {}            
                    new_payload["review"] = payload            
                    review_post_url = "https://1be60b93.us-south.apigw.appdomain.cloud/api/postreview"            
                    post_request(review_post_url, new_payload, id=id)        
                    return redirect("djangoapp:dealer_details", id=id)  
                    

