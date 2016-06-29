from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import stripe as stripelib

stripelib.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.
@login_required
def checkout(request):
    public_key = settings.STRIPE_PUBLISHABLE_KEY
    if request.method == 'POST':
        token = request.POST['stripeToken']
        try:
            charge = stripelib.Charge.create(
              amount=1000, # amount in cents, again
              currency="sgd",
              source=token,
              description="payment@rabbitmq.com"
            )
        # except stripelib.error.CardError as e:
        except Exception as ex:
            raise ex
          # The card has been declined
            pass
    context = {'publishKey': public_key}
    template = 'checkout.html'
    return render(request, template, context)