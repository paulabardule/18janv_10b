import csv

def lasit_otro_kolonnu(csv_fails):
    try:
        with open(csv_fails, 'r', newline='', encoding='utf-8') as csvfile:
            csvlasitajs=csv.reader(csvfile)

            for rinda in csvlasitajs:
                if len(rinda) > 1:
                    print(rinda[1])
                else:
                    print("Nepietiek stabiņu kolonnā")
    except FileNotFoundError:
        print("Norādītais fails nav atrasts.")
    except Exception as e:
        print(f"Kļūda: {e}")

# Norādiet CSV faila ceļu šeit
csv_fails='fails.csv'
lasit_otro_kolonnu(csv_fails)