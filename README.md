### This is hosted on both  ~~AWS~~ and streamlit

~~http://54.226.187.124:8501/~~ 
(AWS will charge for public IPs after February 2024, so this won't last long)
or
https://llmresume.streamlit.app/


# Improve your resume using LLM

[![Demo Page](https://img.shields.io/badge/Project-Demo-FF4B4B?logo=streamlit)](https://llmresume.streamlit.app/)
<!-- [![arxiv paper](https://img.shields.io/badge/arXiv-Paper-B31B1B?logo=arxiv)](https://arxiv.org/abs/2402.06221) -->
<!-- [![PyPI Latest Release](https://img.shields.io/pypi/v/zlm.svg?label=PyPI&color=3775A9&logo=pypi)](https://pypi.org/project/zlm/) -->
<!-- [![PyPI Downloads](https://img.shields.io/pypi/dm/zlm.svg?label=PyPI%20downloads&color=blueviolet&target=blank)](https://pypi.org/project/zlm/) -->
[![GitHub issues open](https://img.shields.io/github/issues/Ztrimus/job-llm.svg?color=orange&label=Issues&logo=github)](https://github.com/19revey/LLM_resume/issues)
[![License: MIT](https://img.shields.io/badge/License-MIT-success.svg?logo)](https://github.com/19revey/LLM_resume/blob/main/LICENSE)


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

