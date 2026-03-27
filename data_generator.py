from argparse import ArgumentParser
import random


def generate_random_number(rangeA, rangeB):
    num = random.randrange(rangeA, rangeB + 1)

    return num


def generate_csv(lines):
    with open("./data.csv", "w") as file:
        file.write(
            "internal_temperature,external_temperature,structural_integrity,energy_level,tank_pressure,critic_modules_status\n"
        )

        for _ in range(lines):
            internal_temperature = generate_random_number(12, 32)
            external_temperature = generate_random_number(-200, 200)
            structural_integrity = generate_random_number(0, 1)
            energy_level = generate_random_number(0, 100)
            tank_pressure = generate_random_number(80, 160)
            critic_modules_status = generate_random_number(0, 1)

            file.write(
                f"{internal_temperature},{external_temperature},{structural_integrity},{energy_level},{tank_pressure},{critic_modules_status}\n"
            )


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-l", "--lines", default=100)
    args = parser.parse_args()
    lines = args.lines

    generate_csv(lines)
