from django.shortcuts import render, get_object_or_404
from django.views import generic
from hsg.models import Group
from django.http import HttpResponse
from hsg.functions import generate_confirmation


class DetailView(generic.DetailView):
    model = Group
    template_name = 'detail.html'


def list_year(request, year):
    hsg_list = Group.objects.filter(registration__date__year=year,
                                    registration__form='FULL')
    return render(request, 'list.html', {'list': hsg_list})


def detail_view(request, pk):
    hsg = get_object_or_404(Group, pk=pk)
    contacts = hsg.registration.first().contact.all()
    registrations = hsg.registration.all()
    return render(request, 'detail.html', {'group': hsg,
                                           'contacts': contacts,
                                           'registrations': registrations})


def all_hsgs(request):
    return render(request, 'list.html',
                  {'list': Group.objects.all().order_by('name')})


def gen_reg(request, registration_id):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Bestaetigung.pdf"'
    response = generate_confirmation(response, registration_id)
    return response
