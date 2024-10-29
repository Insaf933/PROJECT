class Driver:
    def __init__(self, id, name, start_city):
        self.id = id
        self.name = name
        self.start_city = start_city

class City:
    def __init__(self, name, neighbors):
        self.name = name
        self.neighbors = neighbors

class Best_Delivery:
    def __init__(self):
        self.drivers = []
        self.cities = {}
        self.driver_id_counter = 1

    def view_all_drivers(self):
        for driver in self.drivers:
            print(f"{driver.id}, {driver.name}, {driver.start_city}")

    def show_cities(self):
        for city in sorted(self.cities.keys(), reverse=True):
            print(city)

    def search_city(self, key):
        for city in self.cities:
            if key in city:
                print(city)

    def check_similar_drivers(self):
        for city, drivers in self.group_drivers_by_city().items():
            print(f"{city}: {', '.join([driver.name for driver in drivers])}")

    def group_drivers_by_city(self):
        grouped_drivers = {}
        for driver in self.drivers:
            grouped_drivers.setdefault(driver.start_city, []).append(driver)
        return grouped_drivers
    def add_city(self, city_name):
        self.cities[city_name] = []
    def add_neighbor(self, city1, city2):
        self.cities[city1].append(city2)
        self.cities[city2].append(city1)
    def add_driver(self, name, start_city):
        if start_city not in self.cities:
            self.add_city(start_city)
        new_driver = Driver(f"ID{self.driver_id_counter}", name, start_city)
        self.drivers.append(new_driver)
        self.driver_id_counter += 1

    def print_neighboring_cities(self, city_name):
        if city_name in self.cities:
            print(self.cities[city_name])

    def print_drivers_delivering_to_city(self, city_name):
        def bfs(start_city):
            visited = set()
            queue = [start_city]
            while queue:
                current_city = queue.pop(0)
                if current_city == city_name:
                    return True
                visited.add(current_city)
                for neighbor in self.cities[current_city]:
                    if neighbor not in visited:
                        queue.append(neighbor)
            return False

        for driver in self.drivers:
            if bfs(driver.start_city):
                print(driver.id, driver.name)
system = Best_Delivery()
while True:
    print("Hello! Please enter:")
    print("1. To go to the drivers' menu")
    print("2. To go to the cities' menu")
    print("3. To exit the system")
    choice = int(input())

    if choice == '1':
        while True:
            print("DRIVERS' MENU")
            print("Enter:")
            print("1. To view all the drivers")
            print("2. To add a driver")
            print("3. Check similar drivers")
            print("4. To go back to the main menu")
            choice = int(input())

            if choice == '1':
                system.view_all_drivers()
            elif choice == '2':
                name = input("Enter driver name: ")
                start_city = input("Enter driver's start city: ")
                system.add_driver(name, start_city)
            elif choice == '3':
                system.check_similar_drivers()
            elif choice == '4':
                break
            else:
                print("Invalid choice")

    elif choice == '2':
        while True:
            print("CITIES' MENU")
            print("Enter:")
            print("1. Show cities")
            print("2. Search city")
            print("3. Print neighboring cities")
            print("4. Print Drivers delivering to city")
            print("5. To go back to the main menu")
            choice = int(input())

            if choice == '1':
                system.show_cities()
            elif choice == '2':
                key = input("Enter search key: ")
                system.search_city(key)
            elif choice == '3':
                city_name = input("Enter city name: ")
                system.print_neighboring_cities(city_name)
            elif choice == '4':
                city_name = input("Enter city name: ")
                system.print_drivers_delivering_to_city(city_name)
            elif choice == '5':
                break
            else:
                print("Invalid choice")

    elif choice == '3':
        break
    else:
        print("Invalid choice")




