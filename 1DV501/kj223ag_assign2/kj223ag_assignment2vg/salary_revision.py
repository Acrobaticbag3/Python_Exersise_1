def calculate_statistics(salaries):
    # Calculate the average salary
    total_salary = sum(salaries)
    average_salary = total_salary // len(salaries)

    # Sort the salaries
    sorted_salaries = sorted(salaries)

    # Calculate the median salary
    middle_index = len(sorted_salaries) // 2
    if len(sorted_salaries) % 2 == 0:
        median_salary = (sorted_salaries[middle_index - 1] + sorted_salaries[middle_index]) // 2
    else:
        median_salary = sorted_salaries[middle_index]

    # Calculate the salary gap
    salary_gap = sorted_salaries[-1] - sorted_salaries[0]

    return average_salary, median_salary, salary_gap


input_salaries = input("Provide salaries (space-separated integers): ").strip().split()
salaries = [int(s) for s in input_salaries]

average_salary, median_salary, salary_gap = calculate_statistics(salaries)

print(f"Median: {median_salary}")
print(f"Average: {average_salary}")
print(f"Gap: {salary_gap}")
