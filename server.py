from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def play():
    return render_template("index.html", boxNum = 3, color = "lightblue")

@app.route('/play/<int:boxNum>')
def play_num(boxNum):
    return render_template('index.html', boxNum=boxNum, color = "lightblue")

@app.route('/play/<int:boxNum>/<color>')
def play_color(boxNum, color):
    return render_template('index.html', color=color, boxNum=boxNum,)

@app.errorhandler(404)
def pageNotFound(missing):
    return "Sorry! No response. Try again."

if __name__=="__main__":
    app.run(debug=True)

# Second time through solution

# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template("index.html", num = 3, color = "lightblue")

# @app.route('/<int:num>')
# def num_of_boxes(num):
#     return render_template("index.html", num = num, color = "lightblue")

# @app.route('/<int:num>/<string:color>')
# def num_of_boxes_with_color(num, color):
#     return render_template("index.html", num = num, color = color)

# if __name__=="__main__":
#     app.run(debug=True)
