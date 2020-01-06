from django import forms


class NameForm(forms.Form):
    years = range(1940, 2020)
    your_name = forms.CharField(label='Your name', max_length=20)
    gender = forms.ChoiceField(label="gender", choices=(('m', 'male'), ('f', 'female')))
    berth_date = forms.DateField(label="berth_date", widget=forms.SelectDateWidget(years=years))
    english = forms.ChoiceField(label='English level', choices=(
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('C1', 'C1'),
        ('C2', 'C2')
    ))

    # имя, пол, возраст и уровень владения английским (выпадающим списком),
    # если введенные данные это парень старше 20-и (включительно) и уровнем английского B2 выше, или девушка старше 22-ух и уровнем выше чем B1 то перейти на страницу где будет написано, что вы нам подходите, и что не подходит соответсвенно.
