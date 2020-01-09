from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import FormView
from django.contrib import messages

from .forms import SelectionForm


class SelectionClassFormView(FormView):
    template_name = 'blog/accepted.html'
    http_method_names = ['get', 'post']
    form_class = SelectionForm
    success_url = '/accepted/'

    # если введенные данные это парень старше 20-и (включительно) и уровнем английского B2 выше,
    # или девушка старше 22-ух и уровнем выше чем B1 то перейти на страницу где будет написано,
    # что вы нам подходите, и что не подходит соответсвенно.

    def form_valid(self, form):
        print(form.cleaned_data)
        data = form.cleaned_data
        age = timezone.now().year - data['berth_date'].year
        if (data['gender'] == 'male' and age > 19 and data['english'] > 'B2' or
                data['gender'] == 'female' and age > 22 and data['english'] > 'B1'):
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    # def get(self, request, *args, **kwargs):
    #     return super().get(request, *args, **kwargs)
    #
    # def post(self, request, *args, **kwargs):
    #     return super().post(request, *args, **kwargs)

    # если введенные данные это парень старше 20-и (включительно) и уровнем английского B2 выше,
    # или девушка старше 22-ух и уровнем выше чем B1 то перейти на страницу где будет написано,
    # что вы нам подходите, и что не подходит соответсвенно.


def age_condition(form, age_limit):
    if form.cleaned_data["age"] < age_limit:
        form.add_error("berth_date", f"You are young! You are {form.cleaned_data['age']}. "
                                     f"Need {age_limit} and older")
    return form


def fail_conditions(form):
    data = form.cleaned_data
    if data["english"] < "B2":
        form.add_error("english", "You english is bed! Need B2 or higher.")
    if data["gender"] == "male":
        form = age_condition(form, 20)
    elif data["gender"] == "female":
        form = age_condition(form, 23)
    else:
        form.add_error("gender", "Who are you?")
    return form


def selection_def_view(request):
    if request.method == 'POST':
        form = SelectionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data['age'] = timezone.now().year - data['berth_date'].year
            if data['english'] > 'B1' and (data['gender'] == 'male' and data['age'] > 19 or
                                           data['gender'] == 'female' and data['age'] > 22):
                print('success')
                return render(request, "blog/accepted.html", {'data': data})
            else:
                print('no')
                return render(request, 'blog/selection_def.html', {'form': fail_conditions(form)})
    else:
        form = SelectionForm()

    return render(request, 'blog/selection_def.html', {'form': form})


def accepted(request, data):
    return render(request, 'blog/accepted.html', {'data': data})


def index(request):
    return render(request, 'blog/index.html')
