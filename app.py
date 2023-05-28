from flask import Flask,render_template

FAI=Flask(__name__)

@FAI.route('/Jeevi')
def Jeevitha_akka():
    return render_template('jeevi.html',name='madhu',age=33)

@FAI.route('/sandi')
def Jeevitha_sandi():
    return render_template('new.html')


if __name__=='__main__':
    FAI.run(debug=True)