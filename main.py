import numpy as np
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit_aer.noise import NoiseModel, depolarizing_error

backend = Aer.get_backend("qasm_simulator")

def bell_state_circuit():
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    return qc

def apply_measurement_basis(qc, qubit, basis_angle_rad):
    qc.ry(-basis_angle_rad, qubit)

def run_setting(theta_a, theta_b, shots=4096, noise_model=None):
    qc = bell_state_circuit()
    apply_measurement_basis(qc, 0, theta_a)
    apply_measurement_basis(qc, 1, theta_b)
    qc.measure([0, 1], [0, 1])
    tqc = transpile(qc, backend)
    job = backend.run(tqc, shots=shots, noise_model=noise_model)
    counts = job.result().get_counts()
    return counts

def correlation_E(counts, shots):
    same = counts.get("00", 0) + counts.get("11", 0)
    diff = counts.get("01", 0) + counts.get("10", 0)
    return (same - diff) / shots

def chsh_S(shots=4096, noise_model=None):
    # Standard CHSH angles for Bell state (max violation)
    # A0=0, A1=pi/2, B0=pi/4, B1=-pi/4
    A0, A1 = 0.0, np.pi/2
    B0, B1 = np.pi/4, -np.pi/4
    E_A0B0 = correlation_E(run_setting(A0, B0, shots, noise_model), shots)
    E_A0B1 = correlation_E(run_setting(A0, B1, shots, noise_model), shots)
    E_A1B0 = correlation_E(run_setting(A1, B0, shots, noise_model), shots)
    E_A1B1 = correlation_E(run_setting(A1, B1, shots, noise_model), shots)
    S = E_A0B0 + E_A0B1 + E_A1B0 - E_A1B1
    return S, (E_A0B0, E_A0B1, E_A1B0, E_A1B1)

def make_noise(p1=0.0, p2=0.0):
    noise_model = NoiseModel()
    if p1 > 0:
        noise_model.add_all_qubit_quantum_error(depolarizing_error(p1, 1), ["h", "ry"])
    if p2 > 0:
        noise_model.add_all_qubit_quantum_error(depolarizing_error(p2, 2), ["cx"])
    return noise_model

# 1) Ideal CHSH
S_ideal, Es_ideal = chsh_S(shots=8192, noise_model=None)
print("Ideal S:", S_ideal, "E terms:", Es_ideal)

p_vals = np.linspace(0, 0.20, 9)  # sweep noise intensity
S_vals = []

for p in p_vals:
    nm = make_noise(p1=p, p2=min(2*p, 0.25)) 
    S, _ = chsh_S(shots=4096, noise_model=nm)
    S_vals.append(S)

plt.figure()
plt.plot(p_vals, S_vals, marker="o")
plt.axhline(2.0, linestyle="--")          # classical limit
plt.axhline(2*np.sqrt(2), linestyle="--") # quantum max
plt.title("CHSH Bell Inequality: S vs Noise")
plt.xlabel("Depolarizing noise (p)")
plt.ylabel("CHSH S value")
plt.show()