#Докучаев Максим , 29-я когорта, Инженер по тестированию плюс. Дипломный проект
from request import create_order, get_order_by_track

from data import order_body

def test_order_creation_and_tracking():
    # Создание заказа
    create_response = create_order(order_body) # Используем import из data.py
    assert create_response.status_code == 201, "Не удалось создать заказ"

    # Сохранение трек-номера
    track_number = create_response.json().get("track")
    #print("Заказ создан. Номер трека:", track_number)
    assert track_number, "Трек-номер не получен"

    # Получение заказа по трек-номеру
    get_response = get_order_by_track(track_number)
    # Проверка статуса ответа
    assert get_response.status_code == 200, "Заказ не найден"
    #print("Тест успешно пройден. Код 200.")