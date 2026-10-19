from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

qc = QuantumCircuit(1)
qc.h(0)

qc.measure_all()

qc.draw("mpl")
plt.show(block=False)

sim = AerSimulator()
counts = sim.run(qc, shots=500).result().get_counts()

total_shots = sum(counts.values())

print("Counts:", counts, "(Total: ", total_shots, ")")

probabilities = {state: count / total_shots for state, count in counts.items()}

print("Probabilities:", probabilities)

plot_histogram(probabilities)

plt.show()