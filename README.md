# Experimental Verification of Bell Inequality Under Quantum Noise

This project implements a **CHSH Bell Inequality test** using quantum circuit simulation to demonstrate how **quantum entanglement violates classical correlations**, and how **realistic quantum noise degrades these violations**.

The goal of this project is to bridge concepts from **quantum physics** and **computer science** through hands-on experimentation using modern quantum software tools.

---

## Overview

Bell’s Inequality provides a fundamental test to distinguish **classical correlations** from **quantum entanglement**.  
In this project, we:

- Prepare an entangled Bell state
- Perform CHSH measurements using different measurement bases
- Compute correlation values from measurement statistics
- Calculate the CHSH **S-value**
- Analyze how depolarizing noise affects quantum correlations

---

## Tech Stack

- **Python**
- **Qiskit (Quantum Circuit Simulation)**
- **NumPy**
- **Matplotlib**

---

## Key Features

- Bell state preparation using quantum gates
- Implementation of CHSH measurement settings
- Calculation of expectation values from raw measurement counts
- Verification of Bell inequality violation (S > 2)
- Noise modeling using depolarizing noise
- Visualization of S-value degradation under increasing noise

---

## Results Summary

- Ideal simulation shows **CHSH S ≈ 2.7–2.83**, violating the classical bound (S ≤ 2)
- With increasing noise, S-values decrease and eventually fall below the classical limit
- Demonstrates why **noise is a major challenge** in practical quantum computing

---

## How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/Gael12227/CHSH-Bell-Inequality-Violation-Analysis-Using-Qiskit.git
cd CHSH-Bell-Inequality-Violation-Analysis-Using-Qiskit
