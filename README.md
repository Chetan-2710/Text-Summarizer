# SummarizeX: Fast API-Powered Text Summarization Engine

## About the Application

This project is an complete text summarization solution including training pipeline for finetuning, implemented using FastAPI for the backend. It includes model training, prediction, and deployment capabilities. The application is containerized using Docker, making deployment seamless and scalable.

### Features:

FastAPI Backend: High-performance API for text summarization.

End-to-End Pipeline: Includes data processing, model training, and inference.

Model Training Framework: Framework for fine-tuning transformer models from scratch on your own data.

Docker Integration: Easily deployable with a Dockerfile.

RESTful Endpoints: Structured API for training and predictions.


## What is Text Summarization?

Text summarization is the process of condensing a long piece of text into a shorter version while retaining its key information. It is commonly used in applications such as news summarization, research paper summarization, and content summarization for better readability and quick insights.


### Types of Text Summarization:

Extractive Summarization: Selects key sentences or phrases from the original text and combines them to create a summary.

Abstractive Summarization: Generates new sentences that capture the essence of the original text, similar to how humans summarize.



## How is Text Summarization Done?

Text summarization is performed using Natural Language Processing (NLP) techniques. The key steps include:

Preprocessing: Cleaning and tokenizing text data.

Feature Extraction: Identifying key phrases, words, or structures using statistical or machine learning methods.

Model Training: Using deep learning models such as Transformer-based architectures (e.g., BERT, T5, GPT) to generate summaries.

Prediction: The trained model processes input text and generates a concise summary.



# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/Chetan-2710/Text-Summarizer.git
```
### STEP 01- Create a virtual environment after opening the repository

```bash
py -3.12 -m venv textSummarizer
```

```bash
textSummarizer\Scripts\activate
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```
