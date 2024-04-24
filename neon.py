def is_neon_number(num):
    square = num * num
    digit_sum = sum(int(digit) for digit in str(square))
    return digit_sum == num

def display_neon_numbers(start, end):
    neon_numbers = [num for num in range(start, end + 1) if is_neon_number(num)]
    print("Neon numbers between", start, "and", end, "are:", neon_numbers)

#start_num = int(input("Enter the starting number: "))
#end_num = int(input("Enter the ending number: "))

display_neon_numbers(1,10)