COULOMBS_CONSTANT = 8.988e9


def calculate_charge_q2(force, distance_squared, charge_q1):

    charge_q2 = force * distance_squared / (COULOMBS_CONSTANT * charge_q1)

    return charge_q2


force = float(input("Enter the force between the particles (N): "))
distance_squared = float(input("Enter the square of the distance between the particles (m^2): "))
charge_q1 = float(input("Enter the charge of particle 1 (C): "))

charge_q2 = calculate_charge_q2(force, distance_squared, charge_q1)

print(f"The charge of particle 2 is: {charge_q2:.2e} C")

//////////////////////

F = float(input("Enter the value of F"))
r_square = float(input("Enter the value of r"))
K = float(input("Enter the value of K"))
q1 = float(input("Enter the value of q1"))

print("According to the problem number 32, we will using formula \n F = K q1q1/r^2")
print("Since, we want to find q2, so q2 will be equal to Fr^2/kq1")

q2 = (F * (r_square*2)) / (K * q1)

print(f"so, the final answer will be {q2}")
