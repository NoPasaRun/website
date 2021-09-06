from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from user.models import UserModel
from website.models import AddModel, CommentModel, ImageModel
from .forms import CommentForm


class MainView(View):

    def get(self, request):
        adds = sorted(AddModel.objects.all(), key=lambda elem: elem.created_at)
        return render(request, 'website/index.html', {'profiles': UserModel.objects.all(), 'adds': adds})

    def post(self, request):
        form = CommentForm(request.POST)
        if form.is_valid():
            CommentModel(article=form.cleaned_data['article'],
                         text=form.cleaned_data['text'],
                         writer=request.user.profile).save()
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('/user/login')


class CreateView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'website/create.html', {})

    def post(self, request):
        AddModel(title=request.POST['title'],
                       description=request.POST['description'],
                       creator=request.user.profile).save()
        add = AddModel.objects.all()[len(AddModel.objects.all())-1]
        for image in request.FILES.getlist('images'):
            ImageModel(add=add,
                       image=image,
                       description="Image").save()
        return HttpResponseRedirect('/')


class ShowAddView(LoginRequiredMixin, View):

    def get(self, request, pk):
        add = get_object_or_404(AddModel, pk=pk)
        return render(request, 'website/show_adds.html', {'add': add})