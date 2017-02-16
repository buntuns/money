from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Income 
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'gold/index.html'
    context_object_name = 'latest_income_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Income.objects.order_by('-pub_date')[:5]
        
def add_the_income(request):
     try:
         the_last = Income.objects.order_by('-id')[0].remaining
     except:
         the_last =0
     latest_income_list = Income.objects.order_by('-pub_date')[:5]
     if request.POST['bank'] == "in":
         income = Income(income_text=request.POST['add_income'],money_in_text=request.POST['add_money'],remaining=the_last+int(request.POST['add_money']),pub_date=timezone.now())
         income.save()
     else:
         expenses = Income(expenses_text=request.POST['add_income'],money_out_text=request.POST['add_money'], remaining=the_last-int(request.POST['add_money']),pub_date=timezone.now())
         expenses.save()
     context = {'latest_income_list':latest_income_list}
     return render(request,'gold/index.html',context)

def history(request):
    latest_income_list = Income.objects.order_by('pub_date')[:500]
    context = {'latest_income_list':latest_income_list}
    return render(request,'gold/history.html',context)
