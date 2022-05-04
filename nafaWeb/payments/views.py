from multiprocessing import context
from django.http import JsonResponse
from django.shortcuts import render
from .models import Membership, Order
from accounts.models import Profile
import json
# Create your views here.

def checkout(request, id):
    membership = Membership.objects.get(id=id)
    
    context = {"membership":membership}
    return render(request, 'payments/checkout.html', context)


def paymentComplete(request):
    body = json.loads(request.body)
    membership = Membership.objects.get(id=body['membershipId'])
    Order.objects.create(
        product = membership
    )
    user = Profile.objects.get(id=request.user.id)
    user.membership=membership
    user.save()
    print(user.membership)
    return JsonResponse("Payment completed!", safe=False)


    