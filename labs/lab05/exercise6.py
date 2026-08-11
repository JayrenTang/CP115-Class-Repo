time = int(input("Time (minutes): "))
print("\n")

hours = time // 60
minutes = time % 60

print("Original Time: ", time, "minutes")
print("Converted Time: ", hours, "hours", minutes, "minutes")
