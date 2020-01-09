from django import forms
from django.utils.timezone import now


# имя, пол, возраст и уровень владения английским (выпадающим списком),
# если введенные данные это парень старше 20-и (включительно)
# и уровнем английского B2 выше, или девушка старше 22-ух
# и уровнем выше чем B1 то перейти на страницу где будет написано,
# что вы нам подходите, и что не подходит соответсвенно.


class SelectionForm(forms.Form):
    your_name = forms.CharField(
        label_suffix=' ',
        max_length=20)
    gender = forms.ChoiceField(
        label="gender",
        label_suffix=' ',
        choices=(
            ('male', 'Male'),
            ('female', 'Female')
        ))
    years = range(1940, now().year + 1)
    berth_date = forms.DateField(
        label="berth_date",
        label_suffix=' ',
        widget=forms.SelectDateWidget(years=years))
    english = forms.ChoiceField(
        label='English level',
        label_suffix=' ',
        choices=(
            ('A1', 'A1'),
            ('A2', 'A2'),
            ('B1', 'B1'),
            ('B2', 'B2'),
            ('C1', 'C1'),
            ('C2', 'C2'),
        ))
