# Intelligent GPA Prediction and Academic Decision Support System

A structured, AI-inspired system that predicts GPA based on expected grades and helps students make smarter academic decisions.

The system predicts GPA based on the expected grades entered by the user. It analyzes each subject using credits, difficulty, and preparation level. A score is calculated to identify which subjects have the highest impact.
Based on this, it suggests where to focus for better academic performance.

---

## 1. Overview

This project helps students estimate their GPA using expected (predicted) grades and plan their study strategy effectively.

Instead of studying all subjects randomly, the system identifies which subjects will give maximum improvement with minimum effort.

It is designed based on the VIT Bhopal GPA system, making it practical for real academic use.

---

## 2. Problem Statement

Students often struggle with:

- Which subject should I focus on?  
- How can I improve my GPA efficiently?  
- What will my GPA be based on my preparation?  

This project provides a structured and logical solution to these problems.

---

## 3. Objectives

- Predict GPA based on expected grades  
- Identify high-impact subjects  
- Suggest best subject to improve  
- Help achieve a target GPA  
- Provide a structured study strategy  

---

## 4. GPA System (VIT Bhopal)

The GPA is calculated using a weighted average method:

### Grade Points

- S = 10  
- A = 9  
- B = 8  
- C = 7  
- D = 6  
- E = 5  
- F = 0  

### GPA Formula

(Add your GPA formula screenshot below)

![GPA Formula](images/formula.png)

---

## 5. Methodology

The system works in the following steps:

1. Take subject details as input  
2. Calculate predicted GPA  
3. Compute subject priority (impact vs effort)  
4. Suggest best subject to improve  
5. Perform GPA prediction analysis  

---

## 6. Algorithm

1. Input number of subjects  
2. Store subject details (credits, grade, difficulty, preparation)  
3. Calculate GPA using:

   GPA = Σ(grade_points × credits) / Σ(credits)

4. For each subject:
   - Impact = credits × (10 − grade point)  
   - Effort = difficulty + (5 − preparation)  
   - Score = impact / (effort + 1)  

5. Sort subjects based on score (descending)  
6. Simulate improving each subject to grade “S”  
7. Select subject giving best GPA improvement  
8. Display recommendation and analysis  

---

## 7. Features

- GPA prediction based on expected grades  
- Subject prioritization using scoring  
- Target GPA planning  
- What-if GPA analysis  
- Study suggestions  
- Simple terminal interface  

---

## 8. Screenshot

## 9. How to Run

1. Install Python  
2. Clone the repository:
   ```bash
   git clone https://github.com/jahiruddincse/Intelligent-GPA-Prediction-and-Academic-Decision-Support-System
