import math

def calculate_building_height(shadow_length, angle_degrees):
  """
  Вычисляет высоту здания на основе длины тени и угла подъема солнца.

  Args:
    shadow_length: Длина тени, отбрасываемой зданием (в метрах).
    angle_degrees: Угол подъема солнца над горизонтом (в градусах).

  Returns:
    Высота здания (в метрах).
  """

  # Преобразуем угол из градусов в радианы, так как math.tan() принимает радианы.
  angle_radians = math.radians(angle_degrees)

  # Вычисляем высоту здания по формуле: height = shadow_length * tan(angle)
  building_height = shadow_length * math.tan(angle_radians)

  return building_height

# Пример использования функции
shadow_length = 15  # метров
angle_degrees = 40  # градусов

building_height = calculate_building_height(shadow_length, angle_degrees)

print(f"Длина тени: {shadow_length} м")
print(f"Угол подъема солнца: {angle_degrees} °")
print(f"Высота здания: {building_height:.2f} м")