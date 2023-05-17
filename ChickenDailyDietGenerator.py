import random

class Food:
    def __init__(self, name, category, nutritional_values):
        self.name = name
        self.category = category
        self.nutritional_values = nutritional_values

def generate_chicken_diet():
    # Define the food options available
    foods = [
    Food("Corn", "Grains", {"protein": 8, "carbohydrates": 80, "fats": 4, "vitamins": 8}),
    Food("Wheat", "Grains", {"protein": 13, "carbohydrates": 71, "fats": 2, "vitamins": 14}),
    Food("Soybean Meal", "Grains", {"protein": 47, "carbohydrates": 17, "fats": 2, "vitamins": 1}),
    Food("Barley", "Grains", {"protein": 12, "carbohydrates": 73, "fats": 2, "vitamins": 5}),
    Food("Oats", "Grains", {"protein": 17, "carbohydrates": 66, "fats": 6, "vitamins": 5}),
    Food("Rice", "Grains", {"protein": 7, "carbohydrates": 77, "fats": 2, "vitamins": 1}),
    Food("Cabbage", "Vegetables", {"protein": 1.3, "carbohydrates": 5.8, "fats": 0.1, "vitamins": 29}),
    Food("Carrot", "Vegetables", {"protein": 0.9, "carbohydrates": 9.6, "fats": 0.2, "vitamins": 33}),
    Food("Spinach", "Vegetables", {"protein": 2.9, "carbohydrates": 3.6, "fats": 0.4, "vitamins": 28}),
    Food("Kale", "Vegetables", {"protein": 2.9, "carbohydrates": 5.6, "fats": 0.6, "vitamins": 49}),
    Food("Apple", "Fruits", {"protein": 0.3, "carbohydrates": 13.8, "fats": 0.4, "vitamins": 2}),
    Food("Banana", "Fruits", {"protein": 1.1, "carbohydrates": 22, "fats": 0.2, "vitamins": 20}),
    Food("Berries", "Fruits", {"protein": 0.7, "carbohydrates": 14, "fats": 0.3, "vitamins": 25}),
    Food("Tomato", "Fruits", {"protein": 0.9, "carbohydrates": 3.9, "fats": 0.2, "vitamins": 20}),
    Food("Chicken Breast", "Meat", {"protein": 31, "carbohydrates": 0, "fats": 4, "vitamins": 0}),
    Food("Fish", "Meat", {"protein": 22, "carbohydrates": 0, "fats": 6, "vitamins": 0}),
    Food("Insects", "Meat", {"protein": 60, "carbohydrates": 10, "fats": 20, "vitamins": 5}),
    Food("Beef", "Meat", {"protein": 26, "carbohydrates": 0, "fats": 17, "vitamins": 0}),
    Food("Lamb", "Meat", {"protein": 25, "carbohydrates": 0, "fats": 20, "vitamins": 0}),
    Food("Pork", "Meat", {"protein": 21, "carbohydrates": 0, "fats": 6, "vitamins": 0}),
    Food("Turkey", "Meat", {"protein": 29, "carbohydrates": 0, "fats": 1, "vitamins": 0}),
    Food("Duck", "Meat", {"protein": 24, "carbohydrates": 0, "fats": 15, "vitamins": 0}),
    Food("Egg", "Meat", {"protein": 13, "carbohydrates": 1, "fats": 11, "vitamins": 0}),
    Food("Cheese", "Dairy", {"protein": 25, "carbohydrates": 1, "fats": 33, "vitamins": 0}),
    Food("Yogurt", "Dairy", {"protein": 9, "carbohydrates": 6, "fats": 4, "vitamins": 0}),
    Food("Milk", "Dairy", {"protein": 3, "carbohydrates": 5, "fats": 3, "vitamins": 0}),
    Food("Grasshoppers", "Insects", {"protein": 20, "carbohydrates": 6, "fats": 6, "vitamins": 0}),
    Food("Mealworms", "Insects", {"protein": 20, "carbohydrates": 14, "fats": 17, "vitamins": 0}),
    Food("Crickets", "Insects", {"protein": 21, "carbohydrates": 8, "fats": 6, "vitamins": 0}),
    Food("Black Soldier Fly Larvae", "Insects", {"protein": 43, "carbohydrates": 28, "fats": 35, "vitamins": 0}),
    Food("Earthworms", "Insects", {"protein": 20, "carbohydrates": 9, "fats": 6, "vitamins": 0}),
    Food("Mealworm Beetles", "Insects", {"protein": 20, "carbohydrates": 14, "fats": 19, "vitamins": 0}),
    Food("Snails", "Insects", {"protein": 16, "carbohydrates": 2, "fats": 0, "vitamins": 0}),
    Food("Crabs", "Seafood", {"protein": 18, "carbohydrates": 0, "fats": 2, "vitamins": 0}),
    Food("Shrimp", "Seafood", {"protein": 24, "carbohydrates": 1, "fats": 1, "vitamins": 0}),
    Food("Squid", "Seafood", {"protein": 20, "carbohydrates": 4, "fats": 1, "vitamins": 0})
]


    diet = {
        "Grains": 0,
        "Vegetables": 0,
        "Fruits": 0,
        "Meat": 0,
        "Dairy": 0,
        "Insects": 0,
        "Seafood": 0
    }

    # Calculate the nutritional requirements
    protein_requirement = 18
    carbohydrate_requirement = 60
    fat_requirement = 5
    vitamin_requirement = 17

    total_weight = 100  # Total weight of the diet (assumed 100 grams for simplicity)

    # Generate the diet by randomly selecting foods and adjusting weights to meet nutritional requirements
    remaining_weight = total_weight
    while remaining_weight > 0:
        # Randomly select a food from the available options
        food = random.choice(foods)

        # Calculate the weight based on the nutritional requirements and the food's nutritional values
        weight = min(remaining_weight,
                     total_weight * food.nutritional_values["protein"] / protein_requirement,
                     total_weight * food.nutritional_values["carbohydrates"] / carbohydrate_requirement,
                     total_weight * food.nutritional_values["fats"] / fat_requirement,
                     total_weight * food.nutritional_values["vitamins"] / vitamin_requirement)

        # Update the diet dictionary with the selected food and weight
        diet[food.category] += weight
        remaining_weight -= weight

    return diet

# Generate a random chicken diet
daily_diet = generate_chicken_diet()

# Print the daily diet
for food_group, weight in daily_diet.items():
    print(f"{food_group}: {weight:.2f}g")
