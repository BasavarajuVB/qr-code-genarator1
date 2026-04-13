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
<body style="font-family: Arial; background-color: #f4f6f8; text-align: center;">

    <h2 style="color: #2c3e50; font-size: 28px;">Employee QR Generator</h2>

    <form action="/generate" method="post" style="margin-top: 30px;">
        
        <label style="font-size: 18px;">Name:</label><br>
        <input type="text" name="name" style="padding: 8px; width: 250px;"><br><br>

        <label style="font-size: 18px;">Emp Code:</label><br>
        <input type="text" name="emp" style="padding: 8px; width: 250px;"><br><br>

        <label style="font-size: 18px;">Dept:</label><br>
        <input type="text" name="dept" style="padding: 8px; width: 250px;"><br><br>

        <button type="submit" 
            style="padding: 10px 20px; font-size: 16px; background-color: #3498db; color: white; border: none; cursor: pointer;">
            Generate QR
        </button>
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
<body style="font-family: Arial; background-color: #eef2f3; text-align: center;">

    <h2 style="color: #2c3e50; font-size: 26px;">Employee Details</h2>

    <p style="font-size: 18px;"><b style="color:#000;">Name:</b> {{name}}</p>
    <p style="font-size: 18px;"><b style="color:#000;">Emp Code:</b> {{emp}}</p>
    <p style="font-size: 18px;"><b style="color:#000;">Department:</b> {{dept}}</p>

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
