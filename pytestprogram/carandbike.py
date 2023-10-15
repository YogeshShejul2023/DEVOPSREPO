BIKE_RATE_PER_HOUR = 10  # Rs per hour for bikes
CAR_RATE_PER_HOUR = 20   # Rs per hour for cars
HOURS_PER_DAY = 6        # Number of hours the parking lot is open
PROFIT_LIMIT = 10000 # Threshold for a profitable day

# Input: Number of cars and bikes
num_cars = int(input("Enter the number of cars: "))
num_bikes = int(input("Enter the number of bikes: "))

# Calculate the total collection for the day
total_collection = (num_cars * CAR_RATE_PER_HOUR + num_bikes * BIKE_RATE_PER_HOUR) * HOURS_PER_DAY

# Determine if it's a profitable day or not
if total_collection >= PROFIT_LIMIT:
    print("It's a good day! Total collection for the day: Rs", total_collection)
else:
    print("It's a bad day. Total collection for the day: Rs", total_collection)