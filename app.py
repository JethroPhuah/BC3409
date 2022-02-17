#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import request, render_template
from keras.models import load_model

import joblib
@app.route("/", methods =["GET", "POST"])
def index():
    if request.method == "POST":
        NPTA = request.form.get("NPTA")
        TLTA = request.form.get("TLTA")
        WCTA = request.form.get("WCTA")
        print(NPTA, TLTA, WCTA)
        model = load_model("bankrupt")
        pred = model.predict([[float(NPTA), float(TLTA), float(WCTA)]])
        print(pred)
        output = "The predicted chocolate taste is " + str(pred)
        return(render_template("index1.html", result = output))
    else:
        return(render_template("index1.html", result = "Predict 2"))
    


# In[ ]:


if __name__ == "__main__":
    app.run()
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




