# Наталья Тарасова, 43-я когорта, Финальный проект, Инженер по тестированию плюс

import requests
import configuration
import data

def test_create_and_get_order_by_track():
    # Шаг 1: Выполняю запрос на создание заказа (берём headers и json из data.py)
    response_create = requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=data.order_body,
        headers=data.headers
    )
    
    # Проверяю, что заказ создался успешно (код 201)
    assert response_create.status_code == 201
    
    # Шаг 2: Сохраняю номер трека заказа
    track_number = response_create.json()["track"]
    print(f"\n[INFO] Заказ создан. Сохранен трек-номер: {track_number}")
    
    # Шаг 3: Выполняю запрос на получение заказа по треку
    response_get = requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
        params={"t": track_number},
        headers=data.headers
    )
    
    # Шаг 4: Проверяю, что код ответа равен 200
    assert response_get.status_code == 200
    print(f"[INFO] Данные по треку получены успешно. Статус ответа: {response_get.status_code}")
