from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def page2():
    html_template = '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Деплой на Heroku</title>
    <style>
        body {
            font-family: 'Segoe UI';
            background: linear-gradient(135deg, #6a11cb, #2575fc);
            margin: 0;
            padding: 20px;
            min-height: 100vh;
        }
        
        .container {
            max-width: 600px;
            margin: auto;
            background-color: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 5px 15px black;
            text-align: center;
        }
        
        h1 {
            color: #2c3e50;
            margin-bottom: 15px;
        }
        
        p {
            color: #555;
            line-height: 1.6;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Деплой на Heroku</h1>

        <div class="info">
            <h3>Информация о деплое:</h3>
            <p>Конфигурация сервера: <code>heroku.yml</code></p>
        </div>
    </div>
</body>
</html>
    '''
    return render_template_string(html_template)

if __name__ == "__main__":
    app.run(debug=True)