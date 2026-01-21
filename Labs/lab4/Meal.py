class Meal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Chef:
    def make_Meal(self, meal_name):
        return Meal(meal_name)

if __name__ == "__main__":
    order = input("Enter the meal: ")
    meal = Meal(order)

    print(f"The chef has prepared: {meal.get_name()}")

