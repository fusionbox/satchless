from django.core.exceptions import ImproperlyConfigured
from django.template.response import TemplateResponse

from ....checkout import app
from ....order import forms, handler

class SingleStepCheckoutApp(app.CheckoutApp):
    billing_form_class = forms.BillingForm
    checkout_templates = [
        'satchless/checkout/checkout.html'
    ]

    def checkout(self, request, order_token):
        """
        Checkout step 1 of 1
        The order is split into delivery groups and the user gets to pick both the
        delivery and payment methods.
        """
        order = self.get_order(request, order_token)
        if not order or order.status != 'checkout':
            return self.redirect_order(order)
        delivery_groups = order.groups.all()
        for group in delivery_groups:
            delivery_types = list(handler.delivery_queue.enum_types(group))
            if len(delivery_types) != 1:
                raise ImproperlyConfigured("The singlestep checkout requires "
                                           "exactly one delivery type per group.")
            group.delivery_type = delivery_types[0][1].typ
            group.save()
        delivery_group_forms = forms.get_delivery_details_forms_for_groups(delivery_groups,
                                                                           request.POST)
        delivery_valid = True
        if request.method == 'POST':
            delivery_valid = True
            for group, typ, form in delivery_group_forms:
                if form:
                    delivery_valid = delivery_valid and form.is_valid()
        payment_types = list(handler.payment_queue.enum_types(order))
        if len(payment_types) != 1:
            raise ImproperlyConfigured("The singlestep checkout requires "
                                       "exactly one payment methods.")
        order.payment_type = payment_types[0][1].typ
        order.save()
        billing_form = self.billing_form_class(request.POST or None,
                                               instance=order)
        payment_form = forms.get_payment_details_form(order, request.POST)
        if request.method == 'POST':
            billing_valid = billing_form.is_valid()
            payment_valid = payment_form.is_valid() if payment_form else True
            if billing_valid and delivery_valid and payment_valid:
                order = billing_form.save()
                for group, typ, form in delivery_group_forms:
                    handler.delivery_queue.create_variant(group, form)
                handler.payment_queue.create_variant(order, payment_form)
                order.set_status('payment-pending')
                return self.redirect('confirmation',
                                     order_token=order.token)
        return TemplateResponse(request, self.checkout_templates, {
            'billing_form': billing_form,
            'delivery_group_forms': delivery_group_forms,
            'order': order,
            'payment_form': payment_form,
        })

checkout_app = SingleStepCheckoutApp()