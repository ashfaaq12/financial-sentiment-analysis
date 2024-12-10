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
Usage

### 1. Run the Jupyter Notebook:
- Open ```Financial_Sentiment_Analysis_BERT.ipynb``` to train or fine-tune the BERT model and evaluate its performance.

### 2. Launch the Gradio App:
-    Start the web application for real-time sentiment analysis:
    
- ``` bash
    python app.py
    ```
-   Open your browser and go to the URL provided by Gradio (e.g., http://127.0.0.1:7860).

### 3. Input Sentences:

-    Enter financial-related text to analyze the sentiment.

### Model Information
The model is based on a pre-trained BERT variant and fine-tuned for financial sentiment classification. The following dataset columns were utilized:

-    ```Sentence```: The financial text to classify.
-   ```Sentiment```: Target labels with classes (0: Negative, 1: Neutral, 2: Positive).
-    ```text_length``` and ```word_count```: Auxiliary features used during exploration.

### Results
-  Best Accuracy: Achieved using a fine-tuned model with [Model Details].
-  Deployment: The model is deployed in an interactive Gradio app for demonstration.
  
### Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests. For significant changes, please open an issue first to discuss what you'd like to change.

### Acknowledgments
-    Hugging Face Transformers
-    Financial datasets from various sources
-    Gradio for building the web application

### Contact
For questions or feedback, please contact ashfaaqkk12@gmail.com.