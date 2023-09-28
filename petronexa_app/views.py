from django.shortcuts import *
from django.http import *
from petronexa_app.models import *
from petronexa_app.forms import  *
import json
from django.views.decorators.csrf import csrf_exempt
from random import *

# Create your views here.

def homepage (request):
    post = Post.objects.all()
    return render(request, "frontend/index.html", {'post':post})

def contact(request):
    return render(request, "frontend/contact.html")

def blog(request, det_id):
    details = get_object_or_404(Post,id=det_id)
    comments = Comment.objects.filter(post=det_id).order_by('-created_date')
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)  
            comment.details = details
            comment.author = request.user
            comment.save()
            return redirect('frontend:blog', det_id=blog.det_id)
            details = {'form': form, 'most_recent': most_recent,}
    else:
        form = CommentForm()
        
    context = {
        'form' : form,
        'details':details,
        'comments':comments,
    }
    
    return render(request, "frontend/blog-details.html", context)

def fuelfinder(request):
    # Retrieve all fuel stations (you can modify this query based on your needs)
    fuel_stations = Post.objects.all()

    # Process user input for filtering
    search_query = request.GET.get('search', '')
    rating = request.GET.get('rating', 0)
    price = request.GET.get('price', '')
    customer_service = request.GET.get('customer_service', 0)
    random = sample(list(fuel_stations), 3)

    if search_query:
        # Filter by station name (case-insensitive)
        fuel_stations = fuel_stations.filter(title__icontains=search_query)

    if rating:
        # Filter by rating
        fuel_stations = fuel_stations.filter(rating=rating)

    if price:
        # Filter by price (you may need to adjust this based on your model field)
        fuel_stations = fuel_stations.filter(price=price)

    if customer_service:
        # Filter by customer service
        fuel_stations = fuel_stations.filter(customer_service=customer_service)

    return render(request, "frontend/fuelfinder.html", {'random': random})


@csrf_exempt
def addstation(request):
    if request.method == 'POST':
        form = GasStationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Set the author to the currently logged-in user
            post.save()
            return JsonResponse({'message': 'Gas station added successfully'})
        else:
            errors = json.loads(form.errors.as_json())
            return JsonResponse({'error': 'Invalid form submission', 'details': errors}, status=400)
    else:
        # Handle GET requests by rendering the form
        form = GasStationForm()  # Create a new form instance
        return render(request, 'frontend/addstation.html', {'form': form})
def login(request):
    return render(request, "frontend/login.html")

def signup(request):
    return render(request, "frontend/signup.html")