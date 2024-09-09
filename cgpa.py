from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            grades = request.form.getlist('grade')
            credits = request.form.getlist('credit')

            total_points = 0
            total_credits = 0

            for grade, credit in zip(grades, credits):
                grade = float(grade)
                credit = float(credit)
                total_points += grade * credit
                total_credits += credit

            cgpa = total_points / total_credits
            result = f"Your CGPA is {cgpa:.2f}"
        except ValueError:
            result = "Invalid input. Please enter valid numbers."

    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>CGPA Calculator</title>
    </head>
    <body>
        <h1>CGPA Calculator</h1>
        <form method="post">
            <div id="subjects">
                <div class="subject">
                    <label for="grade">Grade:</label>
                    <input type="text" name="grade" required>
                    <label for="credit">Credits:</label>
                    <input type="text" name="credit" required>
                </div>
            </div>
            <button type="button" onclick="addSubject()">Add Another Subject</button><br><br>
            <button type="submit">Calculate CGPA</button>
        </form>
        <br>
        {% if result %}
            <h2>Result: {{ result }}</h2>
        {% endif %}
        
        <script>
            function addSubject() {
                var div = document.createElement('div');
                div.className = 'subject';
                div.innerHTML = '<label for="grade">Grade:</label><input type="text" name="grade" required> <label for="credit">Credits:</label><input type="text" name="credit" required>';
                document.getElementById('subjects').appendChild(div);
            }
        </script>
    </body>
    </html>
    ''', result=result)

if __name__ == '__main__':
    app.run(debug=True)
