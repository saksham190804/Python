def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def can_measure_water(jug1, jug2, target):
    return target <= jug1 + jug2 and target % gcd(jug1, jug2) == 0

def measure_water(jug1_capacity, jug2_capacity, target):
    if can_measure_water(jug1_capacity, jug2_capacity, target):
        return True

    if target <= jug1_capacity:
        jug2_capacity -= jug1_capacity - target
        return can_measure_water(jug1_capacity, jug2_capacity, 0)

    return False

# Given jug capacities
jug1_capacity = 3
jug2_capacity = 4
target = 2

# Measure water
if measure_water(jug1_capacity, jug2_capacity, target):
    print("It is possible to measure exactly 2 liters of water in the 4-liter jug.")
else:
    print("It is not possible to measure exactly 2 liters of water in the 4-liter jug.")
