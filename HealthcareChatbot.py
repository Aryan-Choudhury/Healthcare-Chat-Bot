import pandas as pd
from fuzzywuzzy import process 


disease_symptoms_path = r'C:\Users\Aryan Choudhury\Desktop\ML Chatbot\DiseaseAndSymptoms.csv'
disease_precaution_path = r'C:\Users\Aryan Choudhury\Desktop\ML Chatbot\Disease precaution.csv'


disease_symptoms_df = pd.read_csv(disease_symptoms_path)
disease_precaution_df = pd.read_csv(disease_precaution_path)


symptom_columns = [f'Symptom_{i}' for i in range(1, 18)] 


def healthcare_chatbot(user_input):
    user_symptoms = [symptom.strip().lower() for symptom in user_input.split(',')]


    matched_diseases = []
    for index, row in disease_symptoms_df.iterrows():
        row_symptoms = row[symptom_columns].dropna().str.lower().tolist()
        match_count = sum(1 for user_symptom in user_symptoms if process.extractOne(user_symptom, row_symptoms)[1] >= 80)
        
    
        if match_count > 0:
            matched_diseases.append((row['Disease'], match_count))
    
  
    if not matched_diseases:
        return "No matching diseases found for the entered symptoms.", []

  
    matched_diseases.sort(key=lambda x: x[1], reverse=True)
    predicted_disease = matched_diseases[0][0]  


    precautions = disease_precaution_df[disease_precaution_df['Disease'] == predicted_disease].iloc[0, 1:].dropna().tolist()

    return predicted_disease, precautions


if __name__ == "__main__":
    print("Healthcare Chatbot: Please type your symptoms separated by commas (e.g., 'itching, skin rash').")
    user_input = input("Enter your symptoms: ")
    
    predicted_disease, precautions = healthcare_chatbot(user_input)

    if predicted_disease == "No matching diseases found for the entered symptoms.":
        print(predicted_disease)
    else:
        print(f"\nYou may have {predicted_disease}.")
        print("Here are some precautions to follow:")
        for i, precaution in enumerate(precautions, 1):
            print(f"{i}. {precaution}")
