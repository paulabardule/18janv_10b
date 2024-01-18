def ierakstit_faila(lietotaja_vards):
    try:
        with open('lietotajs.txt', 'a', encoding='utf-8') as faila_objekts:
            faila_objekts.write(lietotaja_vards + '\n')
        print("Vārds veiksmīgi ierakstīts failā.")
    except FileNotFoundError:
        print("Fails nav atrasts.")
    except Exception as e:
        print(f"Kļūda: {e}")

def main():
    try:
        lietotaja_vards = input("Ievadiet savu vārdu: ")

        ierakstit_faila(lietotaja_vards)

    except Exception as e:
        print(f"Kļūda: {e}")

if __name__ == "__main__":
    main()
