from django.shortcuts import *
from django.http import *
from petronexa_app.models import *
from petronexa_app.forms import  *
import json
from django.views.decorators.csrf import csrf_exempt
from random import *
from django.core.mail import *
from django.contrib.auth import *
from django.urls import *
from django.contrib.auth.decorators import *
from django.contrib.admin.views.decorators import *
from django.core.paginator import Paginator
from decimal import Decimal
from random import sample  


# Create your views here.

def homepage(request):
    all_posts = Post.objects.all().order_by('-published_date')
    posts_per_page = 6 
    paginator = Paginator(all_posts, posts_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        'page': page,
    }

    return render(request, 'frontend/index.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = f"{email} sent you a message: {form.cleaned_data['message']}"

            # Send email
            send_mail(
                subject,
                message,
                email,
                ['dansu.jw@gmail.com'],
                fail_silently=False,
            )

            message_obj = ContactMessage(name=name, email=email, subject=subject, message=message)
            message_obj.save()

            return redirect('petronexa_app:homepage')  # Redirect to a thank you page or homepage

    else:
        form = ContactForm()

    return render(request, 'frontend/contact.html', {'form': form})

def blog(request, det_id):
    details = get_object_or_404(Post, id=det_id)
    comments = Comment.objects.filter(post=details).order_by('-created_date')  # Filter comments by the current post

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = details  # Assign the comment to the current post
            comment.author = request.user
            comment.save()
            return redirect('frontend:blog', det_id=det_id)  # Use det_id variable here
    else:
        form = CommentForm()

    context = {
        'form': form,
        'details': details,
        'comments': comments,
    }

    return render(request, "frontend/blog-details.html", context)



@login_required
def fuelfinder(request):
    # Retrieve all fuel stations
    fuel_stations = Post.objects.all()[:3]

    # Process user input for filtering
    search_query = request.GET.get('q', '')  # Updated to 'q' for name search
    rating_range = request.GET.get('rating', '')  # Use a string to specify the rating range
    price = request.GET.get('price', '')
    customer_service = request.GET.get('customer-service', '')  # Updated to 'customer-service'

    # Apply filters only if search query is empty
    if not search_query:
        random_stations = sample(list(fuel_stations), min(3, fuel_stations.count()))
    else:
        random_stations = []  # If search query is not empty, don't show random stations

    if search_query:
        # Filter by station name (case-insensitive)
        fuel_stations = fuel_stations.filter(title__icontains=search_query)

    if rating_range:
        # Split the rating range into minimum and maximum values
        min_rating, max_rating = rating_range.split('-')
        min_rating = Decimal(min_rating)
        max_rating = Decimal(max_rating)

        # Filter by rating range
        fuel_stations = fuel_stations.filter(rating__gte=min_rating, rating__lt=max_rating + Decimal('0.1'))

    if price:
        # Filter by price (you may need to adjust this based on your model field)
        fuel_stations = fuel_stations.filter(price=price)

    if customer_service:
        # Filter by customer service
        fuel_stations = fuel_stations.filter(customer_service=customer_service)

    if request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        data = [{'title': station.title, 'rating': str(station.rating), 'customer_service': station.customer_service, 'price': str(station.price)} for station in fuel_stations]
        return JsonResponse({'fuel_stations': data})

    user_is_not_logged_in = not request.user.is_authenticated
    if user_is_not_logged_in:
        return redirect('petronexa_app:login')
    else:
        return render(request, "frontend/fuelfinder.html", {'filtered_posts': fuel_stations})



@login_required
def addstation(request):
    user_is_not_logged_in = not request.user.is_authenticated
    
    if user_is_not_logged_in:
        return redirect('petronexa_app:login')

    if request.method == 'POST':
        form = GasStationForm(request.POST, request.FILES)
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

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('petronexa_app:homepage')
    else:
        form = LoginForm()
    
    return render(request, 'frontend/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect(reverse('petronexa_app:homepage'))

@staff_member_required
def admin(request):
    if request.user.is_staff:
        return redirect('admin:index')
    else:
        return redirect('petronexa_app:homepage')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('petronexa_app:login')  
    else:
        form = SignUpForm()
    return render(request, 'frontend/signup.html', {'form': form})