import csv

def otra_kolonna(csv_fails):
    try:
        with open(csv_fails, 'r', newline='', encoding='utf8') as csvfile:
            csvlasitajs=csv.reader(csvfile)

            for rinda in csvlasitajs:
                if len(rinda) > 1:
                    print(rinda[1])
                else:
                    print("Nepietiek kolonnu")
    except FileNotFoundError:
        print("Norādītais fails nav atrasts.")
    except Exception as e:
        print(f"Kļūda: {e}")

# Norādiet CSV faila ceļu šeit
csv_fails='fails.csv'
otra_kolonna(csv_fails)