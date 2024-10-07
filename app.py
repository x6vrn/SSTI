from flask import Flask, session, request, make_response, render_template_string, abort
import os
os.system('echo "BBJ{1t5_3a5y_55t1?}" > flag.txt')
app = Flask(__name__)
app.secret_key = 'world1' 

@app.route('/')
def main():
    username = request.cookies.get('session')
    
    if 'username' not in session:
        session['username'] = username if username else 'guest' 

    if session['username'] == 'guest':
        abort(403)

    template = f'''
    <html>
        <head>
        </head>
        <body style="font-family: 'Arial', sans-serif; background-color: #121316; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0;">
            <div style="background-color: #181A1D; padding: 20px; border-radius: 10px; border: solid 0.2px rgb(70, 70, 70); text-align: center;">
                <h1 style="font-size: 26px; color: rgb(255, 255, 255);">Welcome, {session['username']}!</h1>
            </div>
        </body>
    </html>
    '''
    return render_template_string(template)

@app.errorhandler(403)
def unauthorized(error):
    return '''
    <html>
    <head>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                background-color: #121316;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }

            .error-container {
                background-color: #181A1D;
                padding: 20px;
                border-radius: 10px;
                border: solid 0.2px rgb(70, 70, 70);
                text-align: center;
            }

            .pargraph {
                color: white;
            }

            h1 {
                font-size: 26px;
                color: rgb(255, 185, 185);
            }        
        </style>
    </head>
    <body>
        <div class="error-container">
            <h1>403 Unauthorized</h1>
            <p class="pargraph">You do not have permission to access this page.</p>
        </div>
    </body>
    </html>
    ''', 403

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=9090)
