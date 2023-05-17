---
# Chicken Daily Diet Generator

This Python program generates a randomized daily diet for chickens using store-bought food items. The diet is designed to meet the required nutritional values while considering the available food options and their nutritional content.

## Requirements

- Python 3.x

## Usage

1. Clone the repository or download the Python script.

2. Run the script using the Python interpreter: `python chicken_diet_generator.py`.

3. The program will generate a random daily diet for chickens and display the weights of food groups.

4. Modify the code to add or customize food options, adjust nutritional requirements, or make other changes as needed.

## Code Explanation

The program uses the `random` module and a `Food` class to represent food items. Each food item has a name, category, and nutritional values. The available food options are defined as a list of `Food` objects.

The `generate_chicken_diet()` function calculates the nutritional requirements and total weight of the diet. It then randomly selects food items and adjusts their weights to meet the nutritional requirements. The function returns a dictionary representing the daily diet with weights for each food group.

The generated daily diet is printed to the console, displaying the weight of each food group in grams.

## Customization

- To add or modify food options, create new `Food` objects with the desired name, category, and nutritional values. Add them to the `foods` list in the `generate_chicken_diet()` function.

- Adjust the nutritional requirements by modifying the values of `protein_requirement`, `carbohydrate_requirement`, `fat_requirement`, and `vitamin_requirement` variables in the `generate_chicken_diet()` function.

- Modify the total weight of the diet by changing the value of the `total_weight` variable in the `generate_chicken_diet()` function.

## Disclaimer

Please note that the provided nutritional values and percentages are for demonstration purposes only. Actual nutritional requirements for chickens may vary. It is recommended to consult with a poultry nutritionist or veterinarian to determine the accurate nutritional needs for your specific chickens.

