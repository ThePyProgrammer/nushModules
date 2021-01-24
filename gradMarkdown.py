with open("gradModules.csv") as modules, open("grad.md", "w+") as table:
    print("# Graduation Modules\n", file=table)
    lines = modules.readlines()
    for line in range(len(lines)):
        print("|", " | ".join(lines[line].strip().split(",")), "|", file=table)
        if line == 0: print("| --- | --- | --- | -- | -- |", file=table)
