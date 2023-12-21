# Anomaly Detection on Credit Card Fraud

This project aims to detect anomalies in credit card transactions using methods like Logistic Regression, Isolation Forest, Decision Tree, and Naive Bayes. The goal is to identify unusual events in a simulated credit card dataset from Kaggle. The study covers details about the data source, features, code, and model comparison, highlighting the Decision Tree as the best-performing model. Embracing AWS concepts, the practical application provides insights into fraud patterns and incorporates cloud architecture for scalability. AWS facilitates deployment and security plans, ensuring robustness. The conclusion emphasizes the simplicity and accuracy of the Decision Tree model in managing risks and combating fraud in credit card transactions within the AWS framework.

More details please go to: [[Project PowerPoint]](https://drive.google.com/file/d/1aRfzkz3Ce1CibNvE_z8YgL__RyDmn4oH/view?usp=sharing)<br>
The demo video: [[Project Demo]](https://www.youtube.com/watch?v=UPLxJ4jbBDo&ab_channel=YiboGe)

## Project structure
This project encompasses various stages, starting with data preparation, modeling, and deployment using AWS Storage & Compute services. 
<br>
1. Data Preparation <br>
During the data preparation phase, Amazon SageMaker plays a crucial role in data cleansing, which includes normalization, transformation, and featurization. The structured and sizable dataset is stored in AWS S3 to optimize system availability and speed. SageMaker's capabilities are leveraged to clean and preprocess the data efficiently, ensuring it is ready for the subsequent modeling phase. <br>

2. Modelling <br>
In the modeling phase, the prepared data is used for building and training the model. Supervised machine learning techniques are applied to detect outliers, with steps such as model fitting and threshold determination. The analysis is focused on identifying abnormal accounts, especially those suspected of fraudulent transactions.<br>

3. Deploy & Display<br>
Once the model is trained and outliers are identified, the project transitions to deployment and presentation. The model is hosted on an Amazon EC2 instance for accessibility. For an enhanced user experience, Flask is employed for deployment, allowing users to interactively search specific time periods and analyze data related to outliers. This ensures a user-friendly interface for exploring and understanding the outcomes of the anomaly detection process.

