# NLP-Sucide-Watch

The task was to develop an AI-Powered system to detect any potential self-harm or suicidal thoughts from any paragraph of text and flag it. I obtained a dataset from Kaggle and made the necessary modifications. Then, I utilised the Spacy Python library to preprocess the data. To vectorise the data, I employed the CountVectorizer. After that, I trained a machine learning model utilising the Support Vector Classifier. To obtain the optimal hyperparameters, I employed GridSearchCV and executed a grid search. I then utilised the best hyperparameters to train the final model. Finally, I saved the model and vectoriser as a .pkl file utilising the Joblib Python library to use them for constructing an API.

The web application is made using Django Python framework. It includes 2 HTML pages. The initial page enables the user to input their feelings and experiences of the day. The model subsequently executes preprocessing and identifies whether the input refers to self-harm or not. The second page displays the outcome of the model's analysis.

<img width="1440" alt="Screenshot 2023-04-17 at 14 48 15" src="https://user-images.githubusercontent.com/106950467/232442101-a4684327-1170-435e-8329-39d13650723b.png">

<img width="1440" alt="Screenshot 2023-04-17 at 14 48 23" src="https://user-images.githubusercontent.com/106950467/232442185-b72a9bf3-d602-4b51-993c-a277d443efa6.png">
