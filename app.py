from dotenv import load_dotenv

load_dotenv()
import base64
import streamlit as st
import os
import io
from PIL import Image 
import pdf2image
import google.generativeai as genai

# from config import GOOGLE_API_KEY

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,pdf_cotent,prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        ## Convert the PDF to image
        images=pdf2image.convert_from_bytes(uploaded_file.read())

        first_page=images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

## Streamlit App

st.set_page_config(page_title="ATS Resume EXpert")
st.header("ATS Tracking System")
input_text=st.text_area("Job Description: ",key="input")
uploaded_file=st.file_uploader("Upload your resume(PDF)...",type=["pdf"])


if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")


# submit1 = st.button("Write a cover letter")

# submit3 = st.button("Percentage match")

# submit2 = st.button("Write a cover letter")

submit = st.button("Generate results")

input_prompt1 = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description.  
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""
#   Please share your professional evaluation on whether the candidate's profile aligns with the role.

input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then highlight keywords in the job description that miss in the resume.
"""


# input_prompt2 = """
# Given the job description and the job applicant's resume, generate a cover letter. 
# The first paragraph of the  cover letter must briefly discuss the applicant's backgroud. 
# The second paragraph discuss how the applicant fit this role based on the applicant's skillsets matches the job requirements.
# The third paragraph discuss the applicant's interest in this role and thanks for the consideration .
# """

input_prompt2 = """
You are the applicant who applied for this job and want to compose a strong coverletter to convince the employer you have the skills and the expereince for this job.
The first paragraph of the  cover letter must briefly discuss the your backgroud. 
The second paragraph discuss how the applicant fit this role based on your skillsets matches the job requirements.
The third paragraph discuss the your interest in this role and thanks for the consideration .
"""

if submit:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        # response=get_gemini_response(input_prompt1,pdf_content,input_text)
        # st.subheader("Summary")
        # st.write(response)

        response=get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("Match percentage and missing keywords")
        st.write(response)

        response=get_gemini_response(input_prompt2,pdf_content,input_text)
        st.subheader("Coverletter")
        st.write(response)

    else:
        st.write("Please uplaod the resume")


   




