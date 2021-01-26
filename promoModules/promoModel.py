# getting any year, any sem promoModules

def promo(year, sem=0):
    if s == "both": s = 12
    with open("nushModules.csv") as modules, open("y"+str(year)+("s"+sem if sem else "")+"Modules.csv", "w+") as out:
        print(modules.readline(), file=out)

        for i in modules.readlines()[1:]:
            code, mc, name, y, s = i.strip().split(",")
            if y == str(year):
                if sem == 0:
                    print(i, file=out)
                elif sem == 2:
                    if str(sem) in s: print(i, file=out)
                elif s == str(sem):
                    print(i, file=out)
