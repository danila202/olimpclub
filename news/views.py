from django.shortcuts import render, get_object_or_404
from .models import News
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    return render(request, 'news/index.html')


def display_news(request):
    news_list = News.published.all()
    paginator = Paginator(news_list, 3)

    page_number = request.GET.get('page', 1)
    try:
        news_page = paginator.page(page_number)
    except EmptyPage:
        news_page = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        news_page = paginator.page(1)

    return render(request, 'news/posts/list.html', {'news_page': news_page})


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






