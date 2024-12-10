# Financial Sentiment Analysis

This repository contains a Financial Sentiment Analysis project leveraging BERT-based models to classify sentiments in financial text as **Positive**, **Negative**, or **Neutral**. It includes a machine learning pipeline for data preprocessing, training, evaluation, and deployment via a Gradio-based web application.

## Features

- **Sentiment Analysis**: Classifies financial text into positive, negative, or neutral sentiments.
- **Model**: Uses a fine-tuned BERT-based model for sentiment classification.
- **Interactive Application**: A Gradio-based web interface for real-time sentiment analysis.
- **Extensive Preprocessing**: Includes text cleaning, feature extraction, and input preparation for the model.

## Repository Contents

- `.gradio/flagged`: Directory for storing flagged examples from the Gradio app.
- `.gitignore`: Specifies intentionally untracked files to ignore.
- `Financial_Sentiment_Analysis_BERT.ipynb`: Jupyter Notebook with the complete pipeline for training and evaluating the sentiment analysis model.
- `app.py`: Python script to run the Gradio-based web application.

## Getting Started

### Prerequisites

- Python 3.8+
- Recommended libraries (install via `requirements.txt`):
  - Transformers
  - Gradio
  - Pandas
  - NumPy
  - scikit-learn

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ashfaaq12/financial-sentiment-analysis.git
   ```
2. Navigate to the project directory:
    ```bash
    cd financial-sentiment-analysis
    ```
3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```