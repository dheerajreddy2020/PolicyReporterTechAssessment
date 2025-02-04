# Technical Assignment

This project contains solutions for two assignments:

1. **Assignment 1:** Finding the best confidence threshold that yields a recall of at least **0.9**.
2. **Assignment 2:** Implementing a **Finite State Machine (FSM)** to compute the remainder when a binary string is divided by 3.

Each assignment is implemented separately with unit tests.

---

## **Project Structure**
```
technical_assignment/
│── Assignment1/
│   │── best_threshold.py        # Function implementation
│   │── test_cases.py   # Unit tests
│
│── Assignment2/
│   │── fsm.py         # FSM class implementation
│   │── test_cases.py    # Unit tests
│
│── README.md                    # Project documentation
```

---

## **1. Clone the Repository**
To get started, clone this repository:

```sh
git clone https://github.com/dheerajreddy2020/PolicyReporterTechAssessment.git
cd PolicyReporterTechAssessment
```

---

## **2. Initialize and Activate Python Environment**
It is recommended to use a virtual environment for running this project.

#### **For Windows (cmd/PowerShell)**
```sh
python -m venv venv
venv\Scripts\activate
```

#### **For macOS/Linux (Terminal)**
```sh
python3 -m venv venv
source venv/bin/activate
```

---

## **3. Install Requirements (Optional)**
This project does **not** have external dependencies. However, if needed, install packages using:

```sh
pip install -r requirements.txt
```
(Note: `requirements.txt` is not required for this project.)

---

# **Assignment 1: Best Threshold Selection**
This function finds the best confidence threshold that yields a recall of at least **0.9**.

### **Run the Function**
To use the function in a script:
```python
from Assignment1.best_threshold import best_threshold

threshold_data = {
    0.1: {"TP": 90, "TN": 50, "FP": 10, "FN": 10},  # Recall = 0.9
    0.2: {"TP": 85, "TN": 60, "FP": 15, "FN": 5},   # Recall = 0.944
}

print(best_threshold(threshold_data))  # Output: 0.1
```

### **Run Tests**
To execute test cases, run:
```sh
python Assignment1/test_cases.py
```

---

# **Assignment 2: Modulo Three FSM**
This assignment implements a **Finite State Machine (FSM)** to determine the remainder when a binary string is divided by 3.

### **Run the FSM**
To use the FSM in a script:
```python
from Assignment2.fsm import mod_three_fsm

print(mod_three_fsm('1101'))  # Output: 1
print(mod_three_fsm('1110'))  # Output: 2
print(mod_three_fsm('1111'))  # Output: 0
```

### **Run Tests**
To execute unit tests, run:
```sh
python Assignment2/test_cases.py
```

---

## **License**
This project is for evaluation purposes. No license required.

---

## **Author**
Dheeraj Reddy  
