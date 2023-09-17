import numpy as np
import pickle
import streamlit as st

# Load the saved model
with open("C:/Users/Admin/OneDrive/Desktop/LegalEaseAI/summarizer_model.sav", "rb") as model_file:
    loaded_summarizer = pickle.load(model_file)

def legal_summarization(input_text):
     # Example text for summarization
     # Use the loaded summarizer for summarization
     summary = loaded_summarizer(input_text, max_length=160, min_length=50, do_sample=False)
     # Print the summary
     return summary[0]['summary_text']


def main():
    
    
    # giving a title
    st.title('LegalEaseAI')
    
    
    # getting the input data from the user
    
    text = st.text_input('Enter Legal Document') 
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Simplify Legal Documents'):
        diagnosis = legal_summarization(text)
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()
    