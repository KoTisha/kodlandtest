from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import PostForm

# Create your views here.


class MainFormView(FormView):
    template_name = 'main.html'

    def get(self, request):
        return render(request, self.template_name)


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

    def get(self, request):
        return render(request, self.template_name)
