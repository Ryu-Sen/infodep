from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Kitting
from .cellmodel import Cellphone
import datetime



def kitting(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_entry = Kitting.objects.all().count()

    extra_context = {}
    kitting = Kitting.objects.filter(status="kit")
    extra_context['kitting'] = kitting

    # Render the HTML template index.html with the data in the context variable
    return render_to_response(
        'kitting.html',
        extra_context
    )


def returns(request):
    extra_context = {}

    kitting = Kitting.objects.filter(status="returned")
    extra_context['kitting'] = kitting

    return render_to_response(
        'returns.html',
        extra_context
    )

def cellphones(request):
    extra_context = {}

    cellphones = Cellphone.objects.all()
    extra_context['cellphones'] = cellphones

    return render_to_response(
        'cellphones.html',
        extra_context
    )

