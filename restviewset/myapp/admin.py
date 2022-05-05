from django.contrib import admin
from .models import StudentModel
# Register your models here.


@admin.register(StudentModel)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ("marks","email", "roll", "name", "id")[::-1]
    # ordering  = ['roll']