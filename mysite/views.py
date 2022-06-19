import datetime

from django.http import Http404, HttpResponse
from django.template.loader import get_template
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello World")


def current_datetime(request):
    now = datetime.datetime.now()
    html = f"<html><body>It is {now} now.</body></html>"
    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    # html = f"<html><body>In {offset} hour(s), it will be {dt}.</body></html>"
    # return HttpResponse(html)
    return render(request,
                'hours_ahead.html', 
                {'hour_offset': offset, 'next_time': dt}, 
    )


# Exer 2 math and valid_date
def mathematics(request, num_1, num_2):
    try:
        inp_1 = int(num_1)
        inp_2 = int(num_2)
    except ValueError:
        raise Http404()
    
    sum_of_numbers = inp_1 + inp_2
    difference = inp_1 - inp_2
    product = inp_1 * inp_2
    quotient = inp_1 / inp_2
    
    return render(request,
                  'mathematics.html',
                  {'first_value': inp_1,
                   'second_value': inp_2,
                   'display_sum': sum_of_numbers,
                   'display_diff': difference,
                   'display_product': product,
                   'display_quotient': "{:.3f}".format(quotient),
                   }
    )


def validate_date(request, year, month, day):
    # date_is_validated = True
    try:
        given_date = datetime.datetime(int(year), int(month), int(day))

    except ValueError:
        raise Http404("Invalid Date")
    
    return render(request,
                  'valid_date.html',
                  {'given_date': given_date.strftime("%Y/%m/%d")}
    )

    # if date_is_validated:
    #     html = f"<html><body>{given_date} is a valid date</body></html>"
    # else:
    #     html = f"<html><body>{given_date} is not a valid date</body></html>"
    
    # return HttpResponse(html)


def current_datetime_2(request):
    now = datetime.now()
    # template = get_template('current_datetime.html')
    # html = template.render({'current_date': now})
    return render(request, 
                'current_datetime.html',
                {'current_date': now},
    )
    # return HttpResponse(html)
    
        
def print_athlete_list(request):
    try:
        
        ID = [1, 2, 3, 4]
        name = ["John", "Smith", "Ray", "Happy"]
        sport = ["basketball", "soccer", "baseball", "basketball"]
    
        athletes = zip(ID, name, sport)
    except ValueError:
        raise Http404()
    
    return render(request,
                  'athlete.html',
                  {"athletes_list": athletes},
    )
    

def print_a_dictionary(request):
    try:
        students = [
            {"id": 1, "name": "John", "grades": 95},
            {"id": 2, "name": "Smith", "grades": 87},
            {"id": 3, "name": "Ray", "grades": 75},
            {"id": 4, "name": "Happy", "grades": 85},
            
        ]
    except ValueError:
        raise Http404()

    return render(request,
                  'student.html',
                  {'student_list': students},
    )