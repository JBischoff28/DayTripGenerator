import random

def function_of_lists ():
    global destination_list
    destination_list = ["Newport, RI", "Nashville, TN", "San Diego, CA", "Seattle, WA", "Chicago, IL", "The Bahamas", "Miami, FL", "The Grand Caynon", "Las Vegas, NE", "Scottsdale, AR", "Colorado Springs, CO", "Outter Banks, NC", "Charleston, SC"]
    global restaurant_list
    restaurant_list = ["The Brass", "O'Kelly's Bar & Grill", "Camille's", "Apple Bees", "Buffalo Wild Wings", "Los Paleminos", "Olive Garden", "Starlite", "Max & Emily's", "Jersey Mike's", "Freddie's", "IHOP", "CMU Dining Hall", "Menna's Joint", "Pizza Hut"]
    global list_of_transit
    list_of_transit = ["Bicycle", "Car", "Sports Car", "Public Bus", "Taxi", "Uber", "Skateboard", "Segway", "Moped", "Motorcycle", "Rollerskates", "Trolley", "Walking", "Boat"]
    global entertainment_list
    entertainment_list = ["Concert", "Beach Walk", "Comedy Show", "Mansion Tour", "Shopping", "Beach Volleyball", "Night Club", "Music Festival", "Haunted House", "NBA Game", "Sailing", "Paragliding", "NFL Game", "NHL Game"]

def run ():
    function_of_lists()
    generate_random_destination(destination_list)
    generate_random_restaurant(restaurant_list)
    generate_random_transit(list_of_transit)
    generate_random_entertainment(entertainment_list)
    display_full_trip(random_destination, random_restaurant, random_transit, random_entertainment)
    check_user_satisfaction ()

def display_full_trip (random_destination, random_restaurant, random_transit, random_entertainment):
        print(f"Destination: {random_destination}")
        print(f"Restaurant: {random_restaurant}")
        print(f"Mode of Transportation: {random_transit}")
        print(f"Form of Entertainment: {random_entertainment}")

def generate_random_destination (destination_list):
    global random_destination
    random_destination = random.choice(destination_list)
    return random_destination

def generate_random_restaurant (restaurant_list):
    global random_restaurant
    random_restaurant = random.choice(restaurant_list)
    return random_restaurant

def generate_random_transit (list_of_transit):
    global random_transit
    random_transit = random.choice(list_of_transit)
    return random_transit

def generate_random_entertainment (entertainment_list):
    global random_entertainment
    random_entertainment = random.choice(entertainment_list)
    return random_entertainment

def check_user_satisfaction ():

    global user_satisfaction
    user_satisfaction = input("Are you happy with your trip? Y/N:\n")

    if user_satisfaction == 'Y':
        print("Awesome! Have a safe trip!")
    elif user_satisfaction == 'N':
        run()
    else:
        print("That is not a valid response.\n")
        check_user_satisfaction()

run()