import numpy as np
from flask import Flask,render_template,request
import pickle
app= Flask(__name__)
file=open('wqi.pkl','rb')
random_Forest=pickle.load(file)
file.close()

app = Flask(__name__, template_folder='template') 
 # Save model
with open('wqi.pkl', 'rb') as model:
    pickle.load(model)
@app.route('/')
def home() :
  return render_template("index.html")    
@app.route('/login',methods = ['GET','POST'])
def login() :
  year = request.form["year"]
  do = request.form["do"]
  ph = request.form["ph"]
  co = request.form["co"]
  bod = request.form["bod"]
  tc = request.form["tc"]
  na = request.form["na"]
  total = [float(year),float(do),float(ph),float(co),float(bod),float(na),float(tc)]
  res=random_Forest.predict([total])[0]
  y_pred = res
  if(y_pred >= 95 and y_pred<=100):
    return render_template("index.html",showcase = 'Excellent, The Predicted Value Is'+ str(y_pred))
  elif(y_pred >= 89 and y_pred<=94):
    return render_template("index.html",showcase = 'Very Good, The Predicted Value Is'+ str(y_pred))
  elif(y_pred >= 80 and y_pred<=88):
    return render_template("index.html",showcase = 'Good, The Predicted Value Is'+ str(y_pred))
  elif(y_pred >= 65 and y_pred<=79):
    return render_template("index.html",showcase = 'Fair, The Predicted Value Is'+ str(y_pred))
  elif(y_pred >= 45 and y_pred<=64):
    return render_template("index.html",showcase = 'Marginal, The Predicted Value Is'+ str(y_pred))
  else:
    return render_template("index.html",showcase = 'Poor, The Predicted Value Is'+ str(y_pred))





if __name__ == '__main__':
    app.run(debug=False,port=5000)