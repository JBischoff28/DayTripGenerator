import time
import random


def generate_random_destination ():
    destination_list = ["Newport, RI", "Nashville, TN", "San Diego, CA", "Seattle, WA", "Chicago, IL", "The Bahamas", "Miami, FL", "The Grand Caynon", "Las Vegas, NE", "Scottsdale, AR", "Colorado Springs, CO", "Outter Banks, NC", "Charleston, SC"]
    random_destination = random.choice(destination_list)
    print(random_destination)

def generate_random_restaurant ():
    restaurant_list = ["The Brass", "O'Kelly's Bar & Grill", "Camille's", "Apple Bees", "Buffalo Wild Wings", "Los Paleminos", "Olive Garden", "Starlite", "Max & Emily's", "Jersey Mike's", "Freddie's", "IHOP", "CMU Dining Hall", "Menna's Joint", "Pizza Hut"]
    random_restaurant = random.choice(restaurant_list)
    print(random_restaurant)

def generate_random_transit ():
    modes_of_transit = ["Bicycle", "Car", "Sports Car", "Public Bus", "Taxi", "Uber", "Skateboard", "Segway", "Moped", "Motorcycle", "Rollerskates", "Trolley", "Walking", "Boat"]
    random_transit = random.choice(modes_of_transit)
    print(random_transit)