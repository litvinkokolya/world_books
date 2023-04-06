from django.contrib import admin
from .models import Author, Book, Genre, Language, Status, Bookinstance

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')
    list_filter = ('genre', 'author')

@admin.register(Bookinstance)
class BookinstanceAdmin(admin.ModelAdmin):
    list_filter = ('book', 'status')
    fieldsets = ((' Экземпляр книги ', {'fields': ('book', 'imprint', 'inv _nom')}),
                 ('Статус и окончание его действия', {'fields': ('status', 'due_back')}),)


#admin.site.register(Author)
admin.site.register(Author, AuthorAdmin)
#admin.site.register(Book)
#admin.site.register(Book, BookAdmin)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)
#admin.site.register(Bookinstance)
#admin.site.register(Bookinstance, BookinstanceAdmin)





