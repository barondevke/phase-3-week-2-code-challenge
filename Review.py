class Review:
    reviews = []

    def __init__(self, customer_object,restaurant_object,rating):
        self.customer_object = customer_object
        self.restaurant_object = restaurant_object
        self.customerRating = rating
        Review.reviews.append({
            "customerName":self.customer_object.full_name(),
            "restaurantName":self.restaurant_object.restaurant_name,
            "rating":self.customerRating
            })

    def customer(self):
        return self.customer_object.full_name()
    
    def restaurant(self):
        return self.restaurant_object.restaurant_name
    
    def rating(self):
        return self.customerRating


    @classmethod
    def all(instances):
        return instances.reviews     


class Customer:
    customer_instances = []

    def __init__(self,first_name,last_name ):
        self.first_name = first_name
        self.last_name = last_name
        Customer.customer_instances.append(self)
        self.reviews = []
        self.restaurantsVisited = []

    def given_name(self):
        return self.first_name
    
    def family_name(self):
        return self.last_name


    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def create_review(self,restaurant,rating):
        review = Review(self,restaurant,rating)
        self.reviews.append(review)
        restaurant.addReview(review)

    def restaurants(self):
        return[x.restaurant_object.restaurant_name for x in self.reviews]
    
    def num_reviews(self):
        return len(self.reviews)
    
    def restaurantVisiting(self,restaurant):
        self.restaurantsVisited.append(restaurant)
    @classmethod
    def find_by_given_name(instances,fullName):
         for customer in instances.customer_instances:
            if customer.given_name() == fullName:
                return customer.full_name()
            else:
                return None  

      
    @classmethod
    def find_all_by_given_name(instances,fullName):
         customerList = []
         for customer in instances.customer_instances:
            if customer.given_name() == fullName:
                customerList.append(customer.full_name())

            return customerList        
    
    @classmethod
    def all(instances):
        return [x.full_name() for x in instances.customer_instances]
    
    

class Restaurant:

    def __init__(self,restaurant_name):
        self.restaurant_name = restaurant_name
        self.reviewsList = []
        
       

    def name(self):
        return self.restaurant_name   
    
    def addReview(self,review):
        self.reviewsList.append(review)

    def reviews(self):
        return [x.customerRating for x in self.reviewsList]

    def customers(self):
        return [x.customer_object for x in self.reviewsList]


    def average_star_rating(self):
        if self.reviewsList == 0:
            return 0
        else:
            total = 0
            for x in self.reviewsList:
                total+=x.customerRating
            return total/len(self.reviewsList)    




restaurant1 = Restaurant('Shosho')
customer1 = Customer('Steve','Ndaba')
customer2 = Customer('Often', 'Often')
review1 = Review(customer1,restaurant1,5)
customer2.create_review(restaurant1,7)




print(review1.rating())
print(Review.all())
print(review1.customer())
print(review1.restaurant())

        
print(restaurant1.average_star_rating())
print(restaurant1.reviews())