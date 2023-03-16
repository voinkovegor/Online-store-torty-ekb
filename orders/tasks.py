from celery import shared_task

from torty.settings import EMAIL_MAKER
from .models import Order

from io import BytesIO
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

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
              f'Счет в приложении к письму.\n' \
              f'torty-ekb.ru, +7(999)999-99-99'
    email_customer = EmailMessage(subject,
                          message,
                          None,  # от кого письмо
                          [order.email])
    # generate PDF
    html = render_to_string('orders/order/pdf.html', {'order': order})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT / 'css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
    # attach PDF file
    email_customer.attach(f'order_{order.id}.pdf',
                 out.getvalue(),
                 'application/pdf')
    # send e-mail
    email_customer.send()

    message_maker = f'{order.first_name} {order.first_name} разместил(-а) заказ № {order.id},\n\n' \
              f'Детали заказа во вложении. \n' \
              f'Необходимо согласовать заказ по телефону: \n' \
              f'{order.phone}. \n' \
              f'E-mail заказчика {order.email}'

    email_maker = EmailMessage(subject,
                                  message_maker,
                                  None,  # от кого письмо
                                  [EMAIL_MAKER])
    # attach PDF file
    email_maker.attach(f'order_{order.id}.pdf',
                          out.getvalue(),
                          'application/pdf')
    # send e-mail
    email_maker.send()
