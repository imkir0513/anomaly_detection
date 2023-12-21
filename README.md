# anomaly_detection

This project focuses on detecting anomalies in credit card transactions, employing methods such as Logistic Regression, Isolation Forest, Decision Tree, and Naive Bayes. The goal is to identify abnormal events in a simulated credit card transaction dataset obtained from Kaggle. The study involves details about the data source, feature selection, code explanation, and model comparison, with the Decision Tree identified as the best-performing model. The practical application includes insights into fraud patterns, and the project extends to cloud architecture and security plans for scalability. The conclusion emphasizes the simplicity and accuracy of the Decision Tree model in mitigating risks and combating fraud in credit card transactions.

[Project PowerPoint](https://drive.google.com/file/d/1aRfzkz3Ce1CibNvE_z8YgL__RyDmn4oH/view?usp=sharing)
[Project Demo](https://www.youtube.com/watch?v=UPLxJ4jbBDo&ab_channel=YiboGe)

## Project structure
This project encompasses various stages, starting with data preparation, modeling, and deployment using AWS Storage & Compute services. 
<br>
1. Data Preparation <br>
During the data preparation phase, Amazon SageMaker plays a crucial role in data cleansing, which includes normalization, transformation, and featurization. The structured and sizable dataset is stored in AWS S3 to optimize system availability and speed. SageMaker's capabilities are leveraged to clean and preprocess the data efficiently, ensuring it is ready for the subsequent modeling phase. <br>

2. Modelling <br>
In the modeling phase, the prepared data is used for building and training the model. Supervised machine learning techniques are applied to detect outliers, with steps such as model fitting and threshold determination. The analysis is focused on identifying abnormal accounts, especially those suspected of fraudulent transactions.<br>

3. Deploy & Display<br>
Once the model is trained and outliers are identified, the project transitions to deployment and presentation. The model is hosted on an Amazon EC2 instance for accessibility. For an enhanced user experience, Flask is employed for deployment, allowing users to interactively search specific time periods and analyze data related to outliers. This ensures a user-friendly interface for exploring and understanding the outcomes of the anomaly detection process.

