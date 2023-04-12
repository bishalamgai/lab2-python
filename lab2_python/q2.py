def get_positive_input(prompt):
   
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")


def print_species_data(starting_species, avg_daily_increase, num_days):

    print(f"  1                         {starting_species}")
     
    current_species = starting_species
    for day in range(2, num_days + 1):
        current_species += current_species * avg_daily_increase / 100
        print(f" {day:2}                         {int(current_species)}")


# input
starting_species = get_positive_input("Starting number of organisms: ")
avg_daily_increase = get_positive_input("Average daily percentage increase: ")
num_days = get_positive_input("Enter the number of days to display the final data: ")

# Print
print("Day Approximate            Population")
print("-------------------------------------")
print_species_data(starting_species, avg_daily_increase, num_days)
