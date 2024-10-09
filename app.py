from flask import Flask, session, request, render_template_string, abort
import re

app = Flask(__name__)
app.secret_key = 'world1'  # المفتاح السري لتشفير الجلسات

# دالة تعقيم الاسم المدخل: السماح فقط بالأحرف الأبجدية والأرقام و - و .
def sanitize_username(username):
    # التحقق إذا كان الاسم المدخل يحتوي على أحرف غير مسموح بها
    if re.search(r'[^a-zA-Z0-9\-\.\_]', username):
        abort(403)  # إذا كانت المدخلات غير صالحة، يتم رفض الوصول

    return username

@app.route('/')
def main():
    # الحصول على الكوكيز (أو تعيين 'guest' إذا لم توجد)
    username = request.cookies.get('session', 'guest')

    # تعقيم المدخل (اسم المستخدم)
    sanitized_username = sanitize_username(username)

    # إذا كان المستخدم غير موجود في الجلسة
    if 'username' not in session:
        session['username'] = sanitized_username if sanitized_username else 'guest'

    # إذا كانت الجلسة تشير إلى 'guest'، يتم رفض الوصول
    if session['username'] == 'guest':
        abort(403)

    # قالب HTML لعرض رسالة الترحيب
    template = f'''
    <html>
        <head></head>
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
    # رسالة الخطأ إذا كان المستخدم غير مصرح له
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
