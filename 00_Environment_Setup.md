# Environment Setup

You have two easy options:

## Option A — IBM Quantum Platform (no local install)

1. Create a free account: <https://quantum-computing.ibm.com/>
2. Open **Quantum Lab** (managed Jupyter environment).
3. Upload the notebooks from this pack and run them.

## Option B — Local Setup

```bash
# Create conda environment with Python 3.12
conda create -n quantum-workshop python=3.12 -y
conda activate quantum-workshop

# Install Jupyter and quantum computing packages
conda install jupyter notebook ipykernel -y
pip install qiskit qiskit-aer qiskit-ibm-runtime matplotlib

conda install -c conda-forge jupyterlab
# Register the environment as a Jupyter kernel
python -m ipykernel install --user --name quantum-workshop --display-name "Python (quantum-workshop)"
```


> **Note:** The last step registers your conda environment as a Jupyter kernel so you can select it in notebooks.

## Connect to IBM Quantum hardware

- In the new Runtime model (recommended):
  1. **Create a free IBM Quantum account** at <https://quantum-computing.ibm.com/>
  2. **Join the IBM Quantum Network** (free access to simulators and limited hardware):
     - Sign in to your IBM Quantum account
     - Look for "Join IBM Quantum Network" or go to the "Plans" section
     - Select the free "Open Plan" to get access to quantum backends
  3. **Get your API token** from your IBM Quantum account settings.
  4. **Run the setup script** once on your machine:

     ```bash
     # With conda environment activated
     conda activate quantum-workshop
     python setup_ibm_quantum.py
     
     # Or with venv activated
     # source .quantum-workshop/bin/activate
     # python setup_ibm_quantum.py
     ```

     This interactive script will:
     - Guide you through getting your API token
     - Save your credentials securely
     - Test the connection and show available backends
  5. **In code, create the service:**

     ```python
     from qiskit_ibm_runtime import QiskitRuntimeService
     service = QiskitRuntimeService()
     ```
