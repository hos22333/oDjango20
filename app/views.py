"""
Definition of views.
"""
from ast import Return
from . import oClasses
import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt


from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

@csrf_exempt
def oClassTest(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))  # Decode bytes to str
        except json.JSONDecodeError:
            # Handle invalid JSON here (e.g., return an error response)
            return HttpResponseBadRequest('Invalid JSON')


    # Create an instance of the NumberOperations class
    oVarIn1 = data.get("ooVarIn1")
    oVarIn2 = data.get("ooVarIn2")
    oVarIn3 = data.get("ooVarIn3")

    print(oVarIn1)
    print(oVarIn2)
    print(oVarIn3)

    operations = oClasses.NumberOperations(oVarIn1, oVarIn2, oVarIn3)

    # Sum the numbers
    oVarRes1 = operations.sum_numbers()

    # Multiply the numbers
    oVarRes2 = operations.multiply_numbers()

   
    return JsonResponse({'ooVarRes1': oVarRes1,
                        'ooVarRes2': oVarRes2,})
    

