from django.shortcuts import render
from .models import caexam

def caexam_view(request):
    exams = caexam.objects.filter(is_public=True)
    context = {
        'exams': exams,
        'fio': 'Анастасия Чурсина',  # Замените на свои данные
        'group': 'Группа XYZ-123'     # Замените на свои данные
    }
    return render(request, 'exams/caexam.html', context)