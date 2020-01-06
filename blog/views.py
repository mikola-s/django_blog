from django.shortcuts import render
from django.template import loader

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import FormView
from .forms import NameForm


class MyFormView(FormView):
    template_name = 'blog/index.html'
    http_method_names = ['get', 'post']
    form_class = NameForm
    success_url = 'taken/'


    def form_valid(self, form):
        data = form.cleaned_data
        age = timezone.now().year - data['berth_date'].year
        if (data['gender'] == 'm' and age > 19 and data['english'] > 'B2' or
                data['gender'] == 'f' and age > 22 and data['english'] > 'B1'):
            return super().form_valid(form)
        else:
            return HttpResponseRedirect('/')

    def get(self, request, *args, **kwargs):
        print('GET REQUEST')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        return super().post(request, *args, **kwargs)


# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#
#         # check whether it's valid:
#         if form.is_valid():
#             data = form.cleaned_data
#             age = timezone.now().year - data['berth_date'].year
#             if (data['gender'] == 'm' and age > 19 and data['english'] > 'B2' or
#                     data['gender'] == 'f' and age > 22 and data['english'] > 'B1'):
#                 print(form.cleaned_data)
#             # redirect to a new URL:
#             # если введенные данные это парень старше 20-и (включительно) и уровнем английского B2 выше,
#             # или девушка старше 22-ух и уровнем выше чем B1 то перейти на страницу где будет написано, что вы нам подходите, и что не подходит соответсвенно.
#             # {'your_name': 'asdasfafa', 'gender': 'm', 'berth_date': datetime.date(2020, 1, 1), 'english': 'A1'}
#             return HttpResponseRedirect('/taken/')
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()
#
#     return render(request, 'blog/index.html', {'form': form})

def taken(request):
    return render(request, 'blog/taken.html')
