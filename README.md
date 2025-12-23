# Predicting LEGO Investment Values with Historical Price Data

## Project Overview
This project applies data analytics and machine learning techniques to analyze the secondary market performance of LEGO sets. Using historical pricing data and measurable set characteristics—such as age, price per piece, piece count, and minifigure count—the project predicts aftermarket value ratios and classifies LEGO sets as investment-worthy.

The goal of this project is to support data-driven decision-making for LEGO investors by replacing intuition-based purchasing strategies with reproducible, analytical insights.

This repository was developed as part of the **WGU D502 Data Analytics Capstone** and is structured to be fully reproducible.

---

## Repository Structure

<details>
<summary><strong>Click to expand</strong></summary>
<br>


```text
.
├── data/
│   ├── raw/
│   │   └── Kaggle_LEGO_DATASET.csv
│   ├── processed/
│   │   └── lego_model_ready.csv
│   └── README.md
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_analysis.ipynb
├── src/
│   └── make_dataset.py
├── environment.yml
├── README.md
└── .gitignore
```

</details> 


## Data Source

The dataset used in this project is publicly available and licensed under the MIT License.

 - Source: Kaggle
 - Dataset: LEGO Sets and Prices Over Time
 - Link: https://www.kaggle.com/datasets/alexracape/lego-sets-and-prices-over-time

Both the raw dataset and the processed modeling dataset are included in this repository to ensure full reproducibility for academic evaluation.

## Environment Setup

This project uses conda for environment management.
All required Python libraries, including pandas, NumPy, scikit-learn, matplotlib, and seaborn, are specified in the provided environment.yml file.


### 1. Clone the Repository

```bash
git clone git@github.com:BlinkingHeimdall/Predicting-LEGO-Investment-Values-with-Historical-Price-Data.git
cd Predicting-LEGO-Investment-Values-with-Historical-Price-Data
```

### 2. Create and Activate the Environment

```bash
conda env create -f environment.yml
conda activate lego-invest
```

### 3. Register Jupyter Kernel

```bash
python -m ipykernel install --user --name lego-invest --display-name "Python (lego-invest)"
```

## Recommended Execution Order

To fully reproduce the project from raw data to final results, execute the components in the following order:

1. `notebooks/01_eda.ipynb` – Exploratory analysis of the raw dataset
2. `src/make_dataset.py` – Data cleaning and feature engineering
3. `notebooks/02_analysis.ipynb` – Model training, evaluation, and visualization

## Exploratory Data Analysis (EDA)

Exploratory Data Analysis (EDA) is conducted prior to data cleaning and modeling to understand the structure, distributions, and limitations of the raw dataset.

The EDA process includes:
- Examining summary statistics for key numeric variables
- Identifying missing values and inconsistent formatting
- Analyzing skewness and extreme values in aftermarket prices
- Exploring relationships between LEGO set characteristics and aftermarket value ratios

The findings from EDA directly informed the data preparation logic implemented in `src/make_dataset.py`, including:
- Converting missing minifigure counts to zero rather than removing records
- Filtering invalid pricing records
- Applying a logarithmic transformation to the target variable to address skewness

The EDA can be reproduced by running:

```bash
jupyter notebook notebooks/01_eda.ipynb
```

## Data Preparation

The processed modeling dataset can be recreated at any time using the provided script.
```bash
python src.make_dataset.py
```

This script:
- Cleans and validates numeric fields
- Converts missing minifigure counts to zero
- Removes invalid pricing records

- Engineers features such as:
    - Aftermarket value ratio
    - Price per piece
    - Set age (years)

- Outputs a model-ready dataset to:
    - data/processed/lego_model_ready.csv

## Running the Analysis

Launch Jupyter Notebook:
```bash
jupyter notebook
```

Run the following notebook:
01_analysis.ipynb
- Linear regression
- Log-transformed regression
- Random Forest regression
- Random Forest classification
- Model evaluation and visualizations

For classification, LEGO sets are labeled as investment-worthy when the aftermarket value ratio is greater than or equal to 2.0.

## Methods Used

- Supervised Regression
    - Linear Regression
    - Log-Transformed Linear Regression
    - Random Forest Regression

- Supervised Classification
    - Random Forest Classifier

- Evaluation Metrics
    - R²
    - Mean Absolute Error (MAE)
    - Root Mean Squared Error (RMSE)
    - Accuracy
    - Precision
    - Recall
    - F1-Score

- Visualization
    - Feature importance bar charts
    - Predicted vs. actual scatter plots
    - Confusion matrix heatmaps
    - Distribution and relationship plots using Seaborn


## Reproducibility Notes

- All dependencies are defined in environment.yml
- All data used in the analysis is included in the repository
- No external API calls or credentials are required
- All scripts and notebooks run top-to-bottom in a fresh clone

## License

This project is for academic use.
The dataset used is licensed under the MIT License as provided by the original Kaggle source.

## Author
Jason Adams
WGU - Data Analytics Capstone

![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![image](https://img.shields.io/badge/license-MIT-brightgreen)