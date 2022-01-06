from django.shortcuts import render
from .models import (Expertise, TeamMember, CreativeDesign,
                     MyselfModel, MyProject, Service)
from django.views import generic


class HomePageView(generic.ListView):
    model = Expertise
    template_name = 'interface/index.html'
    context_object_name = 'skills'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['designs'] = CreativeDesign.objects.all()
        context['members'] = TeamMember.objects.all()
        context['myself'] = MyselfModel.objects.all()
        context['projects'] = MyProject.objects.all()
        context['services'] = Service.objects.all()
        return context


