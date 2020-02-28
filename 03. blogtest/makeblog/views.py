from django.shortcuts import render, get_object_or_404, redirect
from .models import Makeblog
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.

def home(request): #{
    blogs = Makeblog.objects
    #블로그 모든 글들을 대상으로
    blog_list = Make.objects.all()
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list, 3)
    #request된 페이지가 뭔지를 알아내고 (request 페이지를 변수에 담아내고)
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다.
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs' : blogs})
#}

def detail(request, blog_id): #{
    details = get_object_or_404(Makeblog, pk=blog_id)
    return render(request, 'detail.html', {'details': details})
#}

def new(request): #{
    return render(request, 'new.html')
#}

def create(request): #{
    blog = Makeblog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_data = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))
#}
