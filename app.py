from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

# ✅ Configure your Gemini API key
genai.configure(api_key="AIzaSyD80Eg8SAtKJ9SvafOULUbGDg33i7MQjnw")

# ✅ Use a valid Gemini model (check available models)
model = genai.GenerativeModel("models/gemini-2.5-flash")

@app.route("/", methods=["GET", "POST"])
def home():
    advice = ""
    if request.method == "POST":
        # Get user input safely
        user_question = request.form.get("user_question", "")
        if user_question.strip():
            try:
                # Ask Gemini model for beauty advice
                prompt = f"You are a beauty consultant. Provide detailed and practical advice for the following question:\n{user_question}"
                response = model.generate_content(prompt)
                advice = response.text
            except Exception as e:
                advice = f"⚠️ Error generating advice: {e}"
    return render_template("index.html", advice=advice)

if __name__ == "__main__":
    app.run(debug=True)
