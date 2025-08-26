# Qiskit Cheat Sheet (Tiny)
- `QuantumCircuit(n_qubits, n_clbits)`
- Common gates: `h(q)`, `x(q)`, `z(q)`, `rx(theta, q)`, `cx(ctrl, tgt)`
- Measure: `measure(qreg, creg)` or `measure(q, c)`
- Simulators:
  ```python
  from qiskit import Aer, execute
  backend = Aer.get_backend("qasm_simulator")
  execute(qc, backend, shots=1024).result().get_counts()
  ```
- Draw:
  ```python
  qc.draw("mpl")  # requires matplotlib
  ```
- IBM Runtime (hardware access):
  ```python
  from qiskit_ibm_runtime import QiskitRuntimeService, Sampler
  service = QiskitRuntimeService()
  sampler = Sampler(session=None)
  job = sampler.run(qc)
  job.result()
  ```
