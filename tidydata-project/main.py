import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
df_olympics = pd.read_csv("tidydata-project/data/olympics_08_medalists.csv") # Relative path for the Olympics '08 dataset

# Display Untidy Data
print("Original (Untidy) Olympics '08 Medalists Dataframe:")
print(df_olympics.to_markdown()) # Displays the orignial (untidy) dataframe, showcasing what the data actually looks like before the tidying process.

# Cleaning
## Initial Melting from Wide-format to Long-format
df_olympics_melted = pd.melt(df_olympics, id_vars = ["medalist_name"], # This is the columns that should remain fixed, as they are the names of the medalists which the medal information is based on.
                             value_vars = ["male_archery", "female_archery", "male_athletics", "female_athletics", "male_badminton", "female_badminton", "male_baseball", "male_basketball", "female_basketball", "male_boxing", "male_canoeing and kayaking", "female_canoeing and kayaking", "male_road bicycle racing", "female_road bicycle racing", "male_track cycling", "female_track cycling", "male_mountain biking", "female_mountain biking", "male_bmx", "female_bmx", "male_diving", "female_diving", "female_equestrian sport", "male_equestrian sport", "male_fencing", "female_fencing", "male_field hockey", "female_field hockey", "male_association football", "female_association football", "male_artistic gymnastics", "female_artistic gymnastics", "female_rhythmic gymnastics", "male_trampoline gymnastics", "female_trampoline gymnastics", "male_handball", "female_handball", "male_judo", "female_judo", "male_modern pentathlon", "female_modern pentathlon", "male_rowing", "female_rowing", "male_sailing", "female_sailing", "male_shooting sport", "female_shooting sport", "female_softball", "male_swimming", "female_swimming", "female_synchronized swimming", "male_table tennis", "female_table tennis", "male_taekwondo", "female_taekwondo", "male_tennis", "female_tennis", "male_triathlon", "female_triathlon", "male_beach volleyball", "female_beach volleyball", "male_volleyball", "female_volleyball", "male_water polo", "female_water polo", "male_weightlifting", "female_weightlifting", "male_freestyle wrestling", "female_freestyle wrestling", "male_greco-roman wrestling"], # Names for all the different column names in the dataset.
                             var_name = "Sport", # This is the name of the new column which holds the information from the "value_vars" previously.
                             value_name = "Medal") # This is the name of the new column that holds the inforamtion from the melted columns. In this case, it is the values (medal earned) of the different sports columns.
print(df_olympics_melted) # Displays the datset so far

## Splitting "Sport" into "Sex" and "Sport"
df_olympics_melted[["Sex", "Sport"]] = df_olympics_melted["Sport"].str.split("_", n = 1, expand = True) # The "Sex" and "Sport" columns are added to the dataset, which comes from the original "Sport" values. The values are then split by the underscore (male_archery, female_archery, etc.) to create the two columns. male_archery, for example, gets split by male, which gets added to the "Sex" column, and then by archery, which gets added to the separate "Sport" column, ensuring there is not multiple variables in one column. 
print(df_olympics_melted) # Displays the datset so far

## Removing nan Rows
df_olympics_melted = df_olympics_melted.dropna(subset = ["Medal"]) # This gets rid of the nan rows in the "Medal" column so that each medalist is not displayed for all of the sports, just the one they won a medal in. 
print(df_olympics_melted) # Displays the datset so far

## Capitalizing
df_olympics_melted["Medal"] = df_olympics_melted["Medal"].str.title() # Capitalizes the values in "Medal"
df_olympics_melted["Sex"] = df_olympics_melted["Sex"].str.title() # Capitalizes the values in "Sex"
df_olympics_melted["Sport"] = df_olympics_melted["Sport"].str.title() # Capitalizes the values in "Sport" 
df_olympics_melted.rename(columns = {"medalist_name": "Medalist_Name"}, inplace = True) # Capitalizes medalist_name

# Display Tidy Data
print(df_olympics_melted.to_markdown()) # Displays the new (tidy) dataframe, showcasing what the data actually looks like after the tidying process.

# Visualizing
sns.countplot(data = df_olympics_melted, # Data
              x = "Medal") # Pulls data from the Medal column
plt.title("Count of Medals Earned, by Type, in the '08 Olympics") # Title
plt.xlabel("Medal") # X-axis label
plt.ylabel("Count") # Y-axis label
plt.show() # Displays visualization

sns.barplot(data = df_olympics_melted, # Data
             x = "Sex", # Pulls data from the "Sex" column
             y = "Sport", # Pulls data from the "Sport" column
             hue = "Medal") # Displays different colors by type of medal
plt.title("Count of Medals Earned, by Type and Sex, in the '08 Olympics") # Title
plt.xlabel("Sex") # X-axis label
plt.ylabel("Count") # Y-axis label
plt.yticks([]) # Removes y-axes ticks
plt.show() # Displays the visualization

# Pivot-Table
pt_medals = df_olympics_melted.pivot_table( # Data
    index = "Sport",  # Groups the rows by the "Sport" data
    columns = "Sex",  # Groups the columns by the "Sex" data
    aggfunc = "size", # Counts the medals by sport and sex
    fill_value = 0)  # Switches the NaN values to 0 

# Displaying the Pivot Table
print(pt_medals) # Displays the pivot-table
