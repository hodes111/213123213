from flask import Flask, render_template, request , redirect

from Controllers.UserController import UserController

# создать объект класса Flask
application = Flask (__name__)
# Указать маршрут приложения
@application.route('/', methods = ['POST', 'GET'])
def home():
    title = "Вход"
    message = ''
    login = request.form.get('login')
    password = request.form.get('password')
    if request.method == 'POST':
        if UserController.auth(login, password):
            return redirect('/admin')
        else:
            message = 'Не верный логин или пароль'
    return render_template('login.html',
                           title = title,
                           message = message
                           )

@application.route('/admin')
def admin():
    title = "Панель администратора"
    return render_template('admin.html',
                           title = title)
if __name__ == "__main__":
    application.run(debug=True)