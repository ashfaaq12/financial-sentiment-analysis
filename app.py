import gradio as gr
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load the fine-tuned tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("./fine_tuned_model")
model = AutoModelForSequenceClassification.from_pretrained("./fine_tuned_model")

# Define a prediction function
def predict_sentiment(text):
    inputs = tokenizer(text, padding='max_length', truncation=True, max_length=128, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=1).item()
    if predicted_class == 0:
        return "### Sentiment: **Positive**"
    elif predicted_class == 1:
        return "### Sentiment: **Neutral**"
    elif predicted_class == 2:
        return "### Sentiment: **Negative**"

css = """
body {
    background-image: url(https://img.freepik.com/free-vector/rainbow-coloured-abstract-low-poly-banner-design_1048-12818.jpg?t=st=1730701136~exp=1730704736~hmac=42af035a0d464e1c403ad38bf4a207d6d54c5b2006b2a893d9d0805d559a5d9a&w=1380);
    background-size: cover;
    color: #FF0000;
    font-family: 'Arial', sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}

h1, h2, h3, h4, h5, h6 {
    color: #FFD700;
}

.gradio-container {
    background-color: rgba(0, 0, 0, 0.7); /* Semi-transparent background */
    border-radius: 15px;
    padding: 20px;
    max-width: 600px; /* Center and control width */
    margin: auto; /* Center the container */
    text-align: center;
}

#input_box {
    width: 100%;
    max-width: 500px;
    margin: auto;
    text-align: center;
}
"""

interface = gr.Interface(
    fn=predict_sentiment,
    inputs=gr.Textbox(lines=4, label="Enter Financial Statement", placeholder="Type here..."),
    outputs=gr.Markdown(label="Sentiment Result"),
    allow_flagging="never",
    title="Financial News Sentiment Analysis",
    description="Enter a sentence about financial news to predict its sentiment. Try the examples below!",
    examples=[
        ["The company’s profits surged by 20% this quarter, surpassing analyst forecasts."],
        ["The company reported a 30% decline in sales this quarter, raising concerns about its future viability."],
        ["Market analysts predict mixed results for the upcoming quarter due to varying economic conditions."],
    ],
    css=css
)

if __name__ == "__main__":
    interface.launch()
