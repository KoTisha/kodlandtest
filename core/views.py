from django.shortcuts import render
from django.views.generic.edit import FormView

# Create your views here.


class MainFormView(FormView):
    template_name = 'main.html'

    def get(self, request):
        return render(request, self.template_name)


class AddFormView(FormView):
    template_name = 'add.html'

    def get(self, request):
        return render(request, self.template_name)


class ArticleFormView(FormView):
    template_name = 'state.html'

    def get(self, request):
        return render(request, self.template_name)
