from django.contrib import admin
from .models import Book , CustomUser
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','publication_year')
    search_fields = ('title','author')
    list_filter = ('title','author','publication_year')
    
admin.site.register(Book , BookAdmin)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email','first_name','last_name','date_of_birth')
    search_fields = ('email','first_name','last_name','date_of_birth')
    list_filter = ('email','first_name','last_name','date_of_birth')

admin.site.register(CustomUser, CustomUserAdmin)



