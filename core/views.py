from django.shortcuts import render
from django.utils import timezone
from .models import Question

# Create your views here.
def home(request):
    questions = Question.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    all_q = Question.objects.all()
    return render(request, 'core/home.html', {'questions':questions, 'all_q':all_q})