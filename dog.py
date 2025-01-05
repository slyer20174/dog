# Define the Dog class
class Dog:
    # Class variable
    species = "Canis lupus familiaris"  # All dogs belong to this species
    
    def __init__(self, name, breed, age):
        # Instance variables
        self.name = name
        self.breed = breed
        self.age = age
    
    # Method to display dog details
    def display_details(self):
        print(f"Dog's Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Age: {self.age} years old")
        print(f"Species: {Dog.species}")
        print("-" * 30)

# Main function to create and display dog objects
def main():
    # Create Dog objects for different breeds
    dog1 = Dog("Buddy", "Golden Retriever", 3)
    dog2 = Dog("Max", "Bulldog", 5)

    # Display details of both dogs
    print("Details of Dog 1:")
    dog1.display_details()

    print("Details of Dog 2:")
    dog2.display_details()

if __name__ == "__main__":
    main()