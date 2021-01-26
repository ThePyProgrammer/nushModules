# getting any year, any sem promoModules
import os

def promo(year, sem=-1):
    if sem == "both": sem = 0
    try: os.mkdir("Year "+str(year))
    except: pass
    with open("nushModules.csv") as modules, open("Year "+str(year)+"/y"+str(year)+("s"+str(sem) if sem+1 else "")+"Modules.csv", "w+") as out:
        print(modules.readline().strip(), file=out)

        for i in modules.readlines()[1:]:
            i = i.strip()
            code, mc, name, y, s = i.split(",")
            if y == str(year):
                if sem == -1:
                    print(i, file=out)
                elif sem == 2:
                    if str(sem) in s: print(i, file=out)
                elif s == str(sem):
                    print(i, file=out)

for year in range(1, 7):
    for sem in range(-1, 3):
        promo(year, sem)
