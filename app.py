from flask import Flask ,render_template

FAI=Flask(__name__)

@FAI.route('/First')
def First():
    return render_template('first.html')


@FAI.route('/data_render')
def data_render():
    return render_template('data_render.html',name='raj',age=22)

FAI.run(debug=True)