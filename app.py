#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, request
import os 
import replicate

os.environ["REPLICATE_API_TOKEN"] ="r8_Gy3iXMAZ0YI7f4NOzglvYYBWCnoYeo03wcQXl"
model = replicate.models.get("tstramer/midjourney-diffusion")
version = model.versions.get("436b051ebd8f68d23e83d22de5e198e0995357afef113768c20f0b6fcef23c8b")

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        q = request.form.get("q")
        inputs={"prompt":q}
        output=version.predict(**inputs)
        return(render_template("index.html",result=output[0]))
    else:
        return(render_template("index.html",result="waiting"))
    
if __name__== "__main__":
    app.run()


# In[ ]:




