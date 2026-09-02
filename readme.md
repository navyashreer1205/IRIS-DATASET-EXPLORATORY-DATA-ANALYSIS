# AI/ML Task 1 – Iris Dataset Exploratory Data Analysis

## 📌 Project Overview

This project is completed as part of **Task 1 – Artificial Intelligence & Machine Learning (AI/ML)**.

The objective of this task is to build a basic AI/ML development environment, strengthen Python programming fundamentals, work with datasets using Pandas, perform data cleaning, and conduct Exploratory Data Analysis (EDA).

For the practical EDA component, the **Iris Dataset** is used to understand the data, identify data-quality issues, calculate descriptive statistics, and create meaningful visualizations.

The task establishes the foundation for future machine learning activities such as preprocessing, feature engineering, model development, and evaluation.

---

## 🎯 Objectives

The main objectives of this project are:

- Set up an AI/ML development environment
- Work with Python and Jupyter Notebook
- Use NumPy and Pandas for data analysis
- Load a CSV dataset
- Inspect and understand the dataset
- Identify missing values
- Detect and remove duplicate records
- Rename columns for consistency
- Calculate descriptive statistics
- Calculate mean, median, and mode
- Analyze correlations between numerical features
- Create data visualizations
- Identify potential outliers using box plots
- Document EDA findings
- Use Git and GitHub for version control

These activities follow the practical requirements specified in Task 1. 

---

## 📊 Dataset

### Iris Dataset

The Iris dataset is used for the exploratory data analysis portion of this project.

The dataset contains measurements related to iris flowers, including numerical features such as:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

and a categorical target:

- Species

The dataset is stored in:

```text
data/iris.csv

## 🛠️ Technologies Used   

Technology	Purpose - Python Programming and data analysis
NumPy -	Numerical operations
Pandas - Data loading and manipulation
Matplotlib - Data visualization
Seaborn - Statistical visualization
Jupyter Notebook - Interactive analysis
VS Code - Development environment
Git	Version control
GitHub	Repository and project management

## 📁 Project Structure  

AIML INTERNSHIP/
│
├── data/
│   ├── iris.csv
│   └── iris_cleaned.csv
│
├── notebooks/
│   └── task1_internship.ipynb
│
├── src/
│   └── data_analysis.py
│
├── outputs/
│   ├── histogram.png
│   ├── scatter_plot.png
│   ├── box_plot.png
│   ├── correlation_heatmap.png
│   └── species_distribution.png
│
├── screenshots/
│
├── reports/
│   └── EDA_Report.pdf
│
├── .gitignore
├── requirements.txt
└── README.md

## 📈 Visualizations  

The project includes the following visualizations:

Histogram – Shows the distribution of numerical features.
Scatter Plot – Shows relationships between numerical features.
Box Plot – Helps identify spread and potential outliers.
Correlation Heatmap – Shows relationships between numerical variables.
Species Distribution – Shows the number of records belonging to each species.

The Task 1 document specifically requires a histogram, scatter plot, box plot, and correlation heatmap as part of the practical EDA work.

## EDA Workflow             
Load Dataset
      ↓
Inspect Dataset
      ↓
Check Data Quality
      ↓
Handle Missing Values
      ↓
Remove Duplicates
      ↓
Rename Columns
      ↓
Descriptive Statistics
      ↓
Correlation Analysis
      ↓
Visualization
      ↓
Identify Patterns / Outliers
      ↓
Generate Insights
      ↓
Document Findings

## 🚀 How to Run the Project   

Step 1 – Clone the Repository
git clone <https://github.com/navyashreer1205/IRIS-DATASET-EXPLORATORY-DATA-ANALYSIS>
Step 2 – Navigate to the Project
cd "AIML INTERNSHIP"
Step 3 – Create Virtual Environment
python -m venv .venv
Step 4 – Activate Virtual Environment

For Windows PowerShell:

.venv\Scripts\Activate.ps1
Step 5 – Install Required Libraries
pip install -r requirements.txt
Step 6 – Run the Python Source File
python src/data_analysis.py
Step 7 – Open the Jupyter Notebook

Open:

notebooks/task1_internship.ipynb

in VS Code and select the project's .venv Python kernel.

Run the notebook cells from top to bottom.

## 🔮 Next Step

The cleaned and analyzed dataset from Task 1 provides the foundation for subsequent machine-learning work.

The next task introduces:

Data preprocessing
Feature engineering
Dataset splitting
Baseline machine-learning models
Model evaluation

## 👩‍💻 Author

Navyashree R

AIML Student
AIML INTERNSHIP TASK 1 - @SUMMERIX GLOBAL
