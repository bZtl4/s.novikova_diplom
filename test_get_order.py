# Саша Новикова, 7-я когорта - Финальный проект. Инженер по тестированию плюс
import data
import sender_stand_request

# Получить номер трека заказа
def get_order_track():
    # Сформировать параметры
    headers = data.headers.copy()
    body = data.order_body.copy()

    # Формирование ответа на запрос
    response = sender_stand_request.request_create_order(headers, body)

    # Получить трек заказа (проверка)
    assert response.status_code == 201, "Ошибка: Статус не равен 201"
    return response.json()["track"]


# Получить заказ
def get_order(order_track):
    # Сформировать параметры
    param = data.params.copy()
    param["t"] = order_track

    # Отправить запрос
    response = sender_stand_request.request_get_order(param)

    # Проверить статус
    assert response.status_code == 200, "Ошибка: Статус не равен 200"
    print ("Статус код равен 200")



# Тест на создание заказа и получение информации о нём:
def test_get_order_auto():
    # Выполнить запрос на создание заказа и сохранить номер трека.
    order_track = get_order_track()

    # Выполнить запрос на получения заказа по треку и проверить корректный статус кода.
    get_order(order_track)
