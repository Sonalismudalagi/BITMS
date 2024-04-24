def print_z_pattern(name):
    n = len(name)
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or i + j == n - 1:
                print(name[i], end='')
            else:
                print(' ', end='')
        print()

name = "SONALI"
print_z_pattern(name)