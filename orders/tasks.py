from celery import shared_task
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
    email = EmailMessage(subject,
                          message,
                          'admin@torty.ru',  # от кого письмо
                          [order.email])
    # generate PDF
    html = render_to_string('orders/order/pdf.html', {'order': order})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT / 'css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
    # attach PDF file
    email.attach(f'order_{order.id}.pdf',
                 out.getvalue(),
                 'application/pdf')
    # send e-mail
    email.send()
