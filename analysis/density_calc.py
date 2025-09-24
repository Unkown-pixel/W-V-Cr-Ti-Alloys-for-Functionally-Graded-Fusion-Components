# Density calculation for alloy candidates C, A, B
# Using volume-additive mixture rule
# Author: <Your Name or Handle>
# License: MIT

element_densities = {
    'W': 19.25,   # g/cm³
    'V': 6.11,
    'Cr': 7.19,
    'Ti': 4.51
}

compositions = {
    'C (Original)': {'W': 89.98000, 'V': 10.00000, 'Ti': 0.02000},
    'A (80/20)':    {'W': 71.98400, 'V': 26.40000, 'Cr': 0.80000, 'Ti': 0.81600},
    'B (60/40)':    {'W': 53.98800, 'V': 42.80000, 'Cr': 1.60000, 'Ti': 1.61200}
}

def density_volume_additive(comp):
    """Compute density using 1 / sum(wi/rhoi)."""
    s = 0.0
    for el, wt_percent in comp.items():
        if wt_percent == 0: 
            continue
        w_frac = wt_percent / 100.0
        rho_el = element_densities[el]
        s += w_frac / rho_el
    return 1.0 / s

if __name__ == "__main__":
    print("Density estimates (volume-additive model):")
    for name, comp in compositions.items():
        rho = density_volume_additive(comp)
        print(f"{name}: {rho:.6f} g/cm³")
