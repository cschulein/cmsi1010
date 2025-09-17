def print_triangle(character, lines):
    for count in range(1, lines + 1):
        print(character * count)

print_triangle(character="@", lines=8)
print_triangle(character=".", lines=55)
print_triangle(character="o", lines=5)