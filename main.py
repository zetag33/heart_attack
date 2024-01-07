import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import shapiro, levene
# We could fully do it using just matplotlib but for me the functionality of sns is sometimes simpler and more efficient

# 1. Explanation of the dataset
# You can find it in the pdf associated with the project.
# 2. Integration and selection of data of interest.
# You can find it in the pdf associated with the project, there is little to do in this phase because the dataset is already clean and prepared.

# 3.
# We load the suggested dataset
df = pd.read_csv('C:\\Users\\Usuario\\Desktop\\PR2\\heart.csv')
# Check for any nan's
nan_check = df.isna().any()
any_nan = nan_check.any()
print(any_nan)
print(df.columns)
indexes = []
# There are no NaN's in the dataset

# Let's visually inspect each column for outliers and non-coherent values, we'll do a boxplot for the continuous variables
# and a value_counts for categorical ones.
df.boxplot(column='age')
plt.title('Boxplot of age')
plt.show()
# We can see that the age has no 0, also we don't seem to see any outlier.
# Let's technically check for outliers using one of its technical descriptions.

# Calculate the IQR (Interquartile Range)
column = 'age'
Q1 = df['age'].quantile(0.25)
Q3 = df['age'].quantile(0.75)
IQR = Q3 - Q1

# Define the lower and upper bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Detect outliers
outliers = df[(df['age'] < lower_bound) | (df['age'] > upper_bound)]
if len(outliers) == 0:
    print(f'There are no outliers in the {column} variable')
else:
    print(f'There are {len(outliers)} outliers in the {column} variable')
    indexes.append(outliers.index.to_list())


# The sex column is a categorical one, so I could use a barplot or a simple value_counts, in order to visualize the frequency of its values.
# I'm not 100% sure but as I have searched 1 means male, 0 female. That's the typical convention and it seems to be also the case here.
# We can see there are nearly the double of males than females in the sample.
# There should be always no outliers in a categorical variable, else it's a typo in the data.
sns.countplot(x='sex', data=df)
plt.title('Count of Each Value in the "Sex" Column')
plt.show()

# The cp column means chest pain and it's a categorical variable ranging from 0 to 4, it describes the type of chest pain.
# The majority of the values are classified as 0 as we can visually see.
# There should be always no outliers in a categorical variable, else it's a typo in the data.
sns.countplot(x='cp', data=df)
plt.title('Count of Each Value in the "CP" Column')
plt.show()

# The trtbps column shows, resting blood pressure in mm, so it's a continuous variable, so it can contain outliers, lets check its distribution and if there are any.
df.boxplot(column='trtbps')
plt.title('Boxplot of trtbps')
plt.show()
# Let's technically check for outliers using one of its technical descriptions.

# Calculate the IQR (Interquartile Range)
column = 'trtbps'
Q1 = df['trtbps'].quantile(0.25)
Q3 = df['trtbps'].quantile(0.75)
IQR = Q3 - Q1

# Define the lower and upper bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Detect outliers
outliers = df[(df['trtbps'] < lower_bound) | (df['trtbps'] > upper_bound)]
if len(outliers) == 0:
    print(f'There are no outliers in the {column} variable')
else:
    print(f'There are {len(outliers)} outliers in the {column} variable')
    indexes.append(outliers.index.to_list())
# We can see there are 9 outliers we will make the same for each column and then inspect volumes and take a decision about how to treat them.


# The chol column shows, cholestoral in mg/dl fetched via BMI sensor
column = 'chol'
df.boxplot(column=column)
plt.title(f'Boxplot of {column}')
plt.show()
# Let's technically check for outliers using one of its technical descriptions.

# Calculate the IQR (Interquartile Range)
Q1 = df[column].quantile(0.25)
Q3 = df[column].quantile(0.75)
IQR = Q3 - Q1

# Define the lower and upper bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Detect outliers
outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
if len(outliers) == 0:
    print(f'There are no outliers in the {column} variable')
else:
    print(f'There are {len(outliers)} outliers in the {column} variable')
    indexes.append(outliers.index.to_list())


# The fbs column means: (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false), then it's a categorical variable, that will not have outliers
# We can see that the majority of the values are 0, yet there is sufficient 1 for the variable to contribute with some info in the dataset, so we'll keep the column.
column = 'fbs'
sns.countplot(x=column, data=df)
plt.title(f'Count of Each Value in the {column} Column')
plt.show()

# The restecg column means:  resting electrocardiographic results, it's a categorical variable, then it will not have outliers
# We can see that the vast majority of samples are 0 or 1.
column = 'restecg'
sns.countplot(x=column, data=df)
plt.title(f'Count of Each Value in the {column} Column')
plt.show()


# The thalach column shows, maximum heart rate achieved
column = 'thalachh'
df.boxplot(column=column)
plt.title(f'Boxplot of {column}')
plt.show()

# Calculate the IQR (Interquartile Range)
Q1 = df[column].quantile(0.25)
Q3 = df[column].quantile(0.75)
IQR = Q3 - Q1

# Define the lower and upper bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Detect outliers
outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
if len(outliers) == 0:
    print(f'There are no outliers in the {column} variable')
else:
    print(f'There are {len(outliers)} outliers in the {column} variable')
    indexes.append(outliers.index.to_list())

# The exang column means: exercise induced angina (1 = yes; 0 = no), then it's a categorical variable, that will not have outliers
column = 'exng'
sns.countplot(x=column, data=df)
plt.title(f'Count of Each Value in the {column} Column')
plt.show()


# The oldpeak column shows, previous maximum peak
column = 'oldpeak'
df.boxplot(column=column)
plt.title(f'Boxplot of {column}')
plt.show()

# Calculate the IQR (Interquartile Range)
Q1 = df[column].quantile(0.25)
Q3 = df[column].quantile(0.75)
IQR = Q3 - Q1

# Define the lower and upper bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Detect outliers
outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
if len(outliers) == 0:
    print(f'There are no outliers in the {column} variable')
else:
    print(f'There are {len(outliers)} outliers in the {column} variable')
    indexes.append(outliers.index.to_list())


# The slp column means: the slope of the peak exercise ST segment — 0: downsloping; 1: flat; 2: upsloping
# then it's a categorical variable, that will not have outliers
column = 'slp'
sns.countplot(x=column, data=df)
plt.title(f'Count of Each Value in the {column} Column')
plt.show()

# The ca column means: number of major vessels, ranging from 0 to 3, then it's a categorical variable, that will not have outliers
column = 'caa'
sns.countplot(x=column, data=df)
plt.title(f'Count of Each Value in the {column} Column')
plt.show()

# The thall column means: A blood disorder called thalassemia Value 0: NULL (dropped from the dataset previously
# Value 1: fixed defect (no blood flow in some part of the heart)
# Value 2: normal blood flow
# Value 3: reversible defect (a blood flow is observed but it is not normal),  then it's a categorical variable, that will not have outliers
column = 'thall'
sns.countplot(x=column, data=df)
plt.title(f'Count of Each Value in the {column} Column')
plt.show()

# Finally we'll visualize the target to check volumetry
column = 'output'
sns.countplot(x=column, data=df)
plt.title(f'Count of Each Value in the {column} Column')
plt.show()
# We can see that the target is really balanced, this confirms that the dataset has been specifically manufactured for the task
# because in reality that will not be like this and we should have much more 0 than 1, yet the dataset is ideal for machine learning so it is balanced.

indexes = [item for sublist in indexes for item in sublist]
indexes = set(indexes)
print(indexes, len(indexes))

# We have 19 different outliers in total, for one or for another variable.
# We have different solutions, I would propose two:
# First one simply delete all the registers that contain an outlier in any of its variables
# Second just fit some statistic constant of the variable as the value for the outlier register.
# Taken into a account that outliers are the 6.25% of the total sample, I've decided to just delete them and work with the rest of the dataset
# They seem to be genuinely extreme values due to errors or really strange cases, and I don't have the technical knowledge to check if its really
# relevant for the data, so I'll just delete them.
# We've been also able to see the position of these outliers in the boxplots I've done for each variable.
print(df)
df.drop(indexes, inplace=True)
print(df)
# 4.

# We divide the sample in two groups, output = 0 and output 1.
group_zero = df[df['output'] == 0]
group_one = df[df['output'] == 1]
# As explained in the pdf we are going to do correlation comparison between variables of both groups, hypothesis
# contrast of assumptions for both groups and also a XGBoost tree to check for rules, feature importance and
# explainability.

# 4.2.
# Checking for normality and homogeneity of the variance in the variables for each group.

# We use the shapiro test to check normality and the levene test to check for homogeneity of variances in continuous
# variables.  For categorical variables homogeneity of variances and leven test are concepts that do not apply. We could check
# if there is an association between the output value and the categorical value using chi squared test, but since its not required
# we only apply to the continous variables.

# Let's check normality and homogeneity of variance for the continuous variables. We are going to use a 5% significance level, a common one.
for variable in ['age', 'trtbps', 'chol', 'thalachh', 'oldpeak']:
    data_group_0 = df[df['output'] == 0][variable]
    data_group_1 = df[df['output'] == 1][variable]

    # Normality check
    _, p_value_group_0 = shapiro(data_group_0)
    _, p_value_group_1 = shapiro(data_group_1)

    print(f"Normality test p-values for {variable}:")
    print(f"Group 0: {p_value_group_0}")
    print(f"Group 1: {p_value_group_1}")
    if p_value_group_0 <= 0.05:
        print(f'The variable {variable} for the group 0 does not follow a normal distribution')
    else:
        print(f'The variable {variable} for the group 0 does follow a normal distribution')
    if p_value_group_1 <= 0.05:
        print(f'The variable {variable} for the group 1 does not follow a normal distribution')
    else:
        print(f'The variable {variable} for the group 1 does follow a normal distribution')
    # Homogeneity of variance check
    _, p_value_variance = levene(data_group_0, data_group_1)

    print(f"Homogeneity of variance p-value for {variable}: {p_value_variance}\n")
    if p_value_variance <= 0.05:
        print(f'The variable {variable} does not have homogeneity of variances in both groups')
    else:
        print(f'The variable {variable} has homogeneity of variances in both groups')
    # Visualization (optional)
    sns.boxplot(x='output', y=variable, data=df)
    plt.title(f'Boxplot of {variable} by Output Group')
    plt.show()

# In a nutshell:
    #- The variable age for the group 0: does not follow a normal distribution
    #- The variable age does not have homogeneity of variance between both groups(meaning they are probably different, that would mean, there are differences between groups
    # and that might be why one of them is 0 and the other 1, it's good to find that groups are different statistically.
    #- The variable trtbps for the group 0 does not follow a normal distribution.
    #- The variable thalachh for group 1 does not follow a normal distribution.
    #- The variable oldpeak does not follow a normal distribution for any of the groups.
    #- The variable oldpeak does not have homogeneity of variances in both groups.
    # - All the variables that have not been mentioned above follow a normal distribution and have homogeneity of variances between both groups.
