# Cognitive Overload Risk Detection System

## Overview

This project predicts student overload risk using behavioral LMS interaction logs from the OULAD dataset.

Overload is defined as students who:
- Fail
- Withdraw

The model estimates overload probability using:

- total_clicks
- avg_clicks
- click_std
- avg_delay

## Model

Logistic Regression  
ROC-AUC ≈ 0.84

## Structure

- src/ → source code
- models/ → trained model (generated locally)
- data/ → dataset (not included)

## How to Run

1. Place OULAD CSV files in `data/`
2. Run training pipeline
3. Launch GUI:

GUI predictions:
![image](https://github.com/user/repo/assets/123456/abc123.png)
![image](https://github.com/user/repo/assets/123456/abc123.png)
![image](https://github.com/user/repo/assets/123456/abc123.png)
![image](https://github.com/user/repo/assets/123456/abc123.png)
