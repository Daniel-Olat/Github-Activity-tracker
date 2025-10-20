from flask import Flask, render_template, request
from main import fetch_github_data

app = Flask(__name__)
# keep a simple list of recent activities (sessionless global list)
activities = []


@app.route('/', methods=['GET', 'POST'])
def home():
  global activities
  result = None
  if request.method == 'POST':
    input_text = request.form.get('username')
    if input_text:
      result = fetch_github_data(input_text)
      # result is a list of activity strings; replace activities with latest
      activities = result or []

  return render_template('index.html', activities=activities)


if __name__ == "__main__":
  app.run(debug=True)