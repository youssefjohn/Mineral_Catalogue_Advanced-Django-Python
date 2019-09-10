'''
   BELOW ARE MY VIEWS. THREE OF THEM WILL COLLECT INFORMATION,
   THEN FEED IT TO THE TEMPLATE.
'''

from django.shortcuts import render, get_object_or_404, reverse
from .models import Mineral
from random import choice
from django.http import HttpResponseRedirect



def index_view(request, letter):
    if request.method == 'POST':
        name = request.POST.get('name')
        # This if statement looks for the search bar inputs
        mins = Mineral.objects.filter(name__icontains=name)

    # This elif finds all objects when a user clicks on home
    elif letter == 'home':
        mins = Mineral.objects.all()

    # All other elifs search by category, the category navbar
    elif letter == 'silicate':
        mins = Mineral.objects.filter(category__icontains=letter)

    elif letter == 'oxide':
        mins = Mineral.objects.filter(category__icontains=letter)

    elif letter == 'sulfate':
        mins = Mineral.objects.filter(category__icontains=letter)

    elif letter == 'sulfide':
        mins = Mineral.objects.filter(category__icontains=letter)

    elif letter == 'carbonate':
        mins = Mineral.objects.filter(category__icontains=letter)

    elif letter == 'halide':
        mins = Mineral.objects.filter(category__icontains=letter)

    elif letter == 'sulfosalt':
        mins = Mineral.objects.filter(category__icontains=letter)

    elif letter == 'phosphate':
        mins = Mineral.objects.filter(category__icontains=letter)

    elif letter == 'borate':
        mins = Mineral.objects.filter(category__icontains=letter)

    elif letter == 'organic':
        mins = Mineral.objects.filter(category__icontains=letter)

    elif letter == 'arsenate':
        mins = Mineral.objects.filter(category__icontains=letter)

    elif letter == 'native elements':
        mins = Mineral.objects.filter(category__icontains=letter)

    elif letter == 'other':
        mins = Mineral.objects.filter(category__icontains=letter)

    else:
        # This else looks for objects in the letter navbar
        mins = Mineral.objects.filter(name__startswith=letter)


    minerals = {'mineral_names':mins}

    return render(request, 'rocks/index.html', context=minerals)




def details_view(request, pk):
    '''
        DETAILS VIEW WORKS OFF OF THE INDEX VIEW. WHEN SOMEONE CHOOSES A MINERAL
        FROM THE INDEX URL PAGE, THE PK OF THE MINERAL IS CAPTURED AND GIVEN TO
        DETAILS VIEW. THE DETAILS VIEW THEN LOOKS THROUGH THE DATABASE FOR THE
        MATCHING MINERAL USING THE PK, THEN RENDERS IT.
    '''


    mins = get_object_or_404(Mineral, pk=pk)
    minerals = {"mineral_detail": mins}


    return render(request, "rocks/details.html", context=minerals)

def random_view(request):
    '''
       RANDOM VIEW SELECTS ALL OF THE OBJECTS FROM THE DATABASE, THEN THE
       CHOICE FUNCTION PICS OUT ONE ENTRY RANDOMLY, THEN RENDERS THE IT TO THE
       TEMPLATE
    '''

    all = Mineral.objects.all()

    new_all = choice(all)
    random = {"random_mineral": new_all}

    return render(request, "rocks/random.html", context=random)


