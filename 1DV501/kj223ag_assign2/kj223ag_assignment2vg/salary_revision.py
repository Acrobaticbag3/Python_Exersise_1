# assignment 20

# calculate statistics for a list of salaries
def calculate_statistics(salaries):
    total_salary = sum(salaries)

    # calculate the average salary
    average_salary = total_salary // len(salaries)

    # sort list of salaries
    sorted_salaries = sorted(salaries)

    # calculate median salary
    middle_index = len(sorted_salaries) // 2

    # check if the number of salaries is even
    if len(sorted_salaries) % 2 == 0:
        median_salary = (sorted_salaries[middle_index - 1] + sorted_salaries[middle_index]) // 2
    else:
        median_salary = sorted_salaries[middle_index]

    salary_gap = sorted_salaries[-1] - sorted_salaries[0]

    # return the calculated average, median, and salary
    return average_salary, median_salary, salary_gap


# get salaries as input from user
input_salaries = input("Provide salaries (space-separated integers): ").strip().split()
salaries = [int(s) for s in input_salaries]

# calculate the statistics
average_salary, median_salary, salary_gap = calculate_statistics(salaries)

# print the results
print(f"Median: {median_salary}")
print(f"Average: {average_salary}")
print(f"Gap: {salary_gap}")
