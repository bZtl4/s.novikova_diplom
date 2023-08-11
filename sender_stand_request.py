import config as c
import requests


# Запрос на создание заказа
def request_create_order(headers, body):
    return requests.post(c.URL_SERVICE + c.CREATE_ORDER_PATH,
                         json=body,
                         headers=headers)


# Выполнить запрос на получение заказа по треку
def request_get_order(param):
    return requests.get(c.URL_SERVICE + c.GET_ORDER_PATH,
                        params=param)
