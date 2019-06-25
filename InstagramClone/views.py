""" InstaClone Views """
# Django
from django.http import HttpResponse, JsonResponse

# Utilities
from datetime import datetime
import pdb

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh!, Current server time is {now}'.format(now=str(now)))

def sorted_numbers(request):
    numbers = request.GET['numbers']

    numbers = list(map(int, numbers.split(',')))

    numbers = sorted(numbers)

    data = {
        'status': 'ok',
        'numbers': sorted(numbers),
        'message': 'sort ok'
    }
    #pdb.set_trace()
    return JsonResponse(data, safe=False)


def say_hi(request, name, age):
    """Return a greeting"""
    if age <12:
        message = 'Sorry {}, you are not alowed here'.format(name)
    else:
        message = 'Hola, {}, welcome to InstaClone'.format(name)
    return HttpResponse(message)

