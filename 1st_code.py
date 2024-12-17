def calculate_sum(numbers):
    total = sum(numbers)  
    return total

def calculate_average(numbers):
    total = calculate_sum(numbers)
    average = total / len(numbers)  
    return average

def main():
    num_list = [10, 20, 30, 40, 50]
    sum_result = calculate_sum(num_list)
    average_result = calculate_average(num_list)
    print("Sum of numbers:", sum_result)
    print("Average of numbers:", averge_result)  

# Call the main function
main()