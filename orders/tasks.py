from celery import shared_task

from torty import settings
from .models import Order

from django.template.loader import get_template
from django.core.mail import send_mail



@shared_task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Заказ № {order.id}'
    send_mail(subject,
              message=None,
              from_email='admin@torty.ru',
              recipient_list=[order.email],
              fail_silently=True,
              html_message=get_template(
                  'orders/order/mail_to_customer.html').render(
                  context={'order': order})
              )

    send_mail(subject,
              message=None,
              from_email=None,
              recipient_list=[settings.EMAIL_MAKER],
              fail_silently=True,
              html_message=get_template(
                  'orders/order/mail_to_manager.html').render(
                  context={'order': order})
              )
