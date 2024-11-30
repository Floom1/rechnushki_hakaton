import folium
import json
from openrouteservice import Client

# Укажите ваш API-ключ OpenRouteService
ORS_API_KEY = "5b3ce3597851110001cf62487dfe3169cbe241c29cdd8d2e62f7bc1a"

def display_docks_map_from_geojson(geojson_data, output_file="map.html"):
    """
    Отображает карту с точками доступных мест на основе GeoJSON.

    :param geojson_data: Объект GeoJSON или путь к файлу GeoJSON.
    :param output_file: Имя файла для сохранения карты.
    """
    # Устанавливаем клиента OpenRouteService
    client = Client(key=ORS_API_KEY)

    route = [41, 188, 42, 43, 44, 187, 146]

    # Если передан путь к файлу GeoJSON, читаем его
    if isinstance(geojson_data, str):
        with open('C:/Code/Python/django_5/rechnushki_hakaton/rivers/static/maps/hahatoon.geojson', 'r', encoding='utf-8') as file:
            geojson_data = json.load(file)

    # Проверка на валидность GeoJSON
    if "features" not in geojson_data:
        raise ValueError("Неверный формат GeoJSON.")

    # Извлечение координат, имени и адреса из GeoJSON
    coordinates = []
    for feature in geojson_data["features"]:
        if feature["geometry"]["type"] == "Point" and feature["properties"]["id"] in route:
            lat, lon = feature["geometry"]["coordinates"]
            name = feature["properties"].get("name", "Без названия")
            address = feature["properties"].get("address", "Адрес не указан")
            coordinates.append((lon, lat, name, address))

    if not coordinates:
        raise ValueError("В GeoJSON не найдены точки.")

    # Создаем карту, центрированную на первой точке
    map_center = coordinates[0][1], coordinates[0][0]  # Сначала широта, затем долгота
    map_object = folium.Map(location=map_center, zoom_start=13)

    # Добавляем точки на карту с названием и адресом
    for idx, (lon, lat, name, address) in enumerate(coordinates):
        folium.Marker(
            location=[lat, lon],
            popup=f"<b>{name}</b><br>{address}"
        ).add_to(map_object)

    # Сохраняем карту в HTML-файл
    map_object.save(output_file)
    print(f"Карта сохранена в файл: {output_file}")

# Пример использования
if __name__ == "__main__":
    # Пример GeoJSON-данных


    # Сохранение карты с использованием объекта GeoJSON
    output_file = "docks_map1.html"
    display_docks_map_from_geojson('hahatoon.geojson', output_file)

    # Сообщение пользователю
    print(f"Откройте файл {output_file} в браузере для просмотра карты.")
