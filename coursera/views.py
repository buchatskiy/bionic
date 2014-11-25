from django.http import HttpResponse
from coursera.models import Student

def index(request):
    student_list=Student.objects.order_by('student_text')[:]
    output = ', '.join([p.student_text for p in student_list])
    return HttpResponse(output)