from rdkit import Chem
from rdkit.Chem import rdMolDescriptors
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("MolecularFormulaCalculator")


class MolecularFormulaCalculator:
    @staticmethod
    def smiles_to_mol(smiles: str) -> Chem.Mol | None:
        try:
            mol = Chem.MolFromSmiles(smiles.strip())
            if mol is None:
                logger.warning(f"Niewłaściwy SMILES: {smiles}")
            else:
                logger.info(f"Poprawne przekonwertowano SMILES: {smiles}")
                return mol
        except Exception as e:
            logger.error(f"Błąd konwersji SMILES: {e}")
            return None

    @staticmethod
    def calculate_formula(mol: Chem.Mol) -> str | None:
        try:
            formula = rdMolDescriptors.CalcMolFormula(mol)
            logger.info(f"Wzór sumaryczny: {formula}")
            return formula
        except Exception as e:
            logger.error(f"Błąd podczas obliczania wzoru sumarycznego: {e}")
            return None

    @staticmethod
    def mass_from_smiles(mol: Chem.Mol) -> float | None:
        try:
            mollar_mass = Chem.rdMolDescriptors.CalcExactMolWt(mol)
            logger.info(f"Masa molowa: {mollar_mass}")
            return mollar_mass
        except Exception as e:
            logger.error(f"Błąd podczas obliczania wzoru sumarycznego: {e}")
            return None

    @staticmethod
    def is_ring(mol: Chem.Mol) -> int | None:
        try:
            ring = mol.GetRingInfo().NumRings()
            if ring == 0:
                return 1
            else:
                return 0
        except Exception as e:
            logger.error(f"Błąd podczas sprawdzania pierścieni: {e}")
            return None
