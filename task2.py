length = float(input("Enter the length of the lawn (metres): "))
width = float(input("Enter the width of the lawn (metres): "))
area = length * width
seed_required = area * 50
print(f"Grass seed required: {seed_required:.1f} grams")