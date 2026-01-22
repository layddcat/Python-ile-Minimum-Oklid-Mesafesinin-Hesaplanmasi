points = [(2, 3), (5, 1), (0, 0), (-1, 5), (3, 2)]

def calculateEuclideanDistance(point1, point2):

    x1, y1 = point1
    x2, y2 = point2
    
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return distance

distances = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        point1 = points[i]
        point2 = points[j]
        distance = calculateEuclideanDistance(point1, point2)
        distances.append(distance)

min_distance = min(distances)
print("Minimum Mesafe:", min_distance)
