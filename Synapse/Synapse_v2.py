import csv
import os
import sys


FILE_NAME = "value_r.csv"
FIELDNAMES = ["id", "categoria", "argomento", "livello", "stato", "note"]


def main():
    initialize()

    while True:
        print("\n--- SYNAPSE MENU ---")
        choice = input("1) Aggiungi valore\n2) Leggi report\n3) Modifica valore\n4) Cancella valore\n5) Exit\nScelta: ").strip()

        if choice == "1":
            add_value()
        elif choice == "2":
            view_report()
        elif choice == "3":
            update_value()
        elif choice ==  "4":
            delete_value()
        elif choice == "5":
            sys.exit()
        else:
            print("Scelta non valida.")


# ---------------- INITIALIZE ----------------
def initialize():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()


# ---------------- ADD ----------------
def add_value():
    value_one = input("Id: ").strip()
    value_two = input("Categoria: ").lower().strip()
    value_three = input("Argomento: ").lower().strip()
    value_four = input("Livello: ").lower().strip()
    value_five = input("Stato: ").lower().strip()
    value_six = input("Note: ").lower().strip()

    row = {
        FIELDNAMES[0]: value_one,
        FIELDNAMES[1]: value_two,
        FIELDNAMES[2]: value_three,
        FIELDNAMES[3]: value_four,
        FIELDNAMES[4]: value_five,
        FIELDNAMES[5]: value_six
    }

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writerow(row)

    print("Synapse -- Valore aggiunto con successo.")


# ---------------- VIEW ----------------
def view_report():
    with open(FILE_NAME) as file:
        reader = csv.DictReader(file)

        print("\n--- Synapse -- REPORT ---")
        for row in reader:
            print(f"ID: {row["id"]} | "
                  f"Categoria: {row["categoria"]} |"
                  f"Argomento: {row["argomento"]} |"
                  f"Livello: {row["livello"]} |"
                  f"Stato: {row["stato"]} |"
                  f"Note: {row["note"]}")

#---------------- MODIFY ---------------
def update_value():
    target = input("Quale valore vuoi modificare? ").lower().strip()

    updated_rows = []

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["id"] == target:
                target_int = input("Quale attributo vuoi modificare? ").lower().strip()
                if target_int in FIELDNAMES:
                    new_value = input("Nuovo valore: ").strip()
                    row[target_int] = new_value

            updated_rows.append(row)

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(updated_rows)

    print("Synapse -- Aggiornamento completato.")
    
#--------------- DELETE --------------
def delete_value():
    target = input("Quale valore vuoi eliminare? ").lower().strip()

    remaining_rows = []

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["id"] != target:
                remaining_rows.append(row)

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(remaining_rows)

    print("Synapse -- Valore eliminato.")
    
if __name__ == "__main__":
    main()