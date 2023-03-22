from celery import shared_task

from torty.settings import EMAIL_MAKER
from .models import Order

from io import BytesIO
import weasyprint
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage, send_mail
from django.conf import settings


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
              recipient_list=[order.email],
              fail_silently=True,
              html_message=get_template(
                  'orders/order/mail_to_manager.html').render(
                  context={'order': order})
              )
