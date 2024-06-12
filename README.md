### This is hosted on both  ~~AWS~~ and streamlit

~~http://54.226.187.124:8501/~~ 
(AWS will charge for public IPs after February 2024, so this won't last long)
or
https://llmresume.streamlit.app/


# Improve your resume using LLM

Powered by Google Gemini Pro

    Paste the job description and upload your resume to obtain insights, including: 
        1. an overall match percentage; 
        2. key skills that should be highlighted in your resume; 
        3. identification of keywords from the job description that are not present in your resume.

### To start

Make sure docker is installed, otherwise run installdocker.sh first:
```bash
sh installdocker.sh
```
Build docker image and start container:
```bash
docker compose up
```

