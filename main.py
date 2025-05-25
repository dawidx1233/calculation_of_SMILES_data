from calculator import MolecularFormulaCalculator as mfc


def main():
    print("Wprowadź SMILES lub 'q' aby zakończyć")
    while True:
        user_input = input("\nPodaj SMILES: ")
        if user_input.lower() == "q":
            print("Zakończenie działania programu")
            break
        mol = mfc.smiles_to_mol(user_input)
        if mol is None:
            continue
        formula = mfc.calculate_formula(mol)
        if formula:
            print(f"Wzór sumaryczny: {formula}")
        else:
            print("Nie udało się obliczyć wzoru sumnarycznego")


if __name__ == "__main__":
    main()
