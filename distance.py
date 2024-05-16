# 1- Noktaları temsil eden demetleri içeren 'points' adında bir liste oluşturuyoruz
points = [(2, 3), (5, 1), (0, 0), (-1, 5), (3, 2)]

# 2- İki nokta arasındaki Öklid mesafesini hesaplayan fonksiyonu tanımlıyoruz
def calculateEuclideanDistance(point1, point2):

    # Noktaların x ve y koordinatlarını alıyoruz
    x1, y1 = point1
    x2, y2 = point2
    
    # Öklid mesafesini hesaplıyoruz
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return distance

# 3- Her bir nokta çifti için Öklid mesafesini hesaplayıp 'distances' adında bir liste oluşturuyoruz
distances = []
# 4- Her nokta çiftini karşılaştırmak için iki döngü kullanıyoruz
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        point1 = points[i]
        point2 = points[j]
        # Her iki nokta için Öklid mesafesini hesaplayıp 'distances' listesine ekliyoruz
        distance = calculateEuclideanDistance(point1, point2)
        distances.append(distance)

# 5- 'distances' listesinden minimum mesafeyi buluyoruz
min_distance = min(distances)
print("Minimum Mesafe:", min_distance)