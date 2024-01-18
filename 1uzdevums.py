def lasit_datni():
    try:
        with open("teksts.txt", "r", encoding="utf8") as datne:
            for x in datne:
                print(x)


    except FileNotFoundError:
        print("Datne nav atrasta!")


if __name__=="__main__":
    lasit_datni()