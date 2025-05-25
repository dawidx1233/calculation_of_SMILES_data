from rdkit import Chem
from rdkit.Chem import Descriptors
mol = Chem.MolFromSmiles("C1CCCCC1".strip())
print(mol.GetRingInfo().NumRings())