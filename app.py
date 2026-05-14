from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>SecureStack Project</title>
        <style>
            body{
                font-family: Arial;
                background:#f2f2f2;
                display:flex;
                justify-content:center;
                align-items:center;
                height:100vh;
            }

            .box{
                background:white;
                padding:40px;
                border-radius:10px;
                text-align:center;
                box-shadow:0px 0px 10px gray;
            }

            input{
                padding:10px;
                width:250px;
                margin-top:10px;
            }

            button{
                padding:10px 20px;
                margin-top:15px;
                background:blue;
                color:white;
                border:none;
                border-radius:5px;
            }
        </style>
    </head>

    <body>
        <div class="box">
            <h1>Welcome to My Website</h1>
            <p>This website is deployed securely for cybersecurity internship project.</p>

            <input type="text" placeholder="Enter your name"><br>

            <button>Submit</button>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)