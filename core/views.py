from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import PostForm
from .models import Post

# Create your views here.


class MainFormView(FormView):
    template_name = 'main.html'
    extra_context = {}

    def get(self, request):
        posts = Post.objects.all().order_by('-date')[:10]
        first = True
        self.extra_context['post'] = posts
        self.extra_context['first'] = first
        return render(request, self.template_name, self.extra_context)


class AddFormView(FormView):
    form_class = PostForm
    template_name = 'add.html'
    success_url = '/'
    extra_context = {'form': form_class}

    def get(self, request):
        return render(request, self.template_name, self.extra_context)

    def form_valid(self, form):
        form.save()
        return super(AddFormView, self).form_valid(form)


class ArticleFormView(FormView):
    template_name = 'post.html'
    extra_context = {}

    def get(self, request, article):
        post = Post.objects.get(id=article)
        self.extra_context['article'] = post
        return render(request, self.template_name, self.extra_context)
