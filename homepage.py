import streamlit as st
from transformers import AutoTokenizer
from transformers import pipeline
from src.text_summarizer.config.configuration import configManager

model_eval = configManager().get_model_evaluation_config() # Load the model evaluation configuration

tokenizer = AutoTokenizer.from_pretrained(model_eval.tokenizer_path) # Load the trained model tokenizer 
gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128} # set summary parameters

pipe = pipeline("summarization", model=model_eval.model_path,tokenizer=tokenizer) # create a pred pipeline

    
# Streamlit app
st.title("Easy Text Summarizer")
st.write("Paste your text below and click 'Summarize' to get a summary of your input.")

input_text = st.text_area("Input your text:", height=300) # Input form

if st.button("Summarize"):
    if input_text: # validate input
        summary = pipe(input_text, **gen_kwargs)[0]["summary_text"]
        
        st.write("### Summary")
        st.write(summary) # generate summary
    else:
        st.write("Please enter some text to summarize.")
