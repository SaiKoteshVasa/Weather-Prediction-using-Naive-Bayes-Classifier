# Weather-Prediction-using-Naive-Bayes-Classifier
# Introduction
Weather prediction is a crucial aspect of modern society, impacting various sectors such as agriculture, transportation, and disaster management. Accurate weather forecasts help farmers plan their activities, airlines ensure safe flights, and emergency services prepare for natural disasters, thereby saving lives and resources. The ability to predict weather patterns effectively can significantly enhance decision-making processes and improve overall efficiency in numerous fields.

The model is trained on historical weather data, which includes features such as temperature, humidity, and wind speed. The Naive Bayes Classifier uses this data to learn the relationships between the features and the weather outcomes. This repository includes all necessary code, from data preprocessing to model evaluation, providing a comprehensive guide for replicating and understanding the weather prediction process.


# Dataset
**Dataset Link :** https://drive.google.com/file/d/16lK22GNAuWSOpIAg_25ISxPJHyon1I2k/view?usp=sharing
There are 6 variables corresponding to 6 columns in the dataset:

4 variables indicating weather conditions including: precipitation, temp_max, temp_min, wind
- 1 variable to record date information: date has the form **YYYY-MM-DD**
- The variable _precipitation_ indicates the precipitation information of all forms of water falling to the ground such as rain, hail, snowfall or drizzle.
- The _temp_max_ variable indicates the highest temperature of the day.
- The _temp_min_ variable indicates the lowest temperature of the day.
- The _wind_ variable stores wind speed information for the day.
- The _weather_ defines the weather of the day


# Implementation Steps
1. **Data Collection and Preprocessing:**
   - Collect dataset containing historical weather data, including features such as temperature, humidity, wind speed, and weather conditions.
   - Perform data cleaning to handle missing values, normalize the data, and ensure the dataset is ready for analysis.
2. **Exploratory Data Analysis:**
   - Visualize the data to understand the distribution and relationships between different features.
   - Use plots and graphs to identify patterns and insights that can inform the model-building process.
3. **Model Building:**
   - Split the data into training and testing sets to evaluate the model's performance.
   - Implement the Naive Bayes Classifier using the Scikit-learn library in Python.
   - Train the model on the training dataset to learn the relationships between the features and the weather conditions.
4. **Model Evaluation:**
   - Test the model on the testing dataset to assess its accuracy and performance.
   - Use evaluation metrics such as accuracy score, confusion matrix, and classification report to determine the model's effectiveness.


# Conclusion
With an accuracy score of 82%, this model demonstrates the effectiveness of the Naive Bayes Classifier in predicting weather conditions. The repository includes all necessary code, from data preprocessing to model evaluation, providing a comprehensive guide for replicating and understanding the weather prediction process.
   

