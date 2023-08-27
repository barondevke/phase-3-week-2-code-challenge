# Restaurant Review Management System

The Restaurant Review Management System is a Python program that allows you to manage customer reviews for various restaurants. This system consists of three main classes: Review, Customer, and Restaurant.

## Classes

### Review Class

The Review class represents a customer's review of a restaurant. It has the following attributes and methods:

#### Attributes:

customer_object: The customer who wrote the review.
restaurant_object: The restaurant being reviewed.
customerRating: The rating given by the customer.

#### Methods:

customer(): Returns the full name of the customer.
restaurant(): Returns the name of the restaurant.
rating(): Returns the rating given by the customer.

#### Class Methods:

all(instances): Returns a list of all reviews.

### Customer Class

The Customer class represents a customer who can write reviews and visit restaurants. It has the following attributes and methods:

#### Attributes:

first_name: The first name of the customer.
last_name: The last name of the customer.

#### Methods:

given_name(): Returns the first name of the customer.
family_name(): Returns the last name of the customer.
full_name(): Returns the full name of the customer.
create_review(restaurant, rating): Creates a new review and adds it to the customer's review list.
restaurants(): Returns a list of restaurant names where the customer has written reviews.
num_reviews(): Returns the number of reviews written by the customer.
restaurantVisiting(restaurant): Records that the customer visited a particular restaurant.

#### Class Methods:

find_by_given_name(instances, fullName): Finds a customer's full name based on the given first name.
find_all_by_given_name(instances, fullName): Finds all customer full names based on the given first name.
all(instances): Returns a list of all customer full names.

### Restaurant Class

The Restaurant class represents a restaurant that can receive reviews. It has the following attributes and methods:

#### Attributes:

restaurant_name: The name of the restaurant.

#### Methods:

name(): Returns the name of the restaurant.
addReview(review): Adds a review to the restaurant's review list.
reviews(): Returns a list of ratings given by customers for the restaurant.
customers(): Returns a list of customer objects who reviewed the restaurant.
average_star_rating(): Calculates and returns the average star rating for the restaurant.

## How to use the program:

### Create Customers:

Instantiate Customer objects with their first and last names.
Use the create_review method to have customers write reviews for restaurants.
Record restaurant visits using the restaurantVisiting method.

### Create Restaurants:

Instantiate Restaurant objects with their names.
Reviews can be added to restaurants using the addReview method.
Access Reviews and Information:

Use various methods to access review and information data.
Retrieve all reviews using the all method of the Review class.
Access customer information using methods in the Customer class.
Access restaurant information and review data using methods in the Restaurant class.

#### Summary

The Restaurant Review Management System provides a convenient way to manage customer reviews and restaurant information. It allows you to create customers, write reviews, track restaurant visits, and calculate average ratings.
