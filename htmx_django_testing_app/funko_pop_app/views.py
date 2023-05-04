from django.shortcuts import render
from funko_pop_app.models import FunkoPop


def funko_pop_list(request):
    funko_pops = FunkoPop.objects.all()

    context = {
        'funko_pops': funko_pops,
    }
    return render(request, 'funko_pop_app/funko_pop_list.html', context)
