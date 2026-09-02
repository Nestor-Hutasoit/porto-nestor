# Academic Grade Prediction & Explainable AI (XAI)

A machine learning project designed to predict student academic performance based on lifestyle habits, specifically analyzing the balance between gaming and study hours. This project focuses on building a stable ensemble model and using Explainable AI to interpret the predictions[cite: 10].

## Tech Stack
* **Language:** Python
* **Algorithms:** Random Forest, XGBoost, and Stacking Regressor
* **Model Evaluation:** Scikit-Learn (5-Fold Cross-Validation, GridSearchCV, RandomizedSearchCV
* **Interpretability:** SHAP (SHapley Additive exPlanations)

## Key Features
* **Feature Engineering:** Engineered a `gaming_study_ratio` feature to evaluate the impact of entertainment versus productivity on student grades.
* **Ensemble Architecture:** Evaluated and compared Random Forest (Bagging) and XGBoost (Boosting) models, alongside a Stacking Meta-Learner.
* **Hyperparameter Tuning:** Optimized model performance using GridSearchCV and RandomizedSearchCV.
* **Strict Validation:** Implemented 5-Fold Cross-Validation to analyze the bias-variance tradeoff and ensure model stability across different data splits.
* **Explainable AI:** Utilized SHAP values to visualize and explain the exact impact of each feature on the final grade prediction, identifying `gaming_study_ratio`, `study_hours`, and `sleep_hours` as the most influential factors.
