def lasit_treso_failu_rindu(fails):
    try:
        with open(fails, 'r', encoding='utf-8') as faila_objekts:
            # Iegūt visas rindas no faila
            rindas=faila_objekts.readlines()
            
            if len(rindas) >= 3:
                # Izdrukāt trešās rindas saturu
                print(rindas[2])
            else:
                print("Fails ir par īsu. Nav iespējams nolasīt trešo rindu.")
    except FileNotFoundError:
        print("Norādītais fails nav atrasts.")
    except Exception as e:
        print(f"Kļūda: {e}")

# Norādiet teksta faila ceļu šeit
teksta_fails='teksta_fails.txt'
lasit_treso_failu_rindu(teksta_fails)