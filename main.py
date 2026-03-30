import time

data_limits = {
    "internal_temperature": {
        "min": 18,
        "max": 26,
    },
    "external_temperature": {
        "min": -100,
        "max": 100,
    },
    "structural_integrity": {
        "min": 1,
        "max": 1,
    },
    "energy_level": {
        "min": 50,
        "max": 100,
    },
    "tank_pressure": {
        "min": 100,
        "max": 140,
    },
    "critic_modules_status": {"min": 1, "max": 1},
}


def countdown(seconds, message):
    count = seconds

    while count > 0:
        print(f"{count} segundo{"s" if count > 1 else ""}...")
        time.sleep(1)
        count -= 1

    print(f"\n{message}")


def painel(
    temperatura_Interna,
    temperatura_Externa,
    integridade_Estrutural,
    niveis_de_energia,
    pressao_de_energia,
    Status_dos_modulos_criticos,
):
    print(
        f"Temperatura Interna: {temperatura_Interna}\nTemperatura Externa: {temperatura_Externa}\nIntegridade Estrutural: {integridade_Estrutural}\nNiveis de Energia: {niveis_de_energia}\nPressão de Energia: {pressao_de_energia}\nStatus dos Modulos Criticos: {Status_dos_modulos_criticos}\n"
    )


def separate_headers(headers):
    _headers = headers.split(",")
    _headers[-1] = _headers[-1][: len(_headers[-1]) - 1]

    return _headers


def get_matrix(data):
    matrix = []
    headers = []

    for line in range(len(data)):
        if line == 0:
            headers = separate_headers(data[line])
            continue

        telemetry_data = data[line].split(",")
        validation_line = []

        for h_index in range(len(headers)):
            data_value = int(telemetry_data[h_index])
            is_valid = (
                data_value >= data_limits[headers[h_index]]["min"]
                and data_value <= data_limits[headers[h_index]]["max"]
            )

            validation_line.append(is_valid)

        matrix.append(validation_line)

    return matrix, headers


def get_positives_percentage(matrix, headers):
    count = [0] * len(headers)
    percentages = []
    total_lines = len(matrix)

    for line in matrix:
        for index in range(len(headers)):
            if line[index]:
                count[index] += 1

    for num in count:
        percentages.append(round((num / total_lines) * 100, 2))

    return percentages


def get_average_percentage(percentages):
    count = 0

    for num in percentages:
        count += num

    result = round(count / len(percentages), 2)

    return result


def get_averages(data, headers):
    averages = {
        "internal_temperature": {
            "values": [],
            "average": 0,
        },
        "external_temperature": {
            "values": [],
            "average": 0,
        },
        "structural_integrity": {
            "values": [],
            "average": False,
        },
        "energy_level": {
            "values": [],
            "average": 0,
        },
        "tank_pressure": {
            "values": [],
            "average": 0,
        },
        "critic_modules_status": {"values": [], "average": 0},
    }

    for line in range(1, len(data)):
        values = data[line].split(",")
        values[-1] = values[-1][: len(values[-1]) - 1]

        for h_index in range(len(headers)):
            averages[headers[h_index]]["values"].append(values[h_index])

    for item in averages:
        total_values = 0
        average = 0

        for val in averages[item]["values"]:
            total_values += int(val)

        average = total_values / len(averages[item]["values"])

        averages[item]["average"] = (
            average
            if item != "structural_integrity" and item != "critic_modules_status"
            else average > 0.5
        )

    return averages


def validate_data(data):
    matrix, headers = get_matrix(data)
    averages = get_averages(data, headers)
    percentages = get_positives_percentage(matrix, headers)

    return {
        "percentages": percentages,
        "averages": averages,
    }


def show_percentages(headers, percentages):
    print("PORCENTAGEM DE DADOS POSITIVOS:")

    for index in range(len(percentages)):
        print(f"{headers[index]}: {percentages[index]}%")

    print(f"\nMÉDIA DE PORCENTAGEM: {get_average_percentage(percentages)}%")


def launch(averages, percentages):
    data_map = {
        "internal_temperature": "Temperatura interna",
        "external_temperature": "Temperatura externa",
        "structural_integrity": "Integridade extrutural",
        "energy_level": "Nível de energia",
        "tank_pressure": "Pressão dos tanques",
        "critic_modules_status": "Status dos Módulos Críticos",
    }
    mapped_headers = [data_map[header] for header in averages]
    will_launch = True

    for item in data_limits:
        print(f"{data_map[item]}:", end=" ", flush=True)

        for _ in range(3):
            time.sleep(0.3)
            print(".", end="", flush=True)

        time.sleep(0.5)

        print("\r" + " " * (len(data_map[item]) + 6), end="")

        if (
            int(averages[item]["average"]) < data_limits[item]["min"]
            or int(averages[item]["average"]) > data_limits[item]["max"]
        ):
            will_launch = False
            print(f"\r{data_map[item]}: ERRO")
        else:
            print(f"\r{data_map[item]}: OK")

    if will_launch:
        print("")
        show_percentages(mapped_headers, percentages)

        print("\nPRONTO PARA DECOLAR\n")
        countdown(5, "DECOLAR")
    else:
        print("\nDECOLAGEM ABORTADA")
        print("\nRELATÓRIO DOS SENSORES:")

        averages = list(
            map(lambda item: round(float(averages[item]["average"]), 2), averages)
        )
        painel(*averages)

        print("")
        show_percentages(mapped_headers, percentages)


def main():
    with open("./data.csv", "r") as file:
        data = file.readlines()
        validated_data = validate_data(data)

        launch(
            validated_data["averages"],
            validated_data["percentages"],
        )


if __name__ == "__main__":
    main()
