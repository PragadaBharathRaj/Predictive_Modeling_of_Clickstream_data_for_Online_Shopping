# Predictive_Modeling_of_Clickstream_data_for_Online_Shopping
The goal is to analyze patterns within the clickstream data and predict the potential purchasing amount or price for each user. The goal is to analyze patterns within the clickstream data and label each user interaction based on the potential purchase they might make in that ongoing session


Project Phases:
Phase 1: Dataset Selection and Preprocessing
● Select a dataset suitable for supervised learning tasks.
● Perform data cleaning, normalization, and splitting into training and testing sets.
Phase 2: Exploratory Data Analysis (EDA) and Feature Selection
● Conduct EDA to understand the dataset's characteristics.
● Apply feature selection techniques to identify relevant features for modeling.
Phase 3: Model Implementation and Baseline Evaluation
● Implement at least three supervised learning algorithms (e.g., SVM, Decision Trees,
Neural Networks).
● Evaluate baseline models using initial features without hyperparameter tuning.
Phase 4: Hyperparameter Tuning
● Use techniques like grid search or random search to find optimal hyperparameters for
each model.
● Re-evaluate models with tuned hyperparameters to assess performance improvements.
Phase 5: Model Evaluation and Comparative Analysis
● Evaluate models using metrics such as accuracy, precision, recall, F1 score, and
ROC-AUC.
● Compare the performance, computational efficiency, and applicability of each algorithm.
Phase 6: Conclusion and Recommendations
● Summarize findings and insights gained from the comparative analysis.
● Provide recommendations on the most suitable algorithms for the dataset and problem
type.


- Model deployment:

The Decision Tree Regressor and KNN Classifier has been downloaded to a joblib file and deployed using a AWS EC2 instance with a free tier AWS Educational account:

URL: http://18.191.32.75:5000/
