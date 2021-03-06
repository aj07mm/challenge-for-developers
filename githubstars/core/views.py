from django.urls import reverse_lazy
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View
from django.views.generic import ListView
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from django.utils.decorators import method_decorator

from githubstars.core.models import Repository
from githubstars.core.forms import RegisterForm
from githubstars.core.githubapi import GithubAPI


class BaseView(View):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(BaseView, self).dispatch(request, *args, **kwargs)


class HomeView(BaseView):

    template_name = 'base.html'

    def get(self, request):
        return render(request, self.template_name)


home = HomeView.as_view()


class RegisterView(View):

    template_name = 'register.html',
    form_class = RegisterForm
    success_url = reverse_lazy('home')

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            User = get_user_model()
            user = User.objects.create_user(username=form.cleaned_data['username'])
            user.set_password(form.cleaned_data['password'])
            user.is_staff = True
            user.save()

            user.user_permissions.set([
                Permission.objects.get(codename='change_repository'),
                Permission.objects.get(codename='delete_repository')])

            return redirect(self.success_url)

        return render(request, self.template_name, {'form': form})


register = RegisterView.as_view()


class RepositoryView(BaseView):

    def to_dict(self, repositories):
        result = []

        for repository in repositories:
            result.append({
                "name": repository.name,
                "url": repository.url,
                "language": repository.language or '-',
                "tags": repository.tags or '-',
                "url_admin": reverse_lazy('admin:core_repository_change', args=[repository.pk])
            })

        return result

    def get(self, request):
        repositories = Repository.objects.filter_by_tag(user=request.user, tag_name=request.GET.get('tag_name', ''))

        return JsonResponse(self.to_dict(repositories), safe=False)


repositories = RepositoryView.as_view()


class GetRepositoriesGithubView(BaseView):

    def get(self, request):
        contents = GithubAPI(request.user.username).get_content()

        for content in contents:
            Repository.objects.get_or_create(repo_id=content['id'],
                                             name=content['name'],
                                             url=content['url'],
                                             user=request.user,
                                             language=content['language'])

        return redirect(reverse_lazy('home'))


get_repositories = GetRepositoriesGithubView.as_view()
