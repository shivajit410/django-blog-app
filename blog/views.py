from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView 
from .models import Article
from .forms import CreateArticleForm

# Create your views here.

def home(request):
    # return HttpResponse('Home Page')
    return render(request, 'blog/home.html')


def about(request):
    # return HttpResponse('About Page')
    return render(request, 'blog/about.html')


class ArticlesList(ListView):
    queryset = Article.objects.all().order_by('date')
    context_object_name = 'articles'
    template_name = 'blog/articles.html'

# def article_details(request, slug):
#     return HttpResponse('Article detailed view '+ slug)
    # article = Article.objects.get(slug=slug)

class ArticleDetail(DetailView):
    context_object_name = 'article'
    template_name = 'blog/article_detail.html'

    def get_object(self):
        slug = self.kwargs['slug']
        query_set = Article.objects.get(slug=slug)
        return query_set

@login_required(login_url='/accounts/login/')
def article_create(request):
    if request.method == 'POST':
        form = CreateArticleForm(request.POST, request.FILES)
        if form.is_valid():
            # TODO Save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blog:article')
    else:
        form = CreateArticleForm()
    context = {'form':form}
    return render(request, 'blog/article_create.html', context)