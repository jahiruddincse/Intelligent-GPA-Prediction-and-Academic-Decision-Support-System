# Intelligent GPA Prediction and Academic Decision Support System

A structured decision-support system that predicts GPA based on expected grades and helps students plan their academic strategy effectively.

---

## Overview

This project is designed to assist students in understanding and improving their academic performance. It predicts GPA using expected (user-provided) grades and recommends which subjects to prioritize in order to reach a target GPA.

The system is designed with reference to the **grading structure used at VIT Bhopal**, making it more relevant and practical for students in that academic environment.

---

## GPA System (VIT Bhopal)

The GPA calculation in this project follows the standard weighted average method used in the VIT Bhopal evaluation system.

Each subject contributes to GPA based on its credit value and assigned grade points.

Grade Points:

- S = 10  
- A = 9  
- B = 8  
- C = 7  
- D = 6  
- E = 5  
- F = 0  

### GPA Formula

*(Insert screenshot of GPA formula below)*

<!-- Add your formula screenshot here -->
![GPA Formula](images/formula.png)

---

## Methodology

The system follows a step-by-step approach:

1. Accepts subject details from the user  
2. Calculates predicted GPA using weighted average  
3. Evaluates subjects using an impact vs effort score  
4. Identifies the most effective subject to improve  
5. Performs prediction analysis using simulated grade changes  

---

## Features

- GPA prediction based on expected grades  
- Subject prioritization using scoring logic  
- Target GPA-based recommendation  
- What-if GPA prediction analysis  
- Study suggestions based on difficulty and preparation  

---

## How to Run

1. Install Python  
2. Clone this repository:
   ```bash
   git clone https://github.com/your-username/ai-gpa-prediction-system
