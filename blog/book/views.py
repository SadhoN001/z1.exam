from django.shortcuts import render
from django.utils import timezone 
from book.models import Membership
# Create your views here.

def past_month_list(request):
    one_month_ago = timezone.now() - timezone.timedelta(days=30)
    objects = Membership.objects.filter(created_at__gte=one_month_ago)
    return render(request, 'index.html', {'objects': objects})