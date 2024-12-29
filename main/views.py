from django.shortcuts import render
from .models import PersonalInfo, Skill, Project, Education, Experience, SocialMedia, Course

def home(request):
    context = {
        'personal_info': PersonalInfo.objects.first(),
        'skills': Skill.objects.all(),
        'projects': Project.objects.all().order_by('-date'),
        'education': Education.objects.all().order_by('-start_date'),
        'experiences': Experience.objects.all().order_by('-start_date'),
        'social_media': SocialMedia.objects.all(),
        'courses': Course.objects.all(),
    }
    return render(request, 'main/home.html', context)
