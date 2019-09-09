'''
   BELOW ARE MY VIEWS. THREE OF THEM WILL COLLECT INFORMATION,
   THEN FEED IT TO THE TEMPLATE.
'''

from django.shortcuts import render, get_object_or_404, reverse
from .models import Mineral
from random import choice
from django.http import HttpResponseRedirect



def index(request, letter):
    if request.method == 'POST':
        name = request.POST.get('name')
        print(name)
        mins = Mineral.objects.filter(name__icontains=name)

    elif letter == 'home':
        mins = Mineral.objects.all()

    else:
        mins = Mineral.objects.filter(name__startswith=letter)

    minerals = {'mineral_names':mins}
    return render(request, 'rocks/index.html', context=minerals)




def details(request, pk):
    '''
        DETAILS VIEW WORKS OFF OF THE INDEX VIEW. WHEN SOMEONE CHOOSES A MINERAL
        FROM THE INDEX URL PAGE, THE PK OF THE MINERAL IS CAPTURED AND GIVEN TO
        DETAILS VIEW. THE DETAILS VIEW THEN LOOKS THROUGH THE DATABASE FOR THE
        MATCHING MINERAL USING THE PK, THEN RENDERS IT.
    '''



    print('works')
    mins = get_object_or_404(Mineral, pk=pk)
    minerals = {"mineral_detail": mins}


    return render(request, "rocks/details.html", context=minerals)

def random(request):
    '''
       RANDOM VIEW SELECTS ALL OF THE OBJECTS FROM THE DATABASE, THEN THE
       CHOICE FUNCTION PICS OUT ONE ENTRY RANDOMLY, THEN RENDERS THE IT TO THE
       TEMPLATE
    '''

    all = Mineral.objects.all()

    new_all = choice(all)
    random = {"random_mineral": new_all}

    return render(request, "rocks/random.html", context=random)


