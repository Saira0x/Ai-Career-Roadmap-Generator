import os
import gradio as gr
from groq import Groq


# =========================
# Load Groq Client
# =========================
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))




# =========================
# AI Function
# =========================

def generate_roadmap(field, level, duration, region):

    prompt = f"""
    Create a professional and detailed career roadmap.

    Field: {field}
    Level: {level}
    Duration: {duration}
    Region: {region}

    Include:

    1. Month-wise learning plan
    2. Skills
    3. Tools
    4. Resources
    5. Projects
    6. Job roles
    7. Salary range in {region}
    8. Career advice

    Use headings and bullet points.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1400
    )

    roadmap = response.choices[0].message.content

    file_name = "career_roadmap.txt"

    with open(file_name, "w", encoding="utf-8") as f:
        f.write(roadmap)

    return roadmap, file_name


# =========================
# Custom CSS
# =========================

custom_css = """

body {
    background: linear-gradient(135deg,#020617,#0f172a,#1e293b);
    color: white;
    font-family: Segoe UI, sans-serif;
}

#title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 8px;
    background: linear-gradient(to right,#38bdf8,#818cf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

#subtitle {
    text-align: center;
    font-size: 18px;
    color: #cbd5e1;
    margin-bottom: 35px;
}

.app-card {
    background: rgba(255,255,255,0.06);
    border-radius: 18px;
    padding: 28px;
    box-shadow: 0 0 30px rgba(56,189,248,0.15);
    margin-bottom: 25px;
}

button {
    background: linear-gradient(to right,#38bdf8,#6366f1) !important;
    color: white !important;
    font-size: 16px !important;
    border-radius: 12px !important;
    padding: 12px !important;
}

button:hover {
    transform: scale(1.03);
    transition: 0.3s;
}

footer {
    text-align:center;
    margin-top:30px;
    color:#94a3b8;
    font-size:14px;
}
"""


# =========================
# UI
# =========================

with gr.Blocks() as app:

    # Header
    gr.HTML("<div id='title'>🚀 AI Career Roadmap Generator</div>")
    gr.HTML("<div id='subtitle'>Plan • Learn • Grow</div>")


    # Input Card
    with gr.Column(elem_classes="app-card"):

        with gr.Row():

            field = gr.Textbox(
                label="🎯 Career Field",
                placeholder="AI, Web Dev, Data Science..."
            )

            region = gr.Textbox(
                label="🌍 Region",
                placeholder="Pakistan, USA, UK..."
            )


        level = gr.Radio(
            ["Beginner", "Intermediate", "Advanced"],
            label="📚 Skill Level",
            value="Beginner"
        )


        duration = gr.Radio(
            ["3 Months", "6 Months", "12 Months"],
            label="⏳ Duration",
            value="6 Months"
        )


        generate_btn = gr.Button("✨ Generate Roadmap")


    # Output Card
    with gr.Column(elem_classes="app-card"):

        output_text = gr.Textbox(
            label="📘 Your Roadmap",
            lines=26
        )

        download_file = gr.File(
            label="⬇️ Download"
        )


    # Button Action
    generate_btn.click(
        fn=generate_roadmap,
        inputs=[field, level, duration, region],
        outputs=[output_text, download_file]
    )


    # Footer
    gr.HTML("""
    <footer>
    Made with ❤️ using AI | 2026
    </footer>
    """)


# =========================
# Launch (NEW WAY)
# =========================

app.launch(
    css=custom_css,
    theme=gr.themes.Soft()
)
