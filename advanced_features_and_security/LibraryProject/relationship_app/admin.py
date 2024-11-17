from django.contrib import admin

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('email','first_name','last_name','date_of_birth')
    search_fields = ('email','first_name','last_name','date_of_birth')
    list_filter = ('email','first_name','last_name','date_of_birth')
    
