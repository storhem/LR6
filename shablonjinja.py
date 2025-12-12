from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def page1():
    data = {
        "title": "Jinja 2",
        "header": "Добро пожаловать на страницу, созданную с шаблоном Jinja 2!",
        "description": "Это демонстрация работы наследования шаблонов и передачи данных.",
        "info": {
            "style_file": "static/css/style.css",
            "template_file": "templates/base.html"
        },
        "features": [
            "Наследование шаблонов",
            "Передача данных из Python",
            "Встроенные стили и CSS"
        ]
    }
    return render_template('page1.html', **data)

if __name__ == "__main__":
    app.run(debug=True)