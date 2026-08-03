"""
====================================================
Electrochemistry Python
Nernst Equation Calculator
Author: aroojresearch
====================================================

This module calculates the electrode potential using
the Nernst Equation.

Formula:

E = E0 - (RT / nF) * ln(Q)

Where:
E   = Electrode Potential (V)
E0  = Standard Electrode Potential (V)
R   = Universal Gas Constant
T   = Temperature (K)
n   = Number of electrons transferred
F   = Faraday Constant
Q   = Reaction Quotient

====================================================
"""

import math

# Constants
R = 8.314462618      # J/mol·K
F = 96485.33212      # C/mol


def nernst_equation(E0, temperature, electrons, reaction_quotient):
    """
    Calculate electrode potential using the Nernst Equation.

    Parameters
    ----------
    E0 : float
        Standard electrode potential (V)

    temperature : float
        Temperature (Kelvin)

    electrons : int
        Number of electrons transferred

    reaction_quotient : float
        Reaction quotient (Q)

    Returns
    -------
    float
        Electrode potential (V)
    """

    if electrons <= 0:
        raise ValueError("Number of electrons must be greater than zero.")

    if reaction_quotient <= 0:
        raise ValueError("Reaction quotient must be greater than zero.")

    E = E0 - ((R * temperature) / (electrons * F)) * math.log(reaction_quotient)

    return E


def main():

    print("=" * 50)
    print("NERNST EQUATION CALCULATOR")
    print("=" * 50)

    try:

        E0 = float(input("Standard Electrode Potential E0 (V): "))
        T = float(input("Temperature (K): "))
        n = int(input("Number of Electrons: "))
        Q = float(input("Reaction Quotient (Q): "))

        potential = nernst_equation(E0, T, n, Q)

        print("\n--------------------------------------")
        print(f"Electrode Potential = {potential:.4f} V")
        print("--------------------------------------")

    except ValueError as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()
