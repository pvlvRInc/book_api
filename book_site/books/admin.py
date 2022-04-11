from django.contrib import admin

from books.models import Books, Artists, Companies, Series, Genres, Tags, Commentary, UserBookRating, Quote, UserProfile

# class BookAdmin(admin.ModelAdmin):
#     fields =
#     class Meta:
#         verbose_name = 'Книга'
#         verbose_name_plural = 'Книги'


admin.register(Books)
admin.register(Artists)
admin.register(Companies)
admin.register(Series)
admin.register(Genres)
admin.register(Tags)
admin.register(Commentary)
admin.register(UserBookRating)
admin.register(Quote)
admin.register(UserProfile)
