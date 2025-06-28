## 🚀 IBM Data Science Capstone Project

This repository contains 8 well-documented Jupyter notebooks that collectively aim to predict the successful landing of the Falcon 9 first stage booster. The data is sourced from public APIs and datasets, and the project follows a complete end-to-end Data Science workflow.

---

## 📁 Contents

### Notebook 1: SpaceX Falcon 9 Launch Data Collection

* Data fetched using SpaceX REST API and Wikipedia.
* Focus: Basic information extraction (launch date, site, payload, outcome).
* Output: Raw launch dataset saved to CSV.

### Notebook 2: Data Wrangling and Cleaning

* Cleaned the data: handled missing values, reformatted columns.
* Created a new binary `Class` variable for landing success (1 = Landed, 0 = Failed).

### Notebook 3: Exploratory Data Analysis (EDA)

* Univariate and multivariate analysis on payload, orbit, launch sites, etc.
* Visualized class distribution across boosters and sites using seaborn/matplotlib.

### Notebook 4: Feature Engineering

* Created dummy variables for `Orbit`, `Launch Site`, and `Booster Version`.
* Finalized dataset for machine learning with `Class` as target.

### Notebook 5: Geospatial EDA with Folium

* Visualized launch sites and their proximity to coastlines, railways, cities, and highways.
* Used `folium`, `DivIcon`, and `MousePosition` plugins.
* Calculated distance metrics using haversine formula.

### Notebook 6: Interactive Dashboard with Plotly Dash

* Built a dashboard using Dash with dropdown and range slider.
* Pie Chart: Success by site or per site.
* Scatter Plot: Payload vs. success colored by booster version.

### Notebook 7: Model Training and Testing

* Prepared feature matrix `X` and label `Y`.
* Standardized features with `StandardScaler`.
* Split data into train-test (80/20).

### Notebook 8: Model Evaluation & Comparison

* Trained and tuned 4 ML models using `GridSearchCV`:

  * Logistic Regression
  * SVM
  * Decision Tree ✅ (Best)
  * KNN
* Decision Tree with entropy, random splitter, and max depth 8 gave **94.4% accuracy** on test data.
* Visualized results with confusion matrix.

---

## 🧠 Final Model Recommendation

> **DecisionTreeClassifier** with parameters:
> `{'criterion': 'entropy', 'max_depth': 8, 'max_features': 'sqrt', 'min_samples_leaf': 2, 'min_samples_split': 2, 'splitter': 'random'}`

Best accuracy on validation set: **87.5%**
Test set accuracy: **94.44%**

---

## 🛠 Tech Stack

* Python, Pandas, NumPy, Matplotlib, Seaborn
* Plotly Dash
* Scikit-learn (ML)
* Folium (Geo-visualization)

---

## 📄 License

This project is part of the IBM Data Science Professional Certificate and is intended for educational use only.

---

## 🙌 Acknowledgements

* IBM Skills Network
* SpaceX API
* Wikipedia & Launch Library
* NASA Open Data

---


> *"Failure is an option here. If things are not failing, you are not innovating enough."* – Elon Musk
