import parmed as pmd

protein = pmd.load_file(
    "topol.top",
    xyz="processed.gro"
)

ligand = pmd.load_file(
    "ZINC_GMX.top",
    xyz="zinc.gro"
)

complex = protein + ligand

complex.save("complex.gro")

