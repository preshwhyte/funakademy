from django.shortcuts import render,redirect, get_object_or_404
from .models import Slider,Gallery,News,Staff
from .form import SlideForm, GalleryForm, NewsForm, StaffForm

# Create your views here.
def home(request):
    slider=Slider.objects.all()
    gallery=Gallery.objects.all()
    staff=Staff.objects.all()
    news=News.objects.all()
    return render(request, 'common/home.html',{'slider':slider, 'gallery':gallery, 'staff':staff, 'news':news} )

def about(request):
    return render(request, 'common/about.html')

def gallery(request):
    gallery=Gallery.objects.all()
    return render(request, 'common/gallery.html',{'gallery':gallery})

def addgallery(request):
    gallery=Gallery.objects.all()
    if request.method=="POST":
        galForm=GalleryForm(request.POST, request.FILES)
        if galForm.is_valid():
            galForm.save()
            return redirect('gallery')
        
    else:
        galForm=GalleryForm()
    return render(request, 'common/addgal.html',{'galform':galForm})

def deletegal(request, id):
    gallery=Gallery.objects.get(id=id)
    gallery.delete()
    return redirect('home')



def news(request):
    return render(request, 'common/news.html')

def contact(request):
    slider=Slider.objects.all()
    return render(request, 'common/contact.html', {'slider':slider})

def updateslide(request, slideid):
    slide=Slider.objects.get(pk=slideid)

    slideform=SlideForm(request.POST or None, request.FILES or None, instance=slide)
    if slideform.is_valid():
        slideform.save()
        return redirect('home')
    else:
        slideform=SlideForm()  
    return render(request,'common/slideupdate.html', {'slideform':slideform, 'slide':slide})

def news(request):
    news=News.objects.all()
    return render(request,'common/news.html', {'news':news})

def addnews(request):
    news=News.objects.all()
    if request.method=="POST":
        newsform=NewsForm(request.POST, request.FILES)
        if newsform.is_valid():
            newsform.save()
            return redirect('news')
        
    else:
        newsform=NewsForm()
    return render(request, 'common/addnews.html',{'newsform':newsform})

def updatenews(request, newsid):
    news=News.objects.get(pk=newsid)

    newsform=NewsForm(request.POST or None, request.FILES or None, instance=news)
    if newsform.is_valid():
        newsform.save()
        return redirect('home')

    return render(request,'common/newsupdate.html', {'newsform':newsform, 'news':news})

def staff(request):
    staff=Staff.objects.all()
    return render(request, 'common/staff.html', {'staff':staff} )

def addstaff(request):
    staff=Staff.objects.all()
    if request.method=="POST":
        staffForm=StaffForm(request.POST, request.FILES)
        if staffForm.is_valid():
            staffForm.save()
            return redirect('home')
        
    else:
        staffForm=StaffForm()
    return render(request, 'common/addstaff.html',{'staffform':StaffForm})


    


    



