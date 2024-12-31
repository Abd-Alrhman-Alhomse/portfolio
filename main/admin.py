from django.contrib import admin

from .models import PersonalInfo, Skill, Project, Education, Experience,SocialMedia, Course, Achievement

admin.site.register(PersonalInfo)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(Experience)

admin.site.register(SocialMedia)
admin.site.register(Course)

admin.site.register(Achievement)
