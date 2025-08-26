# Environment Setup

You have two easy options:

## Option A — IBM Quantum Platform (no local install)
1. Create a free account: https://quantum-computing.ibm.com/
2. Open **Quantum Lab** (managed Jupyter environment).
3. Upload the notebooks from this pack and run them.

## Option B — Local (Python 3.10+ recommended)
```bash
python3 -m venv .quantum-workshop
source .quantum-workshop/bin/activate  # Windows: .venv\Scripts\activate
pip install qiskit 
pip install qiskit-aer 
pip install qiskit-ibm-runtime 
pip install matplotlib
```
> If `qiskit_ibm_runtime` fails, try: `pip install qiskit-ibm-runtime`
ZZTIh0DoSrJ0uGUvR5dPReePzo5ROUs8kWNQ3aVi4TOE
## Connect to IBM Quantum hardware
- In the new Runtime model (recommended):
  1. Get an API token from your IBM Quantum account settings.
  2. Do **once** on your machine:
     ```python
     from qiskit_ibm_runtime import QiskitRuntimeService
     QiskitRuntimeService.save_account(channel="ibm_quantum", token="YOUR_TOKEN_HERE", overwrite=True)
     ```
  3. In code, create the service:
     ```python
     service = QiskitRuntimeService()
     ```
