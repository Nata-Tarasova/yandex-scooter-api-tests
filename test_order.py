# Наталья Тарсова, 43-я когорта, Финальный проект, Инженер по тестированию плюс

import sender_stand_request

def test_get_order_by_track_success():
    # Шаг 1: Выполняю запрос на создание заказа через изолированную функцию
    response_create = sender_stand_request.post_new_order()
    
    # Шаг 2: Получаю и сохраняю номер трека заказа
    track_number = response_create.json()["track"]
    
    # Шаг 3: Выполняю запрос на получение заказа по треку
    response_get = sender_stand_request.get_order_by_track(track_number)
    
    # Шаг 4: Проверяю ОДНО конкретное действие (информация о заказе успешно получена) — статус ответа равен 200
    assert response_get.status_code == 200
