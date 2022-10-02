import random

destination_list = ["Newport, RI", "Nashville, TN", "San Diego, CA", "Seattle, WA", "Chicago, IL", "The Bahamas", "Miami, FL", "The Grand Caynon", "Las Vegas, NE", "Scottsdale, AR", "Colorado Springs, CO", "Outter Banks, NC", "Charleston, SC"]
restaurant_list = ["The Brass", "O'Kelly's Bar & Grill", "Camille's", "Apple Bees", "Buffalo Wild Wings", "Los Paleminos", "Olive Garden", "Starlite", "Max & Emily's", "Jersey Mike's", "Freddie's", "IHOP", "CMU Dining Hall", "Menna's Joint", "Pizza Hut"]
list_of_transit = ["Bicycle", "Car", "Sports Car", "Public Bus", "Taxi", "Uber", "Skateboard", "Segway", "Moped", "Motorcycle", "Rollerskates", "Trolley", "Walking", "Boat"]
entertainment_list = ["Concert", "Beach Walk", "Comedy Show", "Mansion Tour", "Shopping", "Beach Volleyball", "Night Club", "Music Festival", "Haunted House", "NBA Game", "Sailing", "Paragliding", "NFL Game", "NHL Game"]

def run ():
    random_destination_pick = generate_random_destination(destination_list)
    random_restaurant_pick = generate_random_restaurant(restaurant_list)
    random_transit_pick = generate_random_transit(list_of_transit)
    random_entertainment_pick = generate_random_entertainment(entertainment_list)
    display_full_trip(random_destination_pick, random_restaurant_pick, random_transit_pick, random_entertainment_pick)
    check_user_satisfaction ()

def display_full_trip (random_destination_pick, random_restaurant_pick, random_transit_pick, random_entertainment_pick):
        print(f"Destination: {random_destination_pick}")
        print(f"Restaurant: {random_restaurant_pick}")
        print(f"Mode of Transportation: {random_transit_pick}")
        print(f"Form of Entertainment: {random_entertainment_pick}")

def generate_random_destination (destination_list):
    random_destination = random.choice(destination_list)
    return random_destination

def generate_random_restaurant (restaurant_list):
    random_restaurant = random.choice(restaurant_list)
    return random_restaurant

def generate_random_transit (list_of_transit):
    random_transit = random.choice(list_of_transit)
    return random_transit

def generate_random_entertainment (entertainment_list):
    random_entertainment = random.choice(entertainment_list)
    return random_entertainment

def check_user_satisfaction ():
    user_satisfaction = input("Are you happy with your trip?:\n")

    if user_satisfaction == 'Y':
        print("Awesome! Have a safe trip!")
    elif user_satisfaction == 'N':
        print("Standby while I generate a new trip.")
    else:
        print("That is not a valid response.\n")
        check_user_satisfaction()


run()