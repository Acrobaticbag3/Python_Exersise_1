# assignment 6
# convert seconds to hours, minutes, and seconds
def seconds_to_hms(seconds):
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return hours, minutes, seconds


seconds = int(input("Give a number of seconds: "))

# Convert seconds to hours, minutes, and seconds
hours, minutes, remaining_seconds = seconds_to_hms(seconds)

print(f"This corresponds to: {hours} hours, {minutes} minutes, and {remaining_seconds} seconds.")   # noqa: E501
