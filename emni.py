talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

total_lots = talents * 20 * 32 + pounds * 32 + lots
grams = total_lots * 13.3

kilograms = int(grams // 1000)
remaining_grams = grams % 1000

print("The weight in modern units:")
print(f"{kilograms