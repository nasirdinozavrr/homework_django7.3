from django.db import models
from django.contrib.auth.models import User

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
    (PRIMARY_EDUCATION, "PRIMARY DEGREE EDUCATION"),
    (INCOMPLETE_SECONDARY_EDUCATION, "INCOMPLETE SECONDARY DEGREE EDUCATION"),
    (FULL_SECONDARY_EDUCATION, "FULL SECONDARY DEGREE EDUCATION"),
    (SECONDARY_SPECIAL_EDUCATION, "SECONDARY SPECIAL DEGREE EDUCATION"),
    (HIGHER_PROFESSIONAL_EDUCATION, "HIGHER PROFESSIONAL DEGREE EDUCATION"),
    (BACHELORS_EDUCATION, "BACHELORS DEGREE EDUCATION"),
    (MASTERS_EDUCATION, "MASTERS DEGREE EDUCATION")
)

class CustomUser(User):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    user_type = models.IntegerField(choices=USER_TYPE,
                                    verbose_name='Тип Пользователя',
                                    default=CLIENT)
    phone_number = models.CharField('phone_number', max_length=100)
    age = models.IntegerField()
    gender = models.IntegerField(choices=GENDER_TYPE, verbose_name='Гендер')
    place_of_birth = models.IntegerField(choices=PLACE_OF_BIRTH, verbose_name='Место рождения')
    degree_education = models.IntegerField(choices=DEGREE_EDUCATION, verbose_name="Степень образования")
    final_question = models.CharField("Ваша любимая книга?", max_length=50)

