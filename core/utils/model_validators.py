import re

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, BaseValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


cpf_digits_re = re.compile(r'^(\d{3})\.(\d{3})\.(\d{3})-(\d{2})$')


def dv_maker(v):
    if v >= 2:
        return 11 - v
    return 0


class MinAgeValidator(BaseValidator):

    message = _("The age must be at least %(limit_value)s years old")

    def __init__(self, limit_value):
        if not isinstance(limit_value, int):
            raise TypeError('Limit value must be an integer')

        super().__init__(limit_value, message=self.message)

    def compare(self, date, limit_value):
        now = timezone.now().date()
        age = now.year - date.year
        if (now.month, now.day) < (date.month, date.day):
            age -= 1
        return age < limit_value


class BRCPFValidator(RegexValidator):
    '''
    Got the code from django-localflavor
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            regex=cpf_digits_re,
            message=_("Invalid CPF number."),
            **kwargs
        )

    def __call__(self, value):
        if not value.isdigit():
            cpf = cpf_digits_re.search(value)
            if cpf:
                value = ''.join(cpf.groups())
            else:
                raise ValidationError(self.message, code='invalid')

        if len(value) != 11:
            raise ValidationError(self.message, code='max_digits')

        orig_dv = value[-2:]
        new_1dv = sum([i * int(value[idx])
                       for idx, i in enumerate(range(10, 1, -1))])
        new_1dv = dv_maker(new_1dv % 11)
        value = value[:-2] + str(new_1dv) + value[-1]
        new_2dv = sum([i * int(value[idx])
                       for idx, i in enumerate(range(11, 1, -1))])
        new_2dv = dv_maker(new_2dv % 11)
        value = value[:-1] + str(new_2dv)
        if value[-2:] != orig_dv:
            raise ValidationError(self.message, code='invalid')
        if value.count(value[0]) == 11:
            raise ValidationError(self.message, code='invalid')
