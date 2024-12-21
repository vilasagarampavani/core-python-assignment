def calculate_fare(distance):
    base_fare = 50
    distance_fare = 10
    total_fare = base_fare + (distance * distance_fare)
    return total_fare

num_trips = input("Enter distances for trips in list format: ")
distances = eval(num_trips)

total_fare = 0

for i, distance in enumerate(distances, start=1):
    fare = calculate_fare(distance)
    print(f"Trip {i}: ${fare}")
    total_fare += fare

print(f"Total Fare: ${total_fare}")
