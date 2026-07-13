# CITES Wild-Sourced Mammal Trade - EDA Project

An exploratory data analysis of the international legal trade in wild-sourced mammals, using data from the CITES Trade Database (2016–2024).

## Dashboard\_Deployed

https://eda-with-pandas-cites-wild-sourced-mammal-trade.streamlit.app/

## Dataset

* **Source**: [CITES Trade Database](https://trade.cites.org/)
* **Filters applied**: Net imports · Class Mammalia · Source W (wild-caught) · Years 2015–2024
* **Size**: 17,535 raw rows --> 34,374 records after cleaning and reshaping to long format

## Files

|File|Description|
|-|-|
|`Ebrahim_Maki_EDA_Project_Notebook.ipynb`|Jupyter notebook - cleaning, visualization, and findings|
|`Ebrahim_Maki_EDA_Project_Presentation.pptx`|Presentation slides|
|`net_imports_2026-07-11 19_22_comma_separated.csv`|Raw dataset downloaded from CITES|

## How to run

```bash
pip install pandas matplotlib
jupyter notebook Ebrahim_Maki_EDA_Project_Notebook.ipynb
```

Then click **Run All**.

## Problem statement

> Legal wild-mammal trade is steady, concentrated in wealthy Western demand, and dominated by hunting trophies of iconic species - elephants, leopards, and lions.

## Author

Ebrahim Maki - General Assembly Data Science Bootcamp

