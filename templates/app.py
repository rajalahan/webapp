import flask
import pickle
import pandas as pd

# Use pickle to load in the pre-trained model.
with open(f'model/30june_lr_model.pickle', 'rb') as f:
    model = pickle.load(f)
    
app = flask.Flask(__name__, template_folder='templates')
@app.route('/', methods=['GET','POST'])
def main():
    if flask.request.method == 'GET':
       return(flask.render_template('main.html'))
    if flask.request.method == 'POST':
       year = flask.request.form['year']
       month = flask.request.form['month']
       day = flask.request.form['day']
       hour = flask.request.form['hour']
       minute = flask.request.form['minute']
       protypeaircanc = flask.request.form['protypeaircanc']
       protypeairdebtnote = flask.request.form['protypeairdebtnote']
       protypeairloss = flask.request.form['protypeairloss']
       protypehot = flask.request.form['protypehot']
       protypehotcanc = flask.request.form['protypehotcanc']
       protypehotdebnote = flask.request.form['protypehotdebnote']
       protypehotloss = flask.request.form['protypehotloss']
       protypeothpro = flask.request.form['protypeothpro']
       protypeothprocanc = flask.request.form['protypeothprocanc']
       protypeothprodebnote = flask.request.form['protypeothprodebnote']
       itetypeinter= flask.request.form['itetypeinter']
        
       input_variables = pd.DataFrame([[year,month,day,hour,minute,protypeaircanc,protypeairdebtnote,protypeairloss,protypehot,protypehotcanc,protypehotdebnote,protypehotloss,protypeothpro,protypeothprocanc ,protypeothprodebnote,itetypeinter]],columns=['year','month','day','hour','minute','protypeaircanc','protypeairdebtnote','protypeairloss','protypehot','protypehotcanc','protypehotdebnote','protypehotloss','protypeothpro','protypeothprocanc' ,'protypeothprodebnote','itetypeinter'],dtype=float,index=['input'])
       prediction = model.predict(input_variables)[0]
       #model = pd.read_pickle(r"C:\Users\Raja\Desktop\project\final_proj_g4\webapp\model\30june_lr_model.pickle")
       #NetFarePredicted=model.predict([[year,month,day,hour,minute,protypeaircanc,protypeairdebtnote,protypeairloss,protypehot,protypehotcanc,protypehotdebnote,protypehotloss,protypeothpro,protypeothprocanc ,protypeothprodebnote,itetypeinter]])
       #NetFarePredicted=NetFarePredicted[0]
       #print(f'NetFarePredicted:{NetFarePredicted:.2f}')
       return flask.render_template('main.html',original_input={'Year':year,'Month':month,'Day':day,'Hour': hour,'Minute':minute,'Product_Type_Air_Cancellation':protypeaircanc,'Product_Type_Air_Debit_Note':protypeairdebtnote,'Product_Type_Air_Loss':protypeairloss,'Product_Type_Hotel':protypehot,'Product_Type_Hotel_Cancellation':protypehotcanc,'Product_Type_Hotel_Debit_Note':  protypehotdebnote,'Product_Type_Hotel_Loss':protypehotloss,'Product_Type_Other_Product':protypeothpro,'Product_Type_Other_Product_Cancellation':protypeothprocanc,'Product_Type_Other_Product_Debit_Note':protypeothprodebnote,'Itenerary_Type':itetypeinter},result=prediction,)
    
if __name__ == '__main__':
    app.run()