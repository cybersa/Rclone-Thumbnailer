from flask import Flask
from flask import render_template
from flask import flash, request, redirect, url_for
import requests
import json
from werkzeug.utils import secure_filename
import os
from utils import thumbnail
import urllib.parse

api_url="http://localhost:5572"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "temp"


@app.context_processor
def utility_processor():

    #Check if file exists
    def is_exists(s):
        return os.path.exists(s)

    # URL Encode
    def url_encode(s):
        return urllib.parse.quote(s)

    return dict(is_exists=is_exists,url_encode=url_encode)



@app.route("/view/<remote>")
def list_remotepath_files(remote):

    path=""
    if "path" in request.args:
        path=request.args["path"]

    data=list_files(remote,path)
    print(data)
    return render_template("index.html",files=data["list"],api_url=api_url,remote=remote,path=path) 

@app.route("/")
def list_remotes():    
    data=requests.post("%s/%s"%(api_url,"config/listremotes"))
    if data.status_code == 200:
        data=data.json()        
    else:
        app.logger.error("Status Code: %s, Content: %s",data.status_code,data.content)
        return {"status":"failed"}

    return render_template("remotes.html",remotes=data["remotes"])

@app.route("/mkdir/<name>",methods=["POST"])
def mkdir(name):
    data=request.json
    response=requests.post("%s/%s"%(api_url,"operations/mkdir"),
        json={
            "fs":data["remote"]+":",
            "remote":"%s/%s"%(data["path"],name),
        })
    if response.status_code == 200:
        response=response.json()        
    else:
        app.logger.error("Status Code: %s, Content: %s",response.status_code,response.content)
        return {"status":"failed"}

    return {"status":"success","response":response}

@app.route("/thumbnail/generate",methods=["POST"])
def thumbnail_generate():
    data=request.json
    for file in data["files"]:
        thumbnail("%s/%s/%s"%(api_url,urllib.parse.quote("["+data["remote"]+":"+data["path"]+"]"),file),"static/thumbs/%s%s/"%(data["remote"],data["path"]))
    return {"status":"success"}


def list_files(remote,path=""):
    data=requests.post("%s/%s"%(api_url,"operations/list"),
        json={"fs":remote+":","remote":path})

    if data.status_code == 200:
        return data.json()
    else:
        app.logger.error("Status Code: %s, Content: %s",data.status_code,data.content)
        return None

@app.route("/upload",methods=['POST'])
def upload():

    if request.method == 'POST':

        remote_path=request.form['path']
        remote=request.form['remote']
        
        # check if the post request has the file part
        if 'file' not in request.files:            
            return "No file part"

        for file in request.files.getlist("file"):

            # If the user does not select a file, the browser submits an
            # empty file without a filename.
            if file.filename == '':                
                return 'No selected file'
            
            if file:
                filename = secure_filename(file.filename)
                save_path=os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(save_path)

                with open(save_path,"rb") as file:

                    response=requests.post("%s/operations/uploadfile?fs=%s:&remote=%s"%(api_url,remote,remote_path),
                    files = {'file':(filename, file.read())})
                    print(response.content)
                    
                thumbnail(save_path,"static/thumbs/%s%s/"%(remote,remote_path))

        return {"status":"success"}

    return {"status":"failed"}