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
        mollar_mass = mfc.mass_from_smiles(mol)
        if mollar_mass:
            print(f"Masa molowa: {round(mollar_mass, 2)}")
        else:
            print("Nie udało się obliczyć masy molowej")
        rings = mfc.is_ring(mol)
        if rings:
            if rings == 0:
                print(f"Cząstka zawieta pierścienie")
            else:
                print(f"Cząstka nie zawieta pierścieni")
        else:print("Nie udało się obliczyć czy jest pierścień")


if __name__ == "__main__":
    main()
