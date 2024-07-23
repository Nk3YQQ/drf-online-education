from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    """ Модель для курса """

    title = models.CharField(max_length=100, verbose_name='Название')
    preview = models.ImageField(upload_to='service/course/', verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание')

    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    """ Модель для урока """

    title = models.CharField(max_length=100, verbose_name='Название')
    preview = models.ImageField(upload_to='service/lesson/', verbose_name='Превью', **NULLABLE)
    video_url = models.URLField(verbose_name='Ссылка на видео', **NULLABLE)

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', related_name='lessons')

    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Subscription(models.Model):
    """ Модель для подписки """

    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')

    def __str__(self):
        return f'{self.user} - {self.course}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
