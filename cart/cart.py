from _pydecimal import Decimal

from django.conf import settings

from shop.models import Product, Topping


class EmptyTopping:
    id = 123
    name = 'Уточнить начинку по телефону'

    def __str__(self):
        return self.name


class Cart:
    def __init__(self, request):
        """Initalize the cart"""

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, topping, quantity=1, override_fields=False):
        """Добавить продукт в корзину или обновить его количество"""

        product_id = str(product.id)
        if not topping:
            topping = EmptyTopping

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': '0',
                                     'price': str(product.price),
                                     'topping': topping.id,
                                     'topping_name': topping.name}
        if override_fields:
            self.cart[product_id]['quantity'] = quantity
            self.cart[product_id]['topping_name'] = topping.name
            self.cart[product_id]['topping'] = topping.id
        else:
            self.cart[product_id]['quantity'] = str(Decimal(self.cart[product_id]['quantity']) + Decimal(quantity))
            self.cart[product_id]['topping_name'] = topping.name
            self.cart[product_id]['topping'] = topping.id

        self.save()

    def save(self):
        """Отметить сеанс как "измененный", чтобы убедиться, что он сохранен"""

        self.session.modified = True

    def remove(self, product):
        """Удаление товара из корзины"""

        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """Перебор элементов в корзине и получение продуктов из базы данных"""

        product_ids = self.cart.keys()

        # get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['topping_name'] = item['topping_name']
            item['price'] = Decimal(item['price'])
            item['quantity'] = Decimal(item['quantity'])
            item['total_price'] = int(item['price'] * item['quantity'])
            yield item

    def __len__(self):
        """Подсчет всех товаров в корзине"""
        return len([item['quantity'] for item in self.cart.values()])

    def get_total_price(self):
        """Подсчет стоимости товаров в корзине"""
        return int(sum(Decimal(item['price']) * Decimal(item['quantity']) for item in
                   self.cart.values()))

    def clear(self):
        """Удаление корзины из сессии"""
        del self.session[settings.CART_SESSION_ID]
        self.save()

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товаров'