import json

from decimal import Decimal
from django.http import HttpResponse


def decimal_format(value, min_decimal_places=0):
    decimal_tuple = value.as_tuple()
    have_decimal_places = -decimal_tuple.exponent
    digits = list(decimal_tuple.digits)
    while have_decimal_places < min_decimal_places:
        digits.append(0)
        have_decimal_places += 1
    while have_decimal_places > min_decimal_places and not digits[-1]:
        if len(digits) > 1:
            digits = digits[:-1]
        have_decimal_places -= 1
    return Decimal((decimal_tuple.sign, digits, -have_decimal_places))


class JSONResponse(HttpResponse):
    class UndercoverDecimal(float):
        '''
        A horrible hack that lets us encode Decimals as numbers.
        Do not do this at home.
        '''

        def __init__(self, value):
            self.value = value

        def __repr__(self):
            return str(self.value)

    def handle_decimal(self, o):
        if isinstance(o, Decimal):
            return self.UndercoverDecimal(o)
        raise TypeError()

    def __init__(self, content='', mimetype=None, status=None,
                 content_type='application/json'):
        content = json.dumps(content, default=self.handle_decimal)
        return super(JSONResponse, self).__init__(content=content,
                                                  mimetype=mimetype,
                                                  status=status,
                                                  content_type=content_type)
