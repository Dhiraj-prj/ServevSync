from urllib import request
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CustomUser, HouseworkerProfile, Service
from .models import HouseworkerProfile





def home(request):
    return render(request, 'Home/home.html')


def login_page(request):
    return render(request, 'Home/login.html')


def signup(request):
    return render(request, 'home/signup.html')



def about(request):
    return render(request, 'home/about.html')


def contact(request):
    return render(request, 'home/contact.html')


def search(request):
    query = request.GET.get('q')
    results = []  # Replace this with your actual search logic

    return render(request, 'home/search_results.html', {'query': query, 'results': results})


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            return redirect('role_redirect')  # Redirect to role_redirect after login
        else:
            return render(request, 'Home/login.html', {'error': 'Invalid credentials'})
    return render(request, 'Home/login.html')


def worker_login(request):
        return render(request, 'Home/home.html')




def hirer_login(request):
    if request.method == "POST":
        # Handle hirer login logic here (e.g., authentication)
     return render(request, 'Home/home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        selected_role = request.POST.get('role')  # Get the selected role from the form

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Check the user's role from their profile
            try:
                profile = UserProfile.objects.get(user=user)

                # Check if the role matches the selected role
                if profile.role == selected_role:
                    login(request, user)

                    # Redirect to the home page after successful login and role match
                    return redirect('home')  # Make sure 'home' matches the URL name in urls.py

                else:
                    # Role mismatch error
                    error_message = "Role mismatch. Please select the correct role."
                    return render(request, 'home/login.html', {'error': error_message})
            except UserProfile.DoesNotExist:
                error_message = "Profile not found for this user."
                return render(request, 'home/login.html', {'error': error_message})

        else:
            # Invalid credentials error
            error_message = "Invalid username or password."
            return render(request, 'home/login.html', {'error': error_message})

    # GET request to render the login page
    return render(request, 'home/login.html')



def service_selection_view(request):
    services = Service.objects.all()  # Fetch all services
    return render(request, 'template.html', {'services': services})





def services(request):
    services = Service.objects.all()
    context = {
        'services': services,
        'service_label': 'Our Services' #you can change this as you wish
    }
    return render(request, 'Home/services.html', context)





@login_required
def edit_profile(request):
    if request.user.role != 'houseworker':
        raise PermissionDenied("Only houseworkers can access this page.")
# Existing profile creation logic here...


@login_required
def role_redirect(request):
        if request.user.role == 'houseworker':
            return redirect('profile_creation')
        elif request.user.role == 'hirer':
            return redirect('home')
        else:
            return redirect('login')

@login_required
def profile_creation(request):
        if request.method == 'POST':
            # Save Houseworker profile
            name = request.POST['name']
            service = request.POST['service']
            contact = request.POST['contact']
            bio = request.POST['bio']
            HouseworkerProfile.objects.create(
                user=request.user,
                name=name,
                service=service,
                contact=contact,
                bio=bio,
            )
            return redirect('houseworker_profile', user_id=request.user.id)
        return render(request, 'home/profile_creation.html')




def home(request):
        return render(request, 'home/home.html')





@login_required
def role_redirect(request):
    user = request.user
    if user.role == 'houseworker':  # Check lowercase role
        # Redirect to profile creation if no profile exists
        if not HouseworkerProfile.objects.filter(user=user).exists():
            return redirect('profile_creation')  # Redirect to profile creation
        return redirect('houseworker_profile')  # Redirect to the worker's profile
    elif user.role == 'houseowner':  # Check lowercase role
        return redirect('home')
    else:
        return redirect('login')


from .models import HouseworkerProfile

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import HouseworkerProfile
from .forms import WorkerProfileForm  # Assuming you have a form










from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import HouseworkerProfile  # Change WorkerProfile to HouseworkerProfile
from .forms import WorkerProfileForm  # Import form


def services_page(request):
    services = Service.objects.all()
    return render(request, "home/services.html", {"services": services})


def create_profile(request):
    if request.method == "POST":
        form = WorkerProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("services_page")  # Redirect to services page after profile creation
    else:
        form = WorkerProfileForm()

    services = Service.objects.all()
    return render(request, "home/profile_creation.html", {"form": form, "services": services})


def get_workers(request, service_id):
    workers = HouseworkerProfile.objects.filter(service_id=service_id).values("name", "contact", "bio")
    return JsonResponse(list(workers), safe=False)






from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.http import JsonResponse
from .models import HouseworkerProfile

def houseworker_profile_list(request):
    profiles = HouseworkerProfile.objects.all()
    profiles_json = serializers.serialize('json', profiles)
    return render(request, 'home/houseworker_profile_list.html', {'profiles_json': profiles_json})

def houseworker_profile_detail(request, profile_id):
    profile = get_object_or_404(HouseworkerProfile, pk=profile_id)
    profile_data = {
        'name': profile.name,
        'service': profile.get_service_display(),  # Get the display value for the choice field
        'contact': profile.contact,
        'bio': profile.bio,
        'rating': profile.rating,
        'photo': profile.photo.url if profile.photo else None,  # Get the URL of the image
    }
    return JsonResponse(profile_data)

from django.shortcuts import render, redirect
from .models import UniqueProfileModel, UniqueServiceModel

def unique_profile_creation_view(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        selected_service_id = request.POST.get('selected_service')
        contact_info = request.POST.get('contact_info')
        biography = request.POST.get('biography')

        # Fetch the selected service
        selected_service = UniqueServiceModel.objects.get(id=selected_service_id)

        # Save the profile data
        UniqueProfileModel.objects.create(
            full_name=full_name,
            selected_service=selected_service,
            contact_info=contact_info,
            biography=biography
        )

        return render(request, 'home/home.html')

    all_services = UniqueServiceModel.objects.all()  # Fetch all services for dropdown
    return render(request, 'home/profile_creation.html', {'all_services': all_services})





