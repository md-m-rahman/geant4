import matplotlib.pyplot as plt
import numpy as np

# Note: You will need 'uproot' installed to read your .root files:
# pip install uproot

def plot_absorption_coefficients():
    # Example Energy Range (eV) - matching your reference image
    energies = np.logspace(3, 8, 100) 
    
    # Mathematical models for the shapes (Placeholder logic)
    # In a real scenario, you would extract the cross-section (sigma) 
    # from your Geant4 .root files and convert to alpha (absorption coeff)
    
    # 1. Photoelectric effect: dominates at low energy (~ E^-3)
    photoelectric = 10**4 * (energies / 10**3)**-3 
    
    # 2. Compton scattering: dominates at mid energy
    compton = 0.5 * np.exp(-((np.log10(energies) - 5)**2) / 2)
    
    # 3. Pair production: starts at 1.022 MeV (approx 10^6 eV)
    pair = np.where(energies > 1.022e6, 0.05 * (np.log10(energies) - 6), 1e-10)

    # 4. Total Coefficient
    total = photoelectric + compton + pair

    # Plotting
    plt.figure(figsize=(10, 6))
    
    plt.plot(energies, total, label='Total', color='blue', linewidth=2)
    plt.plot(energies, compton, label='Compton', color='red', linestyle='--')
    plt.plot(energies, photoelectric, label='Photoelectric', color='green', linestyle=':')
    plt.plot(energies, pair, label='Pair', color='cyan', linestyle='-.')

    # Formatting to match your image
    plt.xscale('log')
    plt.yscale('log')
    plt.xlim(10**3, 10**8)
    plt.ylim(10**-6, 10**4)
    
    plt.xlabel('Incident Gamma Energy (eV)', fontsize=12)
    plt.ylabel('Absorption Coefficient (/cm)', fontsize=12)
    plt.grid(True, which="both", ls="-", alpha=0.2)
    plt.legend(frameon=False, loc='lower right', fontsize=10)
    
    # Adding text labels near curves like in the image
    plt.text(1e7, 1e1, 'Total', color='blue')
    plt.text(5e3, 5e-1, 'Compton', color='red')
    plt.text(1e7, 5e-5, 'Photoelectric', color='green')
    plt.text(5e5, 1e-6, 'Pair', color='cyan')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_absorption_coefficients()