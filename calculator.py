stripColor = {
    'preto': 0,
    'marrom': 1,
    'vermelho': 2,
    'laranja': 3,
    'amarelo': 4,
    'verde': 5,
    'azul': 6,
    'Vvioleta': 7,
    'cinza': 8,
    'branco': 9
}
stripColorMultiplier = {
    'preto': 1,
    'marrom': 10,
    'vermelho': 100,
    'laranja': 1000,
    'amarelo': 10000,
    'verde': 100000,
    'azul': 1000000,
    'violeta': 10000000,
    'cinza': 100000000,
    'branco': 1000000000
}

tolerance_values = {
    'marrom': 0.01,  # Brown - Tolerance ±1%
    'vermelho': 0.02,  # Red - Tolerance ±2%
    'verde': 0.005,  # Green - Tolerance ±0.5%
    'azul': 0.0025,  # Blue - Tolerance ±0.25%
    'violeta': 0.001,  # Violet - Tolerance ±0.1%
    'dourado': 0.05,  # Gold - Tolerance ±5%
    'prateado': 0.1  # Silver - Tolerance ±10%
}


def calc_resistance_2_strips(color_band1, color_band2, color_band_multiplier):
    value = ((stripColor[color_band1] * 10 + stripColor[color_band2]) * stripColorMultiplier[color_band_multiplier])

    return value


def calc_resistance_3_strips(color_band1, color_band2, color_band3, color_band_multiplier):
    value = (stripColor[color_band1] * 100 + stripColor[color_band2] * 10 + stripColor[color_band3]) * \
            stripColorMultiplier[color_band_multiplier]
    return value


def calculate_tolerance(tolerance_band_color):
    value = tolerance_values[tolerance_band_color]
    return value


def resistor_calculator():
    print("Resistor Calculator")
    print("Select the number of strips:")
    print("1. Two strips")
    print("2. Three strips")

    num_strips = int(input("Enter your choice (1 or 2): "))

    if num_strips == 1:

        color_band1 = input("Enter the color of the first band: ")
        color_band2 = input("Enter the color of the second band: ")
        color_band_multiplier = input("Enter the color of the multiplier band: ")
        tolerance_band_color = input("Enter the color of the tolerance band: ")
        resistance = calc_resistance_2_strips(color_band1.lower(), color_band2.lower(), color_band_multiplier.lower())

        tolerance = calculate_tolerance(tolerance_band_color.lower())

        resistance_lower = resistance - (resistance * tolerance)
        resistance_upper = resistance + (resistance * tolerance)

    elif num_strips == 2:

        color_band1 = input("Enter the color of the first band: ")
        color_band2 = input("Enter the color of the second band: ")
        color_band3 = input("Enter the color of the third band: ")
        color_band_multiplier = input("Enter the color of the multiplier band: ")
        tolerance_band_color = input("Enter the color of the tolerance band: ")

        resistance = calc_resistance_3_strips(color_band1.lower(), color_band2.lower(), color_band3.lower(),
                                              color_band_multiplier.lower())
        tolerance = calculate_tolerance(tolerance_band_color.lower())

        resistance_lower = resistance - (resistance * tolerance)
        resistance_upper = resistance + (resistance * tolerance)


    else:

        print("Invalid choice. Please select 1 or 2.")
        return

    print(f"The resistance is: {resistance} ohms and tolerance is: {tolerance}")
    print(f"The lowest resistance is: {resistance_lower} ohms")
    print(f"The highest resistance is: {resistance_upper} ohms")


# Run the resistor calculator
resistor_calculator()
