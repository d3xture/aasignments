COULOMBS_CONSTANT = 8.988e9


def calculate_charge_q2(force, distance_squared, charge_q1):

    charge_q2 = force * distance_squared / (COULOMBS_CONSTANT * charge_q1)

    return charge_q2


force = float(input("Enter the force between the particles (N): "))
distance_squared = float(input("Enter the square of the distance between the particles (m^2): "))
charge_q1 = float(input("Enter the charge of particle 1 (C): "))

charge_q2 = calculate_charge_q2(force, distance_squared, charge_q1)

print(f"The charge of particle 2 is: {charge_q2:.2e} C")