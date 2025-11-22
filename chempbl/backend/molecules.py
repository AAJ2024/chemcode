MOLECULES = {
    "benzene": {
        "name": "Benzene",
        "formula": "C6H6",
        "resonance_structures": [
            {
                "smiles": "C1=CC=CC=C1",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "This structure shows alternating single and double bonds in the ring. Carbon atoms: 6 (each with 4 bonds). Hydrogen atoms: 6 (each bonded to one carbon). All carbons have sp² hybridization. The π electrons are delocalized across the entire ring, creating aromatic stability. Bond angles are 120° due to planar hexagonal geometry."
            },
            {
                "smiles": "c1ccccc1",
                "label": "Structure 2",
                "is_major": True,
                "explanation": "Equivalent resonance form with double bonds shifted to alternate positions. The actual benzene structure is a perfect hybrid where all C-C bonds are identical (1.39 Å). This delocalization energy stabilizes benzene by approximately 36 kcal/mol compared to theoretical cyclohexatriene. All six π electrons occupy molecular orbitals spanning the entire ring."
            }
        ]
    },

    "carbonate": {
        "name": "Carbonate Ion",
        "formula": "CO3(2-)",
        "resonance_structures": [
            {
                "smiles": "[O-]C(=O)[O-]",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "One C=O double bond and two C–O⁻ single bonds. Carbon is sp² hybridized with trigonal planar geometry (120°). π electrons are delocalized over all three C–O bonds, making them equivalent in the hybrid."
            },
            {
                "smiles": "O=C([O-])[O-]",
                "label": "Structure 2",
                "is_major": True,
                "explanation": "Equivalent resonance form with the double bond positioned on a different oxygen atom. All three forms contribute equally to the hybrid, causing all C–O bond lengths to become identical (~1.28 Å)."
            },
            {
                "smiles": "[O-]C([O-])=O",
                "label": "Structure 3",
                "is_major": True,
                "explanation": "Third equivalent resonance form. Charge delocalization spreads the −2 charge evenly across all oxygen atoms, increasing stability through resonance."
            }
        ]
    },

    "acetate": {
        "name": "Acetate Ion",
        "formula": "CH3COO(-)",
        "resonance_structures": [
            {
                "smiles": "CC(=O)[O-]",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "The negative charge is located on the singly bonded oxygen. Carbonyl carbon is sp² hybridized with trigonal planar geometry. The π bond can shift between oxygens, allowing delocalization across the two C–O bonds."
            },
            {
                "smiles": "CC([O-])=O",
                "label": "Structure 2",
                "is_major": True,
                "explanation": "Equivalent resonance structure with the double bond on the opposite oxygen. The hybrid has two identical C–O bond lengths due to equal sharing of π electron density."
            }
        ]
    },

    "nitrate": {
        "name": "Nitrate Ion",
        "formula": "NO3(-)",
        "resonance_structures": [
            {
                "smiles": "[O-][N+](=O)[O-]",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "Nitrogen has a formal positive charge due to forming four bonds. One N=O double bond and two N–O⁻ single bonds. The ion is trigonal planar with sp² hybridized nitrogen. π electrons are delocalized across all three N–O bonds."
            },
            {
                "smiles": "[O-][N+]([O-])=O",
                "label": "Structure 2",
                "is_major": True,
                "explanation": "Equivalent resonance form with the double bond located on a different oxygen. All N–O bond lengths become identical (~1.24 Å) in the resonance hybrid."
            },
            {
                "smiles": "O=[N+]([O-])[O-]",
                "label": "Structure 3",
                "is_major": True,
                "explanation": "Third equal contributor. The −1 charge is delocalized evenly across all oxygens, stabilizing the ion through extensive resonance."
            }
        ]
    },

    "formate": {
        "name": "Formate Ion",
        "formula": "HCOO(-)",
        "resonance_structures": [
            {
                "smiles": "O=C[O-]",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "One C=O double bond and one C–O⁻ single bond. Carbon is sp² hybridized with trigonal planar geometry. The negative charge is initially on one oxygen but becomes delocalized in the resonance hybrid."
            },
            {
                "smiles": "[O-]C=O",
                "label": "Structure 2",
                "is_major": True,
                "explanation": "Equivalent structure where the π bond is located on the other oxygen. Delocalization results in two equal C–O bonds (~1.26 Å) in the hybrid."
            }
        ]
    },

    "phenoxide": {
        "name": "Phenoxide Ion",
        "formula": "C6H5O(-)",
        "resonance_structures": [
            {
                "smiles": "[O-]c1ccccc1",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "Negative charge localized on the oxygen atom attached to the aromatic ring. Oxygen is sp² hybridized, and the lone pair can interact with the benzene π system, enabling delocalization."
            },
            {
                "smiles": "O=C1C=CC=CC1",
                "label": "Structure 2",
                "is_major": False,
                "explanation": "Minor resonance contributor showing charge delocalization into the ring. Less significant because it disrupts aromaticity by forming a C=O bond within the ring."
            }
        ]
    },

    "allyl_cation": {
        "name": "Allyl Cation",
        "formula": "C3H5(+)",
        "resonance_structures": [
            {
                "smiles": "C=C[CH2+]",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "Positive charge located on a terminal carbon. All three carbons are sp² hybridized, forming a conjugated system. π electron donation from the C=C bond stabilizes the positive charge."
            },
            {
                "smiles": "[CH2+]C=C",
                "label": "Structure 2",
                "is_major": True,
                "explanation": "Equivalent structure with the positive charge on the opposite terminal carbon. The hybrid distributes the positive charge evenly across both terminal carbons."
            }
        ]
    },

    "ozone": {
        "name": "Ozone",
        "formula": "O3",
        "resonance_structures": [
            {
                "smiles": "[O-][O+]=O",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "Bent geometry with formal negative charge on one oxygen and positive charge on the central oxygen. π electrons can shift along the O–O–O framework, contributing to strong oxidizing properties."
            },
            {
                "smiles": "O=[O+][O-]",
                "label": "Structure 2",
                "is_major": True,
                "explanation": "Equivalent resonance form with charges assigned to different oxygens. Both structures give partial double-bond character to each O–O bond."
            }
        ]
    },

    "nitrite": {
        "name": "Nitrite Ion",
        "formula": "NO2(-)",
        "resonance_structures": [
            {
                "smiles": "[O-][N+]=O",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "Bent molecular shape with one N=O double bond and one N–O⁻ bond. Nitrogen carries a formal positive charge. π electrons are delocalized across both N–O bonds."
            },
            {
                "smiles": "O=[N+][O-]",
                "label": "Structure 2",
                "is_major": True,
                "explanation": "Equivalent resonance form with charge shifted to the opposite oxygen. The hybrid contains two identical N–O bonds (~1.22 Å)."
            }
        ]
    },

    "carboxylate": {
        "name": "Carboxylate Ion",
        "formula": "RCOO(-)",
        "resonance_structures": [
            {
                "smiles": "CC(=O)[O-]",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "General form with one C=O double bond and one C–O⁻ single bond. Carbon is sp² hybridized. The negative charge is delocalized across both oxygens through π overlap."
            },
            {
                "smiles": "CC([O-])=O",
                "label": "Structure 2",
                "is_major": True,
                "explanation": "Equivalent structure with the π bond on the other oxygen. Resonance leads to identical C–O bond lengths and significant stabilization."
            }
        ]
    },

    "pyridine": {
        "name": "Pyridine",
        "formula": "C5H5N",
        "resonance_structures": [
            {
                "smiles": "c1ccncc1",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "Six-membered aromatic ring with one nitrogen atom. Nitrogen is sp² hybridized with its lone pair in an sp² orbital outside the aromatic π system. π electrons are delocalized around the ring, maintaining aromaticity. Bond angles are ~120°."
            },
            {
                "smiles": "C1=CC=NC=C1",
                "label": "Structure 2",
                "is_major": True,
                "explanation": "Alternative representation showing explicit double bonds. The actual structure has delocalized π electrons maintaining aromaticity throughout the six-membered ring."
            }
        ]
    },

    "sulfate": {
        "name": "Sulfate Ion",
        "formula": "SO4(2-)",
        "resonance_structures": [
            {
                "smiles": "[O-]S(=O)(=O)[O-]",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "Central sulfur atom with tetrahedral geometry. Two S=O bonds and two S–O⁻ bonds. Extended π bonding via sulfur d orbitals allows delocalization across all four S–O bonds."
            },
            {
                "smiles": "O=S(=O)([O-])[O-]",
                "label": "Structure 2",
                "is_major": True,
                "explanation": "Equivalent resonance form moving double bonds to different oxygens. Resonance hybrid shows four equal S–O bonds (~1.47 Å)."
            },
            {
                "smiles": "O=S([O-])(=O)[O-]",
                "label": "Structure 3",
                "is_major": True,
                "explanation": "Third major contributor distributing the −2 charge evenly across all oxygens. Highly stabilized due to resonance."
            }
        ]
    },

    "amidine": {
        "name": "Amidine",
        "formula": "RC(=NH)NH2",
        "resonance_structures": [
            {
                "smiles": "CC(=N)N",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "C=N bond adjacent to amino nitrogen. The lone pair on the amino nitrogen delocalizes into the π system. Carbon is sp² hybridized with trigonal planar geometry."
            },
            {
                "smiles": "CC(N)=N",
                "label": "Structure 2",
                "is_major": True,
                "explanation": "Alternative arrangement showing delocalization. The π electrons distribute across the N–C–N unit providing resonance stabilization."
            }
        ]
    },

    "diazomethane": {
        "name": "Diazomethane",
        "formula": "CH2N2",
        "resonance_structures": [
            {
                "smiles": "C=[N+]=[N-]",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "Carbon double-bonded to positively charged nitrogen, which is double-bonded to negatively charged nitrogen. Carbon is sp² hybridized; the N=N unit is linear and sp hybridized."
            },
            {
                "smiles": "C[N-][N+]#N",
                "label": "Structure 2",
                "is_major": False,
                "explanation": "Minor contributor with nitrogen-nitrogen triple bond. Less stable due to different charge distribution pattern."
            }
        ]
    },

    "cyanate": {
        "name": "Cyanate Ion",
        "formula": "OCN(-)",
        "resonance_structures": [
            {
                "smiles": "[O-]C#N",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "Linear O–C–N unit with carbon sp hybridized. Negative charge resides primarily on oxygen. π electrons delocalize across the O–C–N framework."
            },
            {
                "smiles": "O=C=[N-]",
                "label": "Structure 2",
                "is_major": False,
                "explanation": "Minor structure with negative charge shifted to nitrogen. Less significant but contributes to overall electron distribution."
            }
        ]
    },

    "thiocyanate": {
        "name": "Thiocyanate Ion",
        "formula": "SCN(-)",
        "resonance_structures": [
            {
                "smiles": "[S-]C#N",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "Linear S–C–N arrangement with carbon sp hybridized. Negative charge resides on sulfur due to its polarizability. π electrons delocalize through the S–C–N system."
            },
            {
                "smiles": "S=C=[N-]",
                "label": "Structure 2",
                "is_major": False,
                "explanation": "Minor contributor with negative charge on nitrogen. Less dominant due to sulfur's preference to hold negative charge."
            }
        ]
    },

    "pyrrole": {
        "name": "Pyrrole",
        "formula": "C4H5N",
        "resonance_structures": [
            {
                "smiles": "c1cc[nH]c1",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "Five-membered aromatic ring. Nitrogen is sp² hybridized with its lone pair participating in the aromatic π sextet. All atoms planar with 6 π electrons (Hückel rule)."
            },
            {
                "smiles": "C1=CNC=C1",
                "label": "Structure 2",
                "is_major": True,
                "explanation": "Alternative representation of the aromatic pyrrole ring showing the nitrogen contributing its lone pair to achieve aromaticity."
            }
        ]
    },

    "imidazole": {
        "name": "Imidazole",
        "formula": "C3H4N2",
        "resonance_structures": [
            {
                "smiles": "c1cnc[nH]1",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "Five-membered aromatic ring with two nitrogen atoms. One nitrogen contributes a lone pair to the π system; the other has a lone pair in an sp² orbital. Aromatic with 6 π electrons."
            },
            {
                "smiles": "C1=CN=C[NH]1",
                "label": "Structure 2",
                "is_major": True,
                "explanation": "Alternative representation showing the aromatic character with explicit bonds. Both nitrogens participate in maintaining aromaticity."
            }
        ]
    },

    "enolate": {
        "name": "Enolate Ion",
        "formula": "RCOCH(-)",
        "resonance_structures": [
            {
                "smiles": "CC(=O)[CH2-]",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "Negative charge on α-carbon with carbonyl intact. This form explains nucleophilic behavior at the α-position."
            },
            {
                "smiles": "CC([O-])=C",
                "label": "Structure 2",
                "is_major": True,
                "explanation": "Negative charge on oxygen with C=C double bond. Oxygen stabilizes the negative charge strongly. Hybrid provides delocalization between oxygen and carbon."
            }
        ]
    },

    "nitrogen_dioxide": {
        "name": "Nitrogen Dioxide",
        "formula": "NO2",
        "resonance_structures": [
            {
                "smiles": "[O-][N+]=O",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "One N=O bond and one N–O⁻ bond. Nitrogen carries a formal positive charge. The group is planar with sp² hybridized nitrogen."
            },
            {
                "smiles": "O=[N+][O-]",
                "label": "Structure 2",
                "is_major": True,
                "explanation": "Equivalent resonance form shifting the double bond to the other oxygen. Both N–O bonds have partial double-bond character in the hybrid."
            }
        ]
    },

    "sulfur_trioxide": {
        "name": "Sulfur Trioxide",
        "formula": "SO3",
        "resonance_structures": [
            {
                "smiles": "O=S(=O)=O",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "Trigonal planar geometry with all atoms sp² hybridized. Delocalization occurs via sulfur d-orbitals, giving three equivalent S–O bonds (~1.42 Å)."
            },
            {
                "smiles": "[O-][S+2](=O)[O-]",
                "label": "Structure 2",
                "is_major": False,
                "explanation": "Minor resonance form showing charge separation. Less significant but contributes to overall polarization of S–O bonds."
            }
        ]
    },

    "chlorate": {
        "name": "Chlorate Ion",
        "formula": "ClO3(-)",
        "resonance_structures": [
            {
                "smiles": "[O-][Cl](=O)=O",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "Chlorine is sp³d hybridized with three Cl–O bonds showing partial double-bond character. Negative charge delocalized across oxygens."
            },
            {
                "smiles": "O=[Cl]([O-])=O",
                "label": "Structure 2",
                "is_major": True,
                "explanation": "Equivalent form with charge placed on a different oxygen. Resonance equalizes Cl–O bond lengths (~1.50 Å)."
            }
        ]
    },

    "bicarbonate": {
        "name": "Bicarbonate Ion",
        "formula": "HCO3(-)",
        "resonance_structures": [
            {
                "smiles": "OC(=O)[O-]",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "One C=O bond, one C–O⁻, and one C–OH. Carbon is sp² hybridized. Negative charge delocalized between two oxygens."
            },
            {
                "smiles": "OC([O-])=O",
                "label": "Structure 2",
                "is_major": True,
                "explanation": "Equivalent resonance form shifting negative charge to a different oxygen. Results in equalized partial double-bond character."
            }
        ]
    },

    "water": {
        "name": "Water",
        "formula": "H2O",
        "resonance_structures": [
            {
                "smiles": "O",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "Single Lewis structure with oxygen having two lone pairs. No resonance forms exist. Bent molecular geometry with 104.5° bond angle due to sp³ hybridization."
            }
        ]
    },

    "ammonia": {
        "name": "Ammonia",
        "formula": "NH3",
        "resonance_structures": [
            {
                "smiles": "N",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "Single Lewis structure with nitrogen having one lone pair. Trigonal pyramidal geometry with 107° bond angles. sp³ hybridized nitrogen."
            }
        ]
    },

    "methane": {
        "name": "Methane",
        "formula": "CH4",
        "resonance_structures": [
            {
                "smiles": "C",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "Single Lewis structure. Tetrahedral geometry with perfect 109.5° bond angles. Carbon is sp³ hybridized with four equivalent C–H bonds."
            }
        ]
    },

    "carbon_dioxide": {
        "name": "Carbon Dioxide",
        "formula": "CO2",
        "resonance_structures": [
            {
                "smiles": "O=C=O",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "Two C=O double bonds. Linear molecular geometry (180°) with sp hybridized carbon. No net dipole moment due to symmetry."
            }
        ]
    },

    "ammonium": {
        "name": "Ammonium Ion",
        "formula": "NH4(+)",
        "resonance_structures": [
            {
                "smiles": "[NH4+]",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "Positive charge on nitrogen. Tetrahedral geometry with four equivalent N–H bonds. sp³ hybridized nitrogen with no lone pairs."
            }
        ]
    },

    "hydroxide": {
        "name": "Hydroxide Ion",
        "formula": "OH(-)",
        "resonance_structures": [
            {
                "smiles": "[OH-]",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "Negative charge on oxygen. Oxygen has three lone pairs. Strong Brønsted base. Linear O–H bond."
            }
        ]
    },

    "hydrogen_sulfide": {
        "name": "Hydrogen Sulfide",
        "formula": "H2S",
        "resonance_structures": [
            {
                "smiles": "S",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "Bent molecular geometry with 92° bond angle. Sulfur has two lone pairs. Weaker acid than water due to larger atomic size."
            }
        ]
    },

    "ethanol": {
        "name": "Ethanol",
        "formula": "C2H5OH",
        "resonance_structures": [
            {
                "smiles": "CCO",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "Common alcohol with hydroxyl group attached to ethyl chain. Oxygen is sp³ hybridized with two lone pairs. Forms hydrogen bonds."
            }
        ]
    },

    "acetic_acid": {
        "name": "Acetic Acid",
        "formula": "CH3COOH",
        "resonance_structures": [
            {
                "smiles": "CC(=O)O",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "Carboxylic acid with carbonyl and hydroxyl groups. Weak acid (pKa ~4.76). Forms dimers through hydrogen bonding."
            }
        ]
    },

    "formaldehyde": {
        "name": "Formaldehyde",
        "formula": "CH2O",
        "resonance_structures": [
            {
                "smiles": "C=O",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "Simplest aldehyde. Planar molecule with sp² hybridized carbon. Strong C=O dipole moment. Highly reactive carbonyl compound."
            }
        ]
    },

    "hydrogen_peroxide": {
        "name": "Hydrogen Peroxide",
        "formula": "H2O2",
        "resonance_structures": [
            {
                "smiles": "OO",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "Contains weak O–O peroxide bond. Non-planar structure with dihedral angle. Oxidizing agent. Decomposes to water and oxygen."
            }
        ]
    },

    "phosphate": {
        "name": "Phosphate Ion",
        "formula": "PO4(3-)",
        "resonance_structures": [
            {
                "smiles": "[O-]P([O-])([O-])=O",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "Tetrahedral geometry with sp³ hybridized phosphorus. Three negative charges distributed across four oxygens. Critical biological ion in ATP and DNA."
            },
            {
                "smiles": "O=P([O-])([O-])[O-]",
                "label": "Structure 2",
                "is_major": True,
                "explanation": "Equivalent resonance form. All P–O bonds have partial double-bond character (~1.54 Å) due to resonance delocalization."
            }
        ]
    },

    "methylamine": {
        "name": "Methylamine",
        "formula": "CH3NH2",
        "resonance_structures": [
            {
                "smiles": "CN",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "Primary amine with nitrogen having one lone pair. sp³ hybridized nitrogen. Trigonal pyramidal geometry. Weak Brønsted base."
            }
        ]
    },

    "urea": {
        "name": "Urea",
        "formula": "CO(NH2)2",
        "resonance_structures": [
            {
                "smiles": "NC(=O)N",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "Carbonyl carbon bonded to two amino groups. Planar molecule with sp² hybridized carbon. Important metabolic waste product."
            },
            {
                "smiles": "NC([O-])=[NH2+]",
                "label": "Structure 2",
                "is_major": False,
                "explanation": "Minor resonance form showing charge separation. Nitrogen lone pairs can delocalize into the carbonyl π system."
            }
        ]
    },

    "guanidinium": {
        "name": "Guanidinium Ion",
        "formula": "C(NH2)3(+)",
        "resonance_structures": [
            {
                "smiles": "NC(=[NH2+])N",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "Three amino groups bonded to central carbon. Planar structure with positive charge delocalized across all three nitrogens through resonance."
            },
            {
                "smiles": "[NH2+]=C(N)N",
                "label": "Structure 2",
                "is_major": True,
                "explanation": "Equivalent resonance form. All three C–N bonds are identical due to extensive delocalization. Very stable cation."
            }
        ]
    },

    "azide": {
        "name": "Azide Ion",
        "formula": "N3(-)",
        "resonance_structures": [
            {
                "smiles": "[N-]=[N+]=N",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "Linear three-nitrogen chain. Central nitrogen is positively charged. sp hybridized nitrogens with 180° bond angle."
            },
            {
                "smiles": "N=[N+]=[N-]",
                "label": "Structure 2",
                "is_major": True,
                "explanation": "Equivalent resonance form with charges shifted. Both N–N bonds have partial triple-bond character (~1.18 Å)."
            }
        ]
    },

    "tropylium": {
        "name": "Tropylium Cation",
        "formula": "C7H7(+)",
        "resonance_structures": [
            {
                "smiles": "C1=CC=C[CH+]C=C1",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "Seven-membered aromatic ring with positive charge. Contains 6 π electrons (Hückel rule). All carbons sp² hybridized with equal bond lengths."
            },
            {
                "smiles": "[CH+]1C=CC=CC=C1",
                "label": "Structure 2",
                "is_major": True,
                "explanation": "Equivalent resonance form showing charge delocalization around the ring. Unusually stable carbocation due to aromaticity."
            }
        ]
    },

    "cyclopentadienyl": {
        "name": "Cyclopentadienyl Anion",
        "formula": "C5H5(-)",
        "resonance_structures": [
            {
                "smiles": "[CH-]1C=CC=C1",
                "label": "Structure 1",
                "is_major": True,
                "explanation": "Five-membered aromatic ring with negative charge. Contains 6 π electrons. All carbons sp² hybridized. Highly stable anion."
            },
            {
                "smiles": "C1=C[CH-]C=C1",
                "label": "Structure 2",
                "is_major": True,
                "explanation": "Equivalent resonance form. Negative charge delocalized across all five carbons. Important ligand in organometallic chemistry."
            }
        ]
    }
}

#check for accuracy