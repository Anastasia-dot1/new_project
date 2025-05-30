from django.contrib import admin
from .models import caexam
from django.contrib.auth.models import User

class caexamAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'exam_date', 'is_public')
    list_filter = ('is_public', 'created_at')
    search_fields = ('title', 'users__email')
    filter_horizontal = ('users',)  # для удобного редактирования M2M
    
    date_hierarchy = 'exam_date'  # иерархия по дате экзамена

admin.site.register(caexam, caexamAdmin)