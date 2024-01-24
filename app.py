import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

load_dotenv()


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,pdf_content,prompt):
    model=genai.GenerativeModel('gemini-pro')
    generation_config = genai.GenerationConfig(
    temperature=0.0
    )
    response=model.generate_content([input,pdf_content,prompt],generation_config=generation_config)
    return response.text

def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text

## Streamlit App

st.title("Improve your resume using LLM")
st.text("powered by Gemini pro")
jd=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod the pdf")


if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")


submit = st.button("Generate results")


input_prompt1 = """
You are an skilled Applicant Tracking System scanner with a deep understanding of Applicant Tracking System functionality, 
your task is to evaluate the resume against the provided job description. 
First, show  a single percentage reflecting the overall match between resume and job description. 
Second, highlight the most critical key skills in the job description and assess how much the resume has shown these skills in the resume.
Third, key skills missing: show keywords in the job description that miss in the resume.
"""
#give me the percentage of match if the resume matches the job description.  First the output should come as percentage and then highlight keywords in the job description that miss in the resume.

input_prompt2 = """
You are the applicant who applied for this job and want to compose a strong but concise coverletter to convince the employer you have the skills and the expereince for this job.
The first paragraph of the  cover letter must briefly discuss the your backgroud. 
The second paragraph discuss how the applicant fit this role based on your skillsets matches the job requirements.
The third paragraph discuss the your interest in this role and thanks for the consideration .
"""


if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)

        response=get_gemini_response(input_prompt1,text,jd)
        st.write(response)

        response=get_gemini_response(input_prompt2,text,jd)
        st.subheader("Coverletter")
        st.write(response)

    else:
        st.write("Please uplaod the resume")


   




