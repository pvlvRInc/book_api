from django.contrib.auth.models import AbstractUser, User
from django.db import models


# todo
#  add format of files and files themself


class Books(models.Model):
    """ Book model """

    title = models.CharField(max_length=30, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    cover = models.ImageField(upload_to='media/covers/%Y/%m/%d', blank=True, verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')
    publish_year = models.DecimalField(max_digits=4, decimal_places=0, verbose_name='Дата публикации')
    pages = models.DecimalField(max_digits=6, decimal_places=0, verbose_name='Кол-во страниц')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Название')
    rating = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='Рейтинг')
    downloads = models.IntegerField(verbose_name='Скачиваний')
    age_restriction = models.DecimalField(max_digits=2, decimal_places=0, verbose_name='Возрастное ограничение')

    BOOK_TYPES = (
        ('T', 'Текст'),
        ('A', 'Аудио'),
        ('D', 'Черновик'),
    )
    type = models.CharField(choices=BOOK_TYPES, verbose_name='Тип')

    BOOK_LANGUAGES = (
        ('RUS', 'Русский'),
        ('ENG', 'Английский'),
        ('FR', 'Французкий'),
    )
    language = models.CharField(choices=BOOK_LANGUAGES, verbose_name='Язык')

    BOOK_STATUS = (
        ('Published', 'Опубликована'),
        ('Announced', 'Анонсирована'),
    )
    status = models.CharField(choices=BOOK_STATUS, verbose_name='Статус')

    publisher = models.ForeignKey('Companies', related_name='books', verbose_name='Издатель')
    authors = models.ManyToManyField('Artists', related_name='books', verbose_name='Авторы')
    illustrators = models.ManyToManyField('Artists', related_name='books', verbose_name='Иллюстраторы')
    translators = models.ManyToManyField('Artists', related_name='books', verbose_name='Переводчики')
    book_series = models.ForeignKey('Series', related_name='books', verbose_name='Серия')
    genres = models.ManyToManyField('Genres', symmetrical=False, blank=True, related_name='books', verbose_name='Жанры')
    tags = models.ManyToManyField('Tags', symmetrical=False, blank=True, related_name='books', verbose_name='Теги')

    def __str__(self):
        return self.title


class Artists(models.Model):
    """ Artist model """

    first_name = models.CharField(max_length=15, verbose_name='Имя')
    last_name = models.CharField(max_length=15, verbose_name='Фамилия')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    email = models.EmailField(blank=True, null=True, verbose_name='Почта')

    ARTIST_TYPES = (
        ('I', 'Illustrator'),
        ('A', 'Author'),
        ('T', 'Translator'),
    )
    type = models.CharField(choices=ARTIST_TYPES, verbose_name='Вид деятельности')

    def __str__(self):
        return self.first_name + " " + self.last_name


class Companies(models.Model):
    """ Company model """
    name = models.CharField(max_length=15, verbose_name='Название')
    email = models.EmailField(blank=True, null=True, verbose_name='Почта')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return self.name


class Series(models.Model):
    """ Series model """
    name = models.CharField(max_length=15, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name


class Genres(models.Model):
    """ Genre model """
    name = models.CharField(max_length=15, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name


class Tags(models.Model):
    """ Tag model """
    name = models.CharField(max_length=15, verbose_name='Название')

    def __str__(self):
        return self.name


class Commentary(models.Model):
    """ Commentary model """

    ip = models.CharField(max_length=10, verbose_name='IP Адресс')
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='commentaries', verbose_name='Книга')
    user = models.ForeignKey(User, blank=True, null=True, related_name='commentaries', verbose_name='Пользователь')
    content = models.CharField(max_length=10, verbose_name='Содержание')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='child',
                               verbose_name='Родитель')

    def __str__(self):
        return self.book.title + self.content[:self.content.find('', 15)] + '...'


class UserBookRating(models.Model):
    """ UserBookRating model """

    user = models.ForeignKey(User, verbose_name='Пользователь')
    rate = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='Рейтинг')
    book = models.ForeignKey(Books, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Книга')

    def __str__(self):
        return ' '.join([self.user, self.book, self.rating])


class Quote(models.Model):
    """ Quote model """

    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='quotes', verbose_name='Книга')
    user = models.ForeignKey(User, related_name='quotes', verbose_name='Пользователь')
    content = models.CharField(max_length=10, verbose_name='Содержание')
    up_votes = models.IntegerField(verbose_name='Голоса за')
    down_votes = models.IntegerField(verbose_name='Голоса против')

    def __str__(self):
        return self.book.title + ' ' + self.pk

class UserProfile(models.Model):
    """
    Profile model

    Additional content for User model
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Пользователь')
    first_name = models.CharField(max_length=15, verbose_name='Имя')
    last_name = models.CharField(max_length=15, verbose_name='Фамилия')
    avatar = models.ImageField(upload_to='media/avatars/%Y/%m/%d', blank=True, verbose_name='Аватар')

    read_books = models.ManyToManyField(Books, symmetrical=False, related_name='+', verbose_name='Прочитано')
    current_books = models.ManyToManyField(Books, symmetrical=False, related_name='+', verbose_name='Читает')
    planned_books = models.ManyToManyField(Books, symmetrical=False, related_name='+', verbose_name='В планах')
    forsaken_books = models.ManyToManyField(Books, symmetrical=False, related_name='+', verbose_name='Брошено')

    def __str__(self):
        return self.user.get_username()

    # todo
    #  add image eraser function
