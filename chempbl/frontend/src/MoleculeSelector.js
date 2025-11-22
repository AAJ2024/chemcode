import React, { useState, useEffect } from 'react';
import axios from 'axios';

function MoleculeSelector({ onSelect }) {
  const [molecules, setMolecules] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get('http://localhost:5000/api/molecules')
      .then(response => {
        setMolecules(response.data.molecules);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching molecules:', error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div className="loading">Loading molecules...</div>;
  }

  return (
    <div className="molecule-selector">
      <h2>Select a Molecule</h2>
      <select 
        onChange={(e) => onSelect(e.target.value)} 
        defaultValue=""
        className="molecule-dropdown"
      >
        <option value="" disabled>Choose a molecule...</option>
        {molecules.map(mol => (
          <option key={mol.id} value={mol.id}>
            {mol.name} ({mol.formula})
          </option>
        ))}
      </select>
    </div>
  );
}

export default MoleculeSelector;