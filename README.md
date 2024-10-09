# Healthcare Chatbot

This healthcare chatbot is designed to predict potential diseases based on user-input symptoms and provide corresponding precautions. It utilizes symptom matching and a decision tree model to identify diseases and offer precautions from pre-defined datasets.

## Features

- **Symptom Matching**: The chatbot uses fuzzy string matching to identify the closest match between user-provided symptoms and the symptoms in the dataset.
- **Disease Prediction**: Based on the matched symptoms, the chatbot predicts the disease using a trained Decision Tree classifier.
- **Precaution Suggestions**: Once a disease is predicted, the chatbot retrieves and displays precautionary steps from a predefined dataset.

## Datasets

The project utilizes two datasets:
1. **DiseaseAndSymptoms.csv**: Contains a list of diseases along with up to 17 symptoms for each disease.
2. **Disease precaution.csv**: Contains corresponding precautionary steps for each disease.

## Project Structure
healthcare-chatbot/
├── DiseaseAndSymptoms.csv        # Dataset containing diseases and their symptoms
├── DiseasePrecaution.csv         # Dataset containing diseases and their precautions
├── chatbot.py                    # Main Python file implementing the chatbot
└── README.md                     # Project documentation



