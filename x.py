def display_name_in_x_pattern(name):
    n = len(SONALI)
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                print(name[i], end=" ")
            else:
                print(" ", end=" ")
        print()
