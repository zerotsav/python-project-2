from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

tasks = []

# HTML template as a string (so no separate files needed)
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Simple To-Do List</title>
</head>
<body>
    <h1>My To-Do List</h1>
    <form method="POST" action="/add">
        <input type="text" name="task" placeholder="Add new task" required>
        <button type="submit">Add</button>
    </form>
    <ul>
        {% for idx, task in tasks %}
            <li>{{ task }} <a href="/delete/{{ idx }}">Delete</a></li>
        {% else %}
            <li>No tasks yet!</li>
        {% endfor %}
    </ul>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML, tasks=enumerate(tasks))

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
