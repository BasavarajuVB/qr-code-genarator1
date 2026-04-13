from flask import Flask, render_template_string, request, send_file
import qrcode
import os

app = Flask(__name__)

# Home page (Form)
form_html = """
<!DOCTYPE html>
<html>
<head>
    <title>QR Generator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #4facfe, #00f2fe);
            margin: 0;
            padding: 0;
        }

        .container {
            width: 400px;
            margin: 80px auto;
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            text-align: center;
        }

        h2 {
            margin-bottom: 20px;
            color: #333;
            font-size: 26px;
        }

        input {
            width: 90%;
            padding: 10px;
            margin: 10px 0;
            border-radius: 8px;
            border: 1px solid #ccc;
            font-size: 16px;
        }

        button {
            background: #4facfe;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            cursor: pointer;
            margin-top: 15px;
            width: 100%;
        }

        button:hover {
            background: #00c6ff;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Employee QR Generator</h2>
        <form action="/generate" method="post">
            <input type="text" name="name" placeholder="Enter Name" required>
            <input type="text" name="emp" placeholder="Enter Employee Code" required>
            <input type="text" name="dept" placeholder="Enter Department" required>
            <button type="submit">Generate QR</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(form_html)

@app.route('/generate', methods=['POST'])
def generate_qr():
    name = request.form['name']
    emp = request.form['emp']
    dept = request.form['dept']

    # URL that QR will open
    url = f"https://qr-code-genarator-rajuvb.onrender.com/details?name={name}&emp={emp}&dept={dept}"

    # Generate QR
    img = qrcode.make(url)
    file_path = "qr.png"
    img.save(file_path)

    return send_file(file_path, as_attachment=True)

@app.route('/details')
def details():
    name = request.args.get('name')
    emp = request.args.get('emp')
    dept = request.args.get('dept')

    return render_template_string(details_html, name=name, emp=emp, dept=dept)

if __name__ == '__main__':
    app.run(debug=True)
