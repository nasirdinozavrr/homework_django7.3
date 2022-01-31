from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from . import models

ADMIN = 1
VIPClient = 2
CLIENT = 3
USER_TYPE = (
    (ADMIN, 'ADMIN'),
    (VIPClient, "VIP-Client"),
    (CLIENT, 'CLIENT')
)
MALE = 1
FEMALE = 2
OTHER = 3
GENDER_TYPE = (
    (MALE, 'MALE'),
    (FEMALE, "FEMALE"),
    (OTHER, 'OTHER')
)
USA = 1
CHINA = 2
INDIA = 3
FRANCE = 4
RUSSIA = 5
GERMANY = 6
JAPAN = 7
KYRGYZSTAN = 8
KAZAKHSTAN = 9

PLACE_OF_BIRTH = (
    (USA, "UNITED STATES AMERICA"),
    (CHINA, "CHINA PRC"),
    (INDIA, "INDIA REPUBLIC"),
    (FRANCE, "FRANCE REPUBLIC"),
    (RUSSIA, "RUSSIAN FEDERATION"),
    (GERMANY, "GERMANY FEDERAL REPUBLIC"),
    (JAPAN, "JAPAN"),
    (KYRGYZSTAN, "KYRGYZ REPUBLIC"),
    (KAZAKHSTAN, "KAZAKHSTAN")
)

PRIMARY_EDUCATION = 1
INCOMPLETE_SECONDARY_EDUCATION = 2
FULL_SECONDARY_EDUCATION = 3
SECONDARY_SPECIAL_EDUCATION = 4
HIGHER_PROFESSIONAL_EDUCATION = 5
BACHELORS_EDUCATION = 6
MASTERS_EDUCATION = 7

DEGREE_EDUCATION = (
    (PRIMARY_EDUCATION, "PRIMARY EDUCATION"),
    (INCOMPLETE_SECONDARY_EDUCATION, "INCOMPLETE SECONDARY DEGREE EDUCATION"),
    (FULL_SECONDARY_EDUCATION, "FULL SECONDARY DEGREE EDUCATION"),
    (SECONDARY_SPECIAL_EDUCATION, "SECONDARY SPECIAL DEGREE EDUCATION"),
    (HIGHER_PROFESSIONAL_EDUCATION, "HIGHER PROFESSIONAL DEGREE EDUCATION"),
    (BACHELORS_EDUCATION, "BACHELORS DEGREE EDUCATION"),
    (MASTERS_EDUCATION, "MASTERS DEGREE_EDUCATION")
)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    user_type = forms.ChoiceField(choices=USER_TYPE, required=True)
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True)
    place_of_birth = forms.ChoiceField(choices=PLACE_OF_BIRTH, required=True)
    degree_education = forms.ChoiceField(choices=DEGREE_EDUCATION, required=True)
    final_question = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ваша любимая книга?',
            'id': 'ho-ho'
        }
    ))

    class Meta:
        model = models.CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "age",
            "user_type",
            "gender",
            "place_of_birth",
            "degree_education",
            "final_question"


        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'username',
            'id': 'hello'}
    ))
    email = UsernameField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'email',
            'id': 'hey'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class": 'form-control',
            'placeholder': 'password',
            'id': 'hi',
        }
    ))
