from flask import Flask, render_template, request
import cv2
import numpy as np
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def analyze_image(path):
    img = cv2.imread(path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    avg_color = np.mean(img_rgb, axis=(0, 1)).astype(int)
    
    r, g, b = avg_color
    tone = ""
    description = ""
    suggestions = []

    if r > g and r > b:
        tone = "🔥 Warm Tone"
        description = "You suit earthy and golden shades."
        suggestions = ["coral", "peachpuff", "gold", "olive"]
    elif b > r and b > g:
        tone = "❄️ Cool Tone"
        description = "You look best in jewel tones and icy shades."
        suggestions = ["sapphire", "lavender", "silver", "skyblue"]
    else:
        tone = "🌸 Neutral Tone"
        description = "You balance both warm and cool shades beautifully."
        suggestions = ["rose", "taupe", "mint", "navy"]

    return {
        "average": tuple(avg_color),
        "tone": tone,
        "description": description,
        "suggestions": suggestions
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    analysis = None
    uploaded_image = None

    if request.method == 'POST':
        file = request.files['file']
        if file:
            path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(path)
            uploaded_image = path
            analysis = analyze_image(path)
    
    return render_template('index.html', analysis=analysis, image=uploaded_image)

if __name__ == '__main__':
    app.run(debug=True)
