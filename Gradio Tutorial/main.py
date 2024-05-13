import random
import gradio as gr 

def classify_image(image):
    # Replace this with your actual image classification logic
    flower_types = ["Rose", "Daisy", "Sunflower"]
    return flower_types[random.randint(0, 2)]  # Random prediction for demo


# Define input and output components
image_input = gr.Image(label="Upload an image")
text_output = gr.Text(label="Predicted flower type")

# Create interface instance
interface = gr.Interface(
    fn=classify_image,
    inputs=image_input,
    outputs=text_output,
    title="Flower Classification",
    description="Upload an image of a flower and see what type it is!"
)


interface.launch()
