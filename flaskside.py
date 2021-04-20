from flask import Flask, jsonify, request, render_template
app = Flask(__name__)

@app.route('/hello', methods=['GET','POST'])
def hello():
   
      if request.method == 'POST': 
              print('Incoming..')
              print(request.get_json())
              return 'OK', 200
      else:
          message = {'getting':'Hello from Flask!'}
          return jsonify(message) 
@app.route('/test')
def test_page():
 
      return render_template('index.html') 

if __name__=="__main__":

        app.run(debug=True) 
