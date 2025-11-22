import React, { useState } from 'react';
import axios from 'axios';
import MoleculeSelector from './MoleculeSelector';
import StructureViewer from './StructureViewer';
import './App.css';

function App() {
  const [moleculeData, setMoleculeData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleMoleculeSelect = async (moleculeId) => {
    if (!moleculeId) return;
    
    setLoading(true);
    setError(null);
    
    try {
      const response = await axios.get(
        `http://localhost:5000/api/structure/${moleculeId}`
      );
      setMoleculeData(response.data);
    } /* add error handling */
    catch (error) {
      console.error('Error loading molecule:', error);
      setError('Failed to load molecule structure. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleBack = () => {
    setMoleculeData(null);
    setError(null);
  };

  return (
    <div className="App">
      <header className="app-header">
        <h1>🔬 Resonance Structure Visualizer</h1>
        <p>Interactive 3D visualization of molecular resonance structures</p>
      </header>

      <main className="app-main">
        {!moleculeData && (
          <MoleculeSelector onSelect={handleMoleculeSelect} />
        )}

        {loading && (
          <div className="loading">
            <div className="spinner"></div>
            <p>Loading structure...</p>
          </div>
        )}

        {error && (
          <div className="error-message">
            <p>{error}</p>
            <button onClick={() => setError(null)}>Try Again</button>
          </div>
        )}

        {moleculeData && !loading && (
          <div className="results">
            <button className="back-button" onClick={handleBack}>
              ← Back to Selection
            </button>
            
            <h2 className="molecule-title">
              {moleculeData.molecule_name} ({moleculeData.formula})
            </h2>
            
            <div className="structures-grid">
              {moleculeData.structures.map((structure, idx) => (
                <StructureViewer key={idx} structure={structure} />
              ))}
            </div>

            <div className="info-box">
              <h3>💡 About Resonance Structures</h3>
              <p>
                These structures show different possible arrangements of electrons 
                in the molecule. The actual molecule is a <strong>hybrid</strong> of 
                all resonance contributors, with major contributors having the 
                greatest influence on molecular properties and reactivity.
              </p>
              <p>
                <strong>Stability factors:</strong> Structures with minimal formal 
                charges, negative charges on electronegative atoms (O, N, F), and 
                complete octets are generally more stable.
              </p>
            </div>

            <div className="formula-box">
              <h3>📐 Resonance Stability Score Calculation</h3>
              <pre>{`Stability Score = weighted sum of:
[-10 points] Per non-zero formal charge
[-20 points] Per separated charge pair
[-15 points] Negative charge on electropositive atom
[-15 points] Positive charge on electronegative atom 
[+10 points] All atoms have complete octets
[+5 points]  Negative charge on O/N/halogen
[+5 points]  Positive charge on less electronegative atoms`}</pre>
              
              <p><strong>Example for Carbonate Ion (CO₃²⁻): C(=O)([O-])[O-]</strong></p>
              <ul>
                <li>Base score: 100</li>
                <li>Two oxygen atoms with -1 charge: -10 - 10 = -20</li>
                <li>Negative charges on oxygen (electronegative): +5 + 5 = +10</li>
                <li><code>Final Score = 100 - 20 + 10 = 90</code></li>
              </ul>
            </div>
          </div>
        )}
      </main>

      <footer className="app-footer">
        <p>Educational tool for chemistry students - Drag to rotate 3D models - Scroll to zoom</p>
      </footer>
    </div>
  );
}

export default App;