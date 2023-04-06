from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from gallery.models import Image, Gallery
from gallery.decorators import unauthenticated_user
from gallery.forms import LoginForm, CreateUserForm, ImageForm




def get_gallery(request):
    if request.user.is_authenticated:
        try:
            return Gallery.objects.get(user=request.user, is_active=True)
        except Gallery.DoesNotExist:
            return None
        except:
            return None
    return None




def home_view(request):
    form = ImageForm
    context = {'form': form}
    
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ImageForm(request.POST, request.FILES) or None
            
            if form.is_valid():
                images = request.FILES.getlist('images')
                for img in images:
                    Image.objects.create(gallery=get_gallery(request), image=img, is_deleted=False)
                return redirect(request.META.get('HTTP_REFERER'))
        
        private_images = Image.objects.filter(is_open_source=False, is_deleted=False, gallery=get_gallery(request))
        context.update({'private_images': private_images})
        
    public_images = Image.objects.filter(is_open_source=True, is_deleted=False)
    context.update({'public_images': public_images})
    
    template_name = "home.html"
    return render(request, template_name, context)






@login_required(login_url='login')
def user_gallery_view(request):
    user_pictures = []
    form = ImageForm
    
    try:    
        user_gallery = Gallery.objects.get(user=request.user, is_active=True)
    except Gallery.DoesNotExist:
        user_gallery = None
        messages.error(request, "Sorry, that gallery does not exist")
        return redirect('home')
    
    if user_gallery and user_gallery is not None:
        user_pictures = user_gallery.images()
        
        if request.method == "POST":
            form = ImageForm(request.POST, request.FILES) or None
            
            if form.is_valid():
                images = request.FILES.getlist('images')
                for img in images:
                    Image.objects.create(gallery=get_gallery(request), image=img, is_deleted=False)
                return redirect(request.META.get('HTTP_REFERER'))
    
    
    
    paginator = Paginator(user_pictures, 500)
    page = request.GET.get("page")
    user_pictures_obj = paginator.get_page(page)

    try:
        user_pictures = paginator.page(page)
    except PageNotAnInteger:
        user_pictures = paginator.page(1)
    except EmptyPage:
        user_pictures = paginator.page(paginator.num_pages)
    
    
    context = {
        'form': form,
        'user_pictures': user_pictures_obj
    }
    
    template_name = "user_gallery.html"
    return render(request, template_name, context)







###################################################### AUTH VIEWS ######################################################
@unauthenticated_user
def register_view(request):
    form = CreateUserForm

    if request.method == 'POST':
        form = CreateUserForm(request.POST or None)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            form.save()

            # Successfull registration, log in now
            try:
                user = authenticate(request, username=username, password=password)
                if user is not None and user.is_active:
                    login(request, user)
                    messages.success(request, f"Thank you to join us, {request.user.username}")
                    return redirect('user-gallery')
            except:  # if login failed, redirect to login page for self logging in.
                return redirect('login')

        else:
            for error in form.errors:
                messages.warning(request, error)
            return redirect('register')
    
    else:
        form = CreateUserForm()

    context = {
        'form': form,
    }

    template_name = 'register.html'
    return render(request, template_name, context)







@unauthenticated_user
def login_view(request):
    form = LoginForm
    if request.method == 'POST':
        form = LoginForm(request.POST) or None
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
        
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                messages.success(request, f"Welcome, {request.user.username}")

                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                elif not 'next' in request.POST:
                    return redirect('user-gallery')
                else:
                    return redirect('home')
            else: #user is None or inactive
                messages.warning(request, "Oops! Wrong password or username!")
        
        else: #form is not valid
            for error in form.errors:
                messages.warning(request, error)
            return redirect('register')
    
    else: #method is not POST
        form = LoginForm()
    
    context = {
        'form': form,
    }
    
    template_name = 'login.html'
    return render(request, template_name, context)





@login_required(login_url='login')
def logout_view(request):
    logout(request)
    messages.success(request, "You successfully logged out")
    return redirect(request.META.get('HTTP_REFERER'))

