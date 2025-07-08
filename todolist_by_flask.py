from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

tasks = []

# Simple HTML page template as a string
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Simple To-Do List</title>
</head>
<body>
    <h1>My To-Do List</h1>

    <form method="POST" action="/add">
        <input type="text" name="task" placeholder="Add a new task" required>
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
def home():
    # Show the to-do list page with current tasks
    return render_template_string(HTML, tasks=enumerate(tasks))

@app.route('/add', methods=['POST'])
def add():
    # Get the new task from the form and add it to the list
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete(task_id):
    # Remove the task by index if it exists
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
