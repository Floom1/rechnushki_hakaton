import folium
from openrouteservice import Client

ORS_API_KEY = "5b3ce3597851110001cf62487dfe3169cbe241c29cdd8d2e62f7bc1a"

def display_multiple_routes_on_map(coords_list, output_file="route_map.html"):
    client = Client(key=ORS_API_KEY)

    map_center = coords_list[0][0]
    map_object = folium.Map(location=[map_center[1], map_center[0]], zoom_start=13)

    for idx, (start_coords, end_coords) in enumerate(coords_list, start=1):
        try:
            route = client.directions(
                coordinates=[start_coords, end_coords],
                profile='foot-walking',
                format='geojson'
            )

            # Добавление маршрута на карту
            folium.GeoJson(route, name=f"Маршрут {idx}").add_to(map_object)

            # Добавление начальной и конечной точек
            folium.Marker(
                location=[start_coords[1], start_coords[0]],
                popup=f"Начальная точка {idx}",
                icon=folium.Icon(color="green")
            ).add_to(map_object)

            folium.Marker(
                location=[end_coords[1], end_coords[0]],
                popup=f"Конечная точка {idx}",
                icon=folium.Icon(color="red")
            ).add_to(map_object)

        except Exception as e:
            print(f"Ошибка при получении маршрута {idx}: {e}")

    # Сохранение карты в файл
    map_object.save(output_file)
    print(f"Карта с маршрутами сохранена в файл: {output_file}")

# Пример использования
if __name__ == "__main__":
    # Координаты для двух маршрутов: [(start1, end1), (start2, end2)]
    coords_list = [
        ((37.597100, 55.73013 ), (37.597184, 55.73813)),
        ((37.590694, 55.756427), (37.598984, 55.73833))
    ]

    display_multiple_routes_on_map(coords_list, "multiple_routes_map.html")
