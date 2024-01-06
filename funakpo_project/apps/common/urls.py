from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('news/', views.news, name='news'),
    path('contact/',views.contact, name='contact'),
    path('update/<slideid>', views.updateslide, name='update'),
    path('addgallery/',views.addgallery, name='addgal'),
    path('addstaff/', views.addstaff, name='addstaff'),
    path('addnews/',views.addnews, name='addnews'),
    path('delete/<id>',views.deletegal, name='deletepic'),
    path('news/<newsid>', views.updatenews, name='newsupdate'),
    path('staff/', views.staff, name='staff')
]