with open("sample.log", "r") as file:
    logs = file.readlines()

info = 0
debug = 0
warning = []
error = []

for line in logs:

    if " INFO " in line:
        info += 1

    elif " DEBUG " in line:
        debug += 1

    elif " WARNING " in line:
        warning.append(line.strip())

    elif " ERROR " in line:
        error.append(line.strip())


print("\n========== LOG ANALYSIS REPORT ==========\n")

print(f"Total Log Records: {len(logs)}")
print(f"INFO Messages: {info}")
print(f"DEBUG Messages: {debug}")
print(f"WARNING Messages: {len(warning)}")
print(f"ERROR Messages: {len(error)}")


print("\n========== ERRORS ==========\n")

for i, message in enumerate(error, 1):
    print(f"{i}. {message}")


print("\n========== WARNINGS ==========\n")

for i, message in enumerate(warning, 1):
    print(f"{i}. {message}")


print("\n=========================================")

