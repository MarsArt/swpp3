

from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse

# Create your views here.
#from django.http import HttpResponse
from .models import *


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit =10

    try:
        page = int(request.GET.get('page',1))
    except ValueError:
        raise Http404

    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page, paginator

def home(request, *args, **kwargs):
    qs = Question.objects.all()
    qs = qs.order_by('-added_at')
    page, paginator= paginate(request,qs)
    paginator.baseurl = reverse('home')+'?page='

    return render(request, 'home.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
    })

def popular(request):
    qs=Question.objects.popular()
    page, paginator = paginate(request,qs)
    paginator.baseurl = reverse('popular')+'?page='

    return render(request, 'popular.html', {
        'questions':page.object_list,
        'page':page,
        'paginator':paginator,
    })

def detail(request, pk=1):
    question = get_object_or_404(Question, id=pk)
    answers = question.answer_set.all()
    return render(request, 'detail.html',{
        'Question':question,
        'list_answer':answers,
    })
