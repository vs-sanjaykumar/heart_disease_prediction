Heart Disease Prediction Project

This project aims to predict whether an individual has heart disease or not by utilizing medical terminologies such as blood pressure (BP) level, cholesterol level, chest pain type, and other relevant medical indicators. The dataset used for this project was obtained from Kaggle.

Project Overview:

Data Collection: The dataset was fetched from Kaggle, containing various medical parameters and their corresponding target labels indicating the presence or absence of heart disease.

Data Cleaning and Preprocessing: The collected data underwent thorough cleaning and preprocessing to handle missing values, outliers, and any inconsistencies. This ensured the quality and reliability of the dataset for further analysis.

Exploratory Data Analysis (EDA): Exploratory data analysis techniques were applied to gain insights into the dataset's characteristics and relationships between variables. Visualizations were generated to understand the distribution and correlation of medical features with the target variable.

Model Building: The XGBoost machine learning model was selected for training due to its effectiveness in handling complex datasets and achieving high accuracy in classification tasks. The dataset was split into training and testing sets, and the XGBoost model was trained on the training data.

Model Evaluation: The trained model was evaluated using appropriate performance metrics to assess its predictive accuracy and generalization ability. Techniques such as cross-validation were employed to ensure robustness and reliability of the model.

Deployment: Streamlit, a web application framework, was utilized to host the trained model locally, enabling users to interact with the predictive model through a user-friendly interface. This facilitated easy access and usage of the model for making predictions.

Usage:

Clone the repository to your local machine.
Install the required dependencies listed in the requirements.txt file.
Run the Streamlit application by executing the command: streamlit run app.py.
Note: Ensure that Python and Streamlit are installed on your system before running the application.

Contributing:

Contributions to this project are welcome. Feel free to submit issues, feature requests, or pull requests to improve the functionality and usability of the Heart Disease Prediction Project.

License:

This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgments:

Kaggle for providing the heart disease dataset.
Streamlit for enabling easy deployment of machine learning models as web applications.
