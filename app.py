from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Load course data
with open("data.json") as f:
    data = json.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    selected_course = None
    roadmap = []
    syllabus = {}
    if request.method == "POST":
        selected_course = request.form.get("course")
        if selected_course in data["courses"]:
            roadmap = data["courses"][selected_course]["roadmap"]
            syllabus = data["courses"][selected_course]["syllabus"]
    return render_template("index.html", courses=list(data["courses"].keys()),
                           selected_course=selected_course, roadmap=roadmap, syllabus=syllabus)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
