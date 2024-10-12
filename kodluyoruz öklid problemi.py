import math

# 1. Noktaların Tanımlanma
points = [(1, 2), (4, 6), (3, 1), (5, 5)]

# 2. Öklid Mesafesi hesaplama
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

# 3. Listedeki Mesafelerin Hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):  # Her nokta çiftini al
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# 4. Minimum Mesafeyi bulma
min_distance = min(distances)

# Sonuc
print(f"Noktalar: {points}")
print(f"Mesafeler: {distances}")
print(f"Minimum mesafe: {min_distance}")
