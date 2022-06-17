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
    html = f"<html><body>Sum: {sum_of_numbers}, Difference: {difference}, Product: {product}, Quotient: {quotient}</body></html"
    return HttpResponse(html)


def validate_date(request, year, month, day):
    date_is_validate = True
    try:
        given_date = datetime(int(year), int(month), int(day))

    except ValueError:
        raise Http404()

    if date_is_validate:
        html = f"<html><body>{given_date} is a valid date</body></html>"
    else:
        html = f"<html><body>{given_date} is not a valid date</body></html>"
    
    return HttpResponse(html)


def current_datetime_2(request):
    now = datetime.now()
    # template = get_template('current_datetime.html')
    # html = template.render({'current_date': now})
    return render(request, 
                'current_datetime.html',
                {'current_date': now},
    )
    # return HttpResponse(html)