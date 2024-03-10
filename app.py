from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/combined-results', methods=['POST'])
def combined_results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']
    email = request.form['email']
    
    # Perform regex matching
    regex_matches = re.findall(regex_pattern, test_string)

    # Perform email validation
    email_regex_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    is_email_valid = re.match(email_regex_pattern, email) is not None

    return render_template('combined_results.html', test_string=test_string, regex_pattern=regex_pattern, email=email, regex_matches=regex_matches, is_email_valid=is_email_valid)

if __name__ == '__main__':
    app.run(debug=True)
