# Base class for Superheroes
class Superhero:
    def __init__(self, name, power_level, alias):
        self._name = name              # Private attribute: real name
        self._power_level = power_level  # Private attribute: power level (1-100)
        self._alias = alias            # Private attribute: superhero alias

    # Getter for name
    def get_name(self):
        return self._name

    # Setter for power_level with validation
    def set_power_level(self, power_level):
        if 1 <= power_level <= 100:
            self._power_level = power_level
        else:
            print(f"Invalid power level for {self._alias}. Must be between 1 and 100.")

    # Getter for power_level
    def get_power_level(self):
        return self._power_level

    # Getter for alias
    def get_alias(self):
        return self._alias

    # Method to display superhero info
    def display_info(self):
        return f"Alias: {self._alias}, Name: {self._name}, Power Level: {self._power_level}"

    # Abstract-like move method (to be overridden by subclasses)
    def move(self):
        pass  # Polymorphic method, defined in subclasses

# Derived class for flying superheroes
class FlyingSuperhero(Superhero):
    def __init__(self, name, power_level, alias, flight_speed):
        super().__init__(name, power_level, alias)  # Call parent constructor
        self._flight_speed = flight_speed           # Additional attribute: flight speed (km/h)

    # Getter for flight_speed
    def get_flight_speed(self):
        return self._flight_speed

    # Polymorphic move method
    def move(self):
        return f"{self._alias} is flying at {self._flight_speed} km/h! ✈️"

# Derived class for speedster superheroes
class SpeedsterSuperhero(Superhero):
    def __init__(self, name, power_level, alias, run_speed):
        super().__init__(name, power_level, alias)  # Call parent constructor
        self._run_speed = run_speed                # Additional attribute: running speed (km/h)

    # Getter for run_speed
    def get_run_speed(self):
        return self._run_speed

    # Polymorphic move method
    def move(self):
        return f"{self._alias} is running at super speed of {self._run_speed} km/h! 🏃"

# Main program to demonstrate the classes
def main():
    # Create instances of superheroes
    superman = FlyingSuperhero("Clark Kent", 95, "Superman", 1000)
    flash = SpeedsterSuperhero("Barry Allen", 85, "The Flash", 1200)

    # List to demonstrate polymorphism
    heroes = [superman, flash]

    # Display info and movement for each superhero
    for hero in heroes:
        print(hero.display_info())
        print(hero.move())
        print()  # Blank line for readability

    # Demonstrate encapsulation: Update power level
    print("Updating Superman's power level...")
    superman.set_power_level(98)
    print(superman дисплей_info())

    # Demonstrate invalid power level
    print("\nTrying invalid power level for Flash...")
    flash.set_power_level(150)

if __name__ == "__main__":
    main()