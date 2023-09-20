from django.shortcuts import render, get_object_or_404
from .models import News


def home(request):
    return render(request, 'news/index.html')


def display_news(request):
    news = News.published.all()
    return render(request,'news/posts/list.html', {'news': news,})


def display_detail_new(request,year,month,day,new):
    new = get_object_or_404(News,
                            status=News.Status.PUBLISHED,
                            slug=new,
                            publish__year=year,
                            publish__month=month,
                            publish__day=day)

    return render(request,'news/posts/detail.html', {'new': new})


def display_club_information(request):
    return render(request, 'news/about_club.html')






