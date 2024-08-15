# import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json
from dataclasses import dataclass
import argparse

import requests
from bs4 import BeautifulSoup

from src.webscrap import get_url_content
from src.html_parser import convert_text_to_html

@dataclass
class prompt_template:
    input_prompt1: str = """
You are an skilled Applicant Tracking System scanner with a deep understanding of Applicant Tracking System functionality, 
your task is to evaluate the resume against the provided job description. 
Show  a single percentage reflecting the overall match between resume and job description. 
"""
    input_prompt2: str = """
You are an skilled Applicant Tracking System scanner with a deep understanding of Applicant Tracking System functionality, 
your task is to evaluate the resume against the provided job description. 
Find out the requirements the make this resume disqualified for this job in a list.
"""
    input_prompt3: str = """
You are an skilled Applicant Tracking System scanner with a deep understanding of Applicant Tracking System functionality, 
your task is to evaluate the resume against the provided job description. 
Find out the most critical keywords in the resume that match the job description in a list.
"""
    input_prompt4: str = """
You are submitting a resume to a job with the provided job description. 
Find out the requirements in the job description you should add to make you qualify for this job.
"""
    input_prompt5: str = """
You are the applicant who applied for this job and want to compose a strong but concise coverletter to convince the employer you have the skills and the expereince for this job.
The first paragraph of the  cover letter must briefly discuss the your backgroud. 
The second paragraph discuss how the applicant fit this role based on your skillsets matches the job requirements.
The third paragraph discuss the your interest in this role and thanks for the consideration .
"""


class Resume:
    def __init__(self) -> None:
        self.api_key = None
        self.model = None
        self.uploaded_file = None
        self.prompt = prompt_template()

    def configure_api(self):
        try:
            with open("config.json") as f:
                config = json.load(f)
                self.api_key = config["GOOGLE_API_KEY"]

        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error reading config.json: {e}")
            # Fall back to reading API key from environment variable
            load_dotenv()
            self.api_key = os.getenv("GOOGLE_API_KEY")
            if not self.api_key:
                raise ValueError("API_KEY not found in environment variables either")
            
        # Initialize the generative model
        genai.configure(api_key=self.api_key)

        self.model=genai.GenerativeModel('gemini-pro')


    def configure_pdf(self,resume_file = None):
        
        if  resume_file:
            reader=pdf.PdfReader(resume_file)
            text="resume: "
            for page in range(len(reader.pages)):
                page=reader.pages[page]
                text+=str(page.extract_text())
            return text

        else:
            try:
                with open("config.json") as f:
                    config = json.load(f)
                    resume_file = config["RESUME_FILE"]

            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"Error reading config.json: {e}")
                if not resume_file:
                    raise ValueError("resume not found!")
            reader=pdf.PdfReader(resume_file)
            text="resume: "
            for page in range(len(reader.pages)):
                page=reader.pages[page]
                text+=str(page.extract_text())
            return text

    def get_gemini_response(self,prompt,pdf,jd,temp=0.0):

        generation_config = genai.GenerationConfig(
        temperature=temp
        )
        response=self.model.generate_content([prompt,pdf,jd],generation_config=generation_config)
        return response.text

    def get_jd(self,url):
        jd="job description: "
        jd = get_url_content(url)
        return jd
    
    def run(self,resume,jd):
        # self.configure_api()
        # text=self.configure_pdf()
        
        # jd="need a phd in computer science"
        responses=[]
        responses.append(self.get_gemini_response(self.prompt.input_prompt1,resume,jd))
        responses.append(self.get_gemini_response(self.prompt.input_prompt3,resume,jd))
        responses.append(self.get_gemini_response(self.prompt.input_prompt2,resume,jd))
        responses.append(self.get_gemini_response(self.prompt.input_prompt4,resume,jd))
        responses.append(self.get_gemini_response(self.prompt.input_prompt5,resume,jd))
        return responses


def get_args():
    parser = argparse.ArgumentParser(description='optimize the resume for a job application')
    parser.add_argument("-u", "--url", help="URL of the job posting")
    parser.add_argument("-r", "--resume", default="artifacts/resume.pdf",  help="Path of user's resume.")
    # parser.add_argument("-k", "--api_key", default="os", help="LLM Provider API Keys")
    # parser.add_argument("-d", "--downloads_dir", help="Give detailed path of folder")
    # parser.add_argument("-p", "--provider", default="gemini", help="LLM provider name. support for openai, gemini, together, g4f")

    return parser.parse_args()

   
import webbrowser

if __name__ == "__main__":
    app = Resume()
    args = get_args()
    try:
        app.configure_api()
        resume=app.configure_pdf(args.resume)
        jd=app.get_jd(args.url)
        response=app.run(resume,jd)
        # print(jd)

        file_path = 'output.html'
        with open(file_path, 'w') as file:
            file.write(convert_text_to_html(response))

        webbrowser.open('file://' + os.path.realpath(file_path))
        
    except Exception as e:
        print(f"Configuration failed: {e}")


