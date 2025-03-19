# Lessons in Tidy Data Principles: <br> A Tidy Data Project Based on the '08 Olympic Medalists Dataset 🥇

## Project Overview
### "Lessons in Tidy Data Principles" aims to apply tidy data principles to a very untidy version of the '08 Olympic Medalists dataset. This project is guided by three important principles of tidy data:<br>
1. Each variable forms a column. 
2. Each observation forms a row.
3. Each type of observational unit forms a table. (Wickham, 2014)<br>
### These principles are designed to create an universal language of sorts that allows data to become meaningfully structured so that it is easily used and understood by various software platforms. Some of main tasks in this project include melting to convert the dataset's orignial wide format to long format as well as splitting columns to ensure multiple variables are not present within one column. By undergoing these processes, the '08 Olympic Mdalists datset becomes much easier to use and extract insights from.

## Instructions

```
# Cloning

git clone https://github.com/aalvar23nd/tidydata-project

# Repository

cd tidydata-project

# Install Dependencies

pip install pandas seaborn matplotlib.pyplot

# Run

python main.py

```
## Dataset Desription
### This dataset is adapted from https://edjnet.github.io/OlympicsGoNUTS/2008/. The dataset shows all medalists from the 2008 Summer Olympics. The specific columns utilized in my adapted dataset are the medalist's name, their sex, and what sport they competed and won a medal in. 

## References
### For further reading on:
#### Data Wranging in Pandas: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
#### Tidy Data Principles: https://vita.had.co.nz/papers/tidy-data.pdf 
##### - Citation:
#####   - Wickham, H. (2014). Tidy Data. Journal of Statistical Software, 59(10), 1–23. https://doi.org/10.18637/jss.v059.i10

## Expected Outputs
### After running the script, the expected outputs are:<br>
#### - A display of the original dataset
#### - A tidy version of the dataset after proper cleaning functions are applied
#### - Two visualizations:
##### - A count of medals earned by type: <br> 
![Figure_1](https://github.com/user-attachments/assets/7b921617-f245-43d1-9960-6e5e61307974)
##### - A count of medals earned by type and sex: <br>
![Figure_3](https://github.com/user-attachments/assets/323d0aa7-6f1d-422c-8e34-0e538edaf072)



