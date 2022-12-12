from django.shortcuts import render, redirect
from .models import Topic, Photo
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
# Create your views here.

def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('gallery')

    return render(request, 'photos/login_register.html', {'page': page})


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            if user is not None:
                login(request, user)
                return redirect('gallery')

    context = {'form': form, 'page': page}
    return render(request, 'photos/login_register.html', context)


@login_required(login_url='login')
def gallery(request):
    User = user = request.user
    topic = request.GET.get('topic')
    if topic == None:
        photos = Photo.objects.filter(topic__user=user)
    else:
        photos = Photo.objects.all()

    topics = Topic.objects.filter(user=user)
    context = {'topics': topics, 'photos': photos}
    return render(request, 'photos/gallery.html', context)


@login_required(login_url='login')
def viewPhoto(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    return render(request, 'photos/photo.html', {'photo': photo})


@login_required(login_url='login')
def addPhoto(request):
    user = request.user

    topics = user.topic_set.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['topic'] != 'none':
            topic = Topic.objects.get(id=data['topic'])
        elif data['topic_new'] != '':
            topic, created = Topic.objects.get_or_create(
                user=user,
                name=data['topic_new'])
        else:
            topic = None

        for image in images:
            photo = Photo.objects.create(
                topic=topic,
                description=data['description'],
                image=image,
            )

        return redirect('gallery')

    context = {'topics': topics}
    return render(request, 'photos/add.html', context)

@login_required(login_url='login')
def deletePhoto(request, photo_id):
    photo = Photo.objects.get(id = photo_id)
    photo.delete()
    return redirect('gallery')