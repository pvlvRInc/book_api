from django.db import models


# todo
#  add format of files and files themself
#  add quotes
#  add verbose and related names
#  define __str__
#  override User model

class Books(models.Model):
    """ Book model """

    title = models.CharField(max_length=30)
    description = models.TextField()
    cover = models.ImageField(upload_to='media/%Y/%m/%d', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    publish_year = models.DecimalField(max_digits=4, decimal_places=0)
    pages = models.DecimalField(max_digits=6, decimal_places=0)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    downloads = models.IntegerField()

    BOOK_TYPES = (
        ('T', 'Text'),
        ('A', 'Audio'),
        ('D', 'Draft'),
    )
    type = models.CharField(choices=BOOK_TYPES)

    publisher = models.ForeignKey('Companies', related_name='books')
    authors = models.ManyToManyField('Artists', related_name='books')
    illustrators = models.ManyToManyField('Artists', related_name='books')
    translators = models.ManyToManyField('Artists', related_name='books')
    book_series = models.ForeignKey('Series', related_name='books')  # todo add model
    genres = models.ManyToManyField('Genres', symmetrical=False, blank=True, related_name='books')
    tags = models.ManyToManyField('Tags', symmetrical=False, blank=True, related_name='books')


class Artists(models.Model):
    """ Artist model """

    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(blank=True, null=True)

    ARTIST_TYPES = (
        ('I', 'Illustrator'),
        ('A', 'Author'),
        ('T', 'Translator'),
    )
    type = models.CharField(choices=ARTIST_TYPES)


class Companies(models.Model):
    """ Company model """
    name = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_year = models.DecimalField(max_digits=4, decimal_places=0)


class Series(models.Model):
    """ Series model """
    name = models.CharField(max_length=15)
    description = models.TextField()


class Genres(models.Model):
    """ Genre model """
    name = models.CharField(max_length=15)
    description = models.TextField()


class Tags(models.Model):
    """ Tag model """
    name = models.CharField(max_length=15)


class Commentary(models.Model):
    """ Commentary model """

    ip = models.CharField(max_length=10)
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='commentaries')
    user = models.ForeignKey(blank=True, null=True, related_name='commentaries')  # todo add model
    content = models.CharField(max_length=10)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)


class UserBookRating(models.Model):
    """ UserBookRating model """

    user = models.ForeignKey()  # todo add model
    content = models.CharField(max_length=10)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

class Quotes(models.Model):
    """ Quote model """

    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='quotes')
    user = models.ForeignKey(related_name='quotes')  # todo add model
    content = models.CharField(max_length=10)
    up_votes = models.IntegerField()
    down_votes = models.IntegerField()