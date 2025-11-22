import React, { useEffect, useRef } from 'react';

function StructureViewer({ structure }) {
  const containerRef = useRef(null);
  const viewerRef = useRef(null);

  useEffect(() => {
    if (!structure || !window.$3Dmol) return;

    if (containerRef.current) {
      containerRef.current.innerHTML = '';
    }

    const config = {
      backgroundColor: 'white'
    };

    const viewer = window.$3Dmol.createViewer(containerRef.current, config);

    viewer.addModel(structure.mol_block, 'sdf');
    
    viewer.setStyle({}, {
      stick: { radius: 0.15 },
      sphere: { scale: 0.3 }
    });

    const atoms = viewer.getModel().selectedAtoms({});
    atoms.forEach((atom) => {
      viewer.addLabel(atom.elem, {
        position: atom,
        backgroundColor: 'rgba(255, 255, 255, 0.7)',
        fontColor: 'black',
        fontSize: 12,
        backgroundOpacity: 0.7
      });
    });

    if (structure.formal_charges) {
      Object.entries(structure.formal_charges).forEach(([atomIdx, charge]) => {
        const label = charge > 0 ? `+${charge}` : `${charge}`;
        viewer.addLabel(label, {
          position: { serial: parseInt(atomIdx) + 1 },
          backgroundColor: 'rgba(255, 255, 255, 0.8)',
          fontColor: charge < 0 ? 'red' : 'blue',
          fontSize: 14,
          fontWeight: 'bold'
        });
      });
    }

    if (structure.lone_pairs) {
      Object.entries(structure.lone_pairs).forEach(([atomIdx, numPairs]) => {
        const label = '⋮'.repeat(numPairs);
        viewer.addLabel(label, {
          position: { serial: parseInt(atomIdx) + 1 },
          backgroundColor: 'transparent',
          fontColor: 'purple',
          fontSize: 20,
          fontWeight: 'bold'
        });
      });
    }

    viewer.zoomTo();
    viewer.render();
    viewerRef.current = viewer;

    return () => {
      if (viewerRef.current) {
        viewerRef.current.clear();
      }
    };
  }, [structure]);

  return (
    <div className="structure-card">
      <div className="structure-header">
        <h3>{structure.label}</h3>
        {structure.is_major && (
          <span className="major-badge">⭐ Major Contributor</span>
        )}
        <p className="score">Stability Score: {structure.stability_score}</p>
      </div>
      <div 
        ref={containerRef}
        className="viewer-container"
        style={{ width: '350px', height: '350px', position: 'relative' }}
      />
      <div className="explanation">
        <p>{structure.explanation}</p>
      </div>
    </div>
  );
}

export default StructureViewer;