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
- notebooks/ → trained model
- data/ → dataset

## How to Run

1. Place OULAD CSV files in `data/`
2. Run training pipeline
3. Launch GUI:

## GUI predictions:





![image](https://github.com/sakshio-o/Cognitive-overload-risk/blob/3acc1c0c283f8aee77e44993371bb7fea461474f/Screenshot%202026-03-14%20214652.png)
![image](https://github.com/sakshio-o/Cognitive-overload-risk/blob/3acc1c0c283f8aee77e44993371bb7fea461474f/Screenshot%202026-03-14%20214824.png)
![image](https://github.com/sakshio-o/Cognitive-overload-risk/blob/3acc1c0c283f8aee77e44993371bb7fea461474f/Screenshot%202026-03-14%20215008.png)
![image](https://github.com/sakshio-o/Cognitive-overload-risk/blob/3acc1c0c283f8aee77e44993371bb7fea461474f/Screenshot%202026-03-14%20215118.png)
