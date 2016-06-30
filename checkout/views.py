from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import stripe


# Create your views here.
@login_required
def checkout(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    public_key = settings.STRIPE_PUBLIC_KEY
    if request.method == 'POST':
        token = request.POST['stripeToken']
        customer_id = request.user.userstripe.stripe_id
        print(token)
        try:
            customer = stripe.Customer.retrieve(customer_id)
            customer.cards.create(token)
            charge = stripe.Charge.create(
              amount=1000, # amount in cents, again
              currency="usd",
              customer=customer,
              description="Test Product"
            )
        # except stripelib.error.CardError as e:
        except Exception as ex:
            raise ex
          # The card has been declined
            pass
    context = {'publishKey': public_key}
    template = 'checkout.html'
    return render(request, template, context)