

from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required

# Create your views here.
#from django.http import HttpResponse
from .models import *
#from .forms import *


'''def test(request, *args, **kwargs):
    return HttpResponse('OK')
'''

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
 #   print(request.user)
    return render(request, 'home.html', {
        'questions': page.object_list,
 #       'user':request.user,
        'page': page,
        'paginator': paginator,
    })

def popular(request):
    qs=Question.objects.popular()
    qs = qs.order_by('-added_at')
    page, paginator = paginate(request,qs)
    paginator.baseurl = reverse('popular')+'?page='
    return render(request, 'popular.html', {
        'questions':page.object_list,
 #       'user': request.user,
        'page':page,
        'paginator':paginator,
    })

def detail(request, pk=1):
    question = get_object_or_404(Question, id=pk)
    answers = question.answer_set.all()
#    form = AnswerForm(initial={'question': str(pk)})
    return render(request, 'detail.html',{
        'Question':question,
 #       'user': request.user,
        'list_answer':answers,
 #       'form':form,
    })


# def question_ask(request):
#     if request.method == 'POST':
#         form = AskForm(request.POST)
#         if form.is_valid():
#             form._user = request.user
#             ask=form.save()
#             return HttpResponseRedirect(ask.get_url())
#     else:
#         form = AskForm()
#     return render(request, 'ask.html',{
#         'form':form,
#         'user': request.user,
#     })

# def question_answer(request):
#     if request.method == 'POST':
#         form = AnswerForm(request.POST)
#         if form.is_valid():
#             form._user=request.user
#             print(request.user)
#             answer=form.save()
#             url = reverse('question_detail', args=[answer.question.id])
#             return  HttpResponseRedirect(url)
#     return HttpResponseRedirect('/')

# def signup_user(request):
#     if request.method=='POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             print("========================", )
#             if user is not None:
#                 login(request, user)
#                 return HttpResponseRedirect('/')
#     form = SignupForm()
#     return render(request, 'signup.html', {'form': form, 'user':request.user,})
#
#
# def login_user(request):
#     if request.method=='POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             user=form.save()
#             print(user)
#         if user is not None:
#             login(request, user)
#             print(user)
#             return HttpResponseRedirect('/')
#     form = LoginForm()
#     return  render(request, 'login.html', {'form': form, 'user':request.user,})
#
#
# def user_logout(request):
#     print(request.user)
#     logout(request)
#     return redirect('login')