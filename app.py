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
</head>
<body>
    <h2>Employee QR Generator</h2>
    <form action="/generate" method="post">
        Name: <input type="text" name="name"><br><br>
        Emp Code: <input type="text" name="emp"><br><br>
        Dept: <input type="text" name="dept"><br><br>
        <button type="submit">Generate QR</button>
    </form>
</body>
</html>
"""

# Show employee details
details_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Employee Details</title>
</head>
<body>
    <h2>Employee Details</h2>
    <p><b>Name:</b> {{name}}</p>
    <p><b>Emp Code:</b> {{emp}}</p>
    <p><b>Department:</b> {{dept}}</p>
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
