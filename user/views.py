import functools

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic.base import View


class Decorator_Mixin(object):
    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super().as_view(*args, **kwargs)
        view = decorator(view)
        return view
# 装饰器
def decorator(func):
    @functools.wraps(func)
    def wrapper(request, *args, **kwargs):
        print('123')
        print('234')
        return func(request, *args, **kwargs)

    return wrapper


def ceshi(requests):
    return render(requests,template_name='index.html',context={'name':"ls"})
    # return redirect('/index/2018')


def demo(requests, year):
    print(year)
    print(requests.COOKIES)
    # print(reverse('index:main'))
    res = HttpResponse('hello world')
    res.set_cookie(key='name', value='ls', max_age=99999)
    return res


@method_decorator(decorator=decorator, name='get')
class Login(Decorator_Mixin,View):
    def get(self, request):
        return HttpResponse('hello world')

    def post(self, request):
        return 'login'
