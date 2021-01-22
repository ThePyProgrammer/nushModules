with open("nushModules.csv") as modules, open("table.md", "w+") as table:
    print("# Table\n", file=table)
    lines = modules.readlines()
    for line in range(len(lines)):
        print("|", " | ".join(lines[line].strip().split(",")), "|", file=table)
        if line == 0: print("| --- | --- | --- | -- | -- |", file=table)
