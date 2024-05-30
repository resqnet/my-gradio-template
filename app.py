import gradio as gr

def greet(name):
    return "Hello " + name + "!"

app = gr.Interface(fn=greet, inputs="text", outputs="text")
app.launch(server_name="0.0.0.0", server_port=7860, debug=True)
