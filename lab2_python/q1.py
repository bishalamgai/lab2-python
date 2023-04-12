#Enter the number of years
num_years = int(input("Enter the number of years: "))

# Storing rainfall data for each year
total_rainfall_per_year = []
avg_monthly_rainfall_per_year = []

# Loop through each year
for year in range(1, num_years + 1):
    #Variable to store total rainfall for this year
    total_rainfall = 0

    #Store monthly rainfall data for this year
    monthly_rainfall = []

    # Loop through each month
    for month in range(1, 13):
        #Enter rainfall amount for this month
        rainfall_cm = float(input("Enter the rainfall amount for the Month- ".format(month)))
        
        # Add rainfall amount to monthly data list
        monthly_rainfall.append(rainfall_cm)
        
        # Add rainfall amount to total for this year
        total_rainfall += rainfall_cm
    
    # Add total rainfall for this year to list of yearly totals
    total_rainfall_per_year.append(total_rainfall)
    
    # Calculate average monthly rainfall
    avg_monthly_rainfall = total_rainfall / 12
    
    # Add average monthly rainfall for this year to list of yearly averages
    avg_monthly_rainfall_per_year.append(avg_monthly_rainfall)

# Print results
for year in range(1, num_years + 1):
    print(f"\nTotal Rainfall: {total_rainfall_per_year[year-1]:.2f} cm")
    print(f" Average Monthly Rainfall: {avg_monthly_rainfall_per_year[year-1]:.2f} cm")
