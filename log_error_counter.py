def count_errors(log_file):
    error_lines = []

    with open(log_file, "r") as file:
        for line in file:
            if "ERROR" in line:
                error_lines.append(line.strip())

    print("Total ERROR lines:", len(error_lines))

    print(f"\nError Lines : {error_lines}")


# Example usage
count_errors("system.log")
