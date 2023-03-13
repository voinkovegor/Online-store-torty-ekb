from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Заказ № {order.id}'
    message = f'Уважаемый(-ая) {order.first_name},\n\n' \
              f'Вы успешно оформили заказ № {order.id}. ' \
              f'В ближайшее время с вами свяжется менеджер.\n' \
              f'Телефон для связи +7(999)999-99-99'
    mail_sent = send_mail(subject,
                          message,
                          None,  # от кого письмо
                          [order.email])
    return mail_sent