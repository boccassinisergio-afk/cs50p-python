import json
import os

cartella = os.path.dirname(__file__)
print(cartella)
print(os.path.join(cartella, "report.json"))

def main():
    report_n = carica_dati()
    vendite = report_n["vendite"]
    problemi = report_n["problemi"]
    while True:
        print("\n=== CALL TRACKER ===")
        print("1 - Registra vendita")
        print("2 - Registra problema cliente")
        print("3 - Vedi report di oggi")
        print("4 - Esci")

        scelta = input("\nScegli: ").strip()

        if scelta == "1":
            print("(funzione vendita - prossimo blocco)")
            cliente = input("Cliente: ").strip()
            auto = input("Auto: ").strip()
            costo = input("Costo: ").strip()
            extra = input("Extra: ").strip()
            insert_vendite(vendite, cliente, auto, costo, extra)
            
        elif scelta == "2":
            print("(funzione problema - prossimo blocco)")
            problemi_list = []
            cliente = input("Cliente: ").strip()
            while True:
                problemi_var = input("Problema: ").strip()
                if problemi_var == "exit":
                    break 
                else:
                    problemi_list.append(problemi_var)
            insert_problemi(problemi, problemi_list, cliente)
            
        elif scelta == "3":
            print("(funzione report - prossimo blocco)")
            report(vendite, problemi)
        elif scelta == "4":
            print("Arrivederci!")
            salva_dati(vendite, problemi)
            break
        else:
            print("Scelta non valida, riprova.")
            

def insert_vendite(vendite, n1, n2, n3, n4):
    ven_uno = {"cliente":n1 , "auto":n2, "costo":n3, "extra":n4}
    return vendite.append(ven_uno)
    
def insert_problemi(problemi, problemi_list, n1):
    pro_uno = {"cliente":n1, "problema":problemi_list}
    return problemi.append(pro_uno)

def report(vendite, problemi):
    contatore = {}
    contatore_problemi = {}
    for i in vendite:
        if i["extra"] not in contatore:
            contatore[i["extra"]] = 1
        else:
            contatore[i["extra"]] += 1
    for chiave, valore in contatore.items():
        print(chiave, valore)
      
    for i in problemi:
        for problema in i["problema"]:
            if problema not in contatore_problemi:
                contatore_problemi[problema] = 1
            else:
                contatore_problemi[problema] += 1
    for chiave, valore in contatore_problemi.items():
        print(chiave, valore)
        
def salva_dati(vendite, problemi):
    cartella = os.path.dirname(__file__)
    dict_vendite_problemi = {"vendite":vendite, "problemi": problemi}
    with open(os.path.join(cartella, "report.json"), "w") as f:
        json.dump(dict_vendite_problemi, f)
        
def carica_dati():
    cartella = os.path.dirname(__file__)
    if os.path.exists(os.path.join(cartella, "report.json")):
        with open(os.path.join(cartella, "report.json"), "r") as f:
            report_n = json.load(f)
            return report_n
    else:
        return {"vendite":[], "problemi": []}

main()
