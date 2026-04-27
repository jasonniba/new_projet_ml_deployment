import gradio as gr
from src.model import predict_model

def predict(feature1, feature2):
    return predict_model(feature1, feature2)

demo = gr.Interface(
    fn=predict,
    inputs=[
        gr.Number(label="Feature 1"),
        gr.Number(label="Feature 2")
    ],
    outputs=gr.Number(label="Prediction"),
    title="ML Prediction App",
    description="Interface pour tester le modèle"
)

demo.launch(server_name="0.0.0.0", server_port=7860)