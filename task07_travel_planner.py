
Destination = input("What is your destination: ")
Distance = int(input("How far it is in kilo meters: "))
Speed = int(input("Average speed in kilo meter per hour: "))

Time = Distance/Speed

print(f"Destination: {Destination}")
print(f"Distance: {Distance}km")
print(f"Average Speed: {Speed}km/h")

print(f"Estimated Travel Time: {Time}")

Time_inminutes = Distance/(Speed*60)

print(f"Estimated Travel Time in km/min: {Time_inminutes}")