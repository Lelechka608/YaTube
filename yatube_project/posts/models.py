from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название группы',
        help_text='Введите понятное название группы'
    )
    slug = models.SlugField(
        max_length=150,
        unique=True,
        verbose_name='Адрес группы',
        help_text='Введите slug группы. (Будет использован для генерации url)'
    )
    description = models.TextField(
        verbose_name='Описание группы',
        help_text='Добавьте описание группы'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

class Post(models.Model):
    objects = models.Manager()
    text = models.TextField(
        verbose_name='Содержание поста',
        help_text='Укажите понятное содержание поста'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
        help_text='Выберите дату публикации (по умолчанию текущая дата/время)'
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Группа для поста',
        help_text='Группа, к которой относиться пост. (может быть пустой)'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор поста',
        help_text='Автор из таблицы User'
    )




    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('pub_date',)
        get_latest_by = 'pub_date'

