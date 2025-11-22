from flask import Flask, jsonify, request
from flask_cors import CORS
from rdkit import Chem
from rdkit.Chem import AllChem
from molecules import MOLECULES

app = Flask(__name__)
CORS(app)  


@app.route('/api/molecules', methods=['GET'])
def get_molecule_list():
    """return list of available molecules for dropdown"""
    molecule_list = []
    for key, data in MOLECULES.items():
        molecule_list.append({
            "id": key,
            "name": data["name"],
            "formula": data["formula"]
        })
    return jsonify({"molecules": molecule_list})


@app.route('/api/structure/<molecule_id>', methods=['GET'])
def get_structure(molecule_id):
    """return resonance structures with 3D coordinates and scores"""
    
 
    if molecule_id not in MOLECULES:
        return jsonify({"error": "Molecule not found"}), 404
    
    mol_data = MOLECULES[molecule_id]
    structures = []
    

    for idx, res_struct in enumerate(mol_data["resonance_structures"]):

        mol = Chem.MolFromSmiles(res_struct["smiles"])
        
        if mol is None:
            continue
        

        mol = Chem.AddHs(mol)
        
  
        try:
            AllChem.EmbedMolecule(mol, randomSeed=42)
            AllChem.MMFFOptimizeMolecule(mol)
        except:
   
            AllChem.Compute2DCoords(mol)
        
      
        formal_charges = {}
        lone_pairs = {}
        for atom in mol.GetAtoms():
            fc = atom.GetFormalCharge()
            if fc != 0:
                formal_charges[atom.GetIdx()] = fc
            
       
            expected_valence = {
                'C': 4, 'N': 5, 'O': 6, 'F': 7, 'S': 6, 'Cl': 7, 'Br': 7
            }
            if atom.GetSymbol() in expected_valence:
                num_bonds = sum([bond.GetBondTypeAsDouble() for bond in atom.GetBonds()])
                lp = (expected_valence[atom.GetSymbol()] - num_bonds - fc) / 2
                if lp > 0:
                    lone_pairs[atom.GetIdx()] = int(lp)
        
        score = calculate_stability(mol)
        
    
        mol_block = Chem.MolToMolBlock(mol, includeStereo=True)
        
 
        structures.append({
            "rank": idx + 1,
            "label": res_struct["label"],
            "is_major": res_struct.get("is_major", False),
            "mol_block": mol_block,
            "formal_charges": formal_charges,
            "lone_pairs": lone_pairs,
            "stability_score": score,
            "explanation": res_struct["explanation"]
        })
    
    return jsonify({
        "molecule_name": mol_data["name"],
        "formula": mol_data["formula"],
        "structures": structures
    })

def calculate_stability(mol):
    """calculate simple stability score based on formal charges"""
    score = 100
    
    for atom in mol.GetAtoms():
        fc = atom.GetFormalCharge()
        
   
        if fc != 0:
            score -= 10
        
     
        if fc == -1 and atom.GetSymbol() in ['O', 'N', 'F', 'Cl']:
            score += 5
        
 
        if fc == 1 and atom.GetSymbol() in ['O', 'N', 'F']:
            score -= 5
    # review these later
    return max(score, 0)

if __name__ == '__main__':
    app.run(debug=True, port=5000)




