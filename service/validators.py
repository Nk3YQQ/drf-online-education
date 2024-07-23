from rest_framework.exceptions import ValidationError


class CheckLessonURLValidator:
    """ Валидатор для проверки ссылки """

    def __init__(self, field):
        self.field = field

    def __call__(self, val):
        tmp_val = dict(val).get(self.field)
        if tmp_val is None or 'youtube.com' in tmp_val:
            return
        raise ValidationError('Ссылка не может использоваться')
