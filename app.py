#!/usr/bin/env python

from flask import Flask,request,render_template
import os

application=Flask(__name__)
app=application


@app.route('/')
def start():
        return render_template("index.html")

@app.route('/upload_file',methods=['POST'])
def upload():
	mfile=request.files['file']
	f=open(mfile.filename,'w')
	contents=mfile.read()
	f.write(contents)


	os.system("hadoop fs -rm /assignment/output/_SUCCESS")
	os.system("hadoop fs -rm /assignment/output/part-00000")
	os.system("hadoop fs -rmdir /assignment/output")
	os.system("hadoop fs -rm /assignment/output.txt")
	os.system("hadoop fs -mkdir /assignment")
	os.system("hadoop fs -put "+mfile.filename+" /assignment/"+mfile.filename)
    os.system("hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -D stream.map.output.field.seperator'\t' -D stream.num.map.output.key.fields=3 -file /home/ubuntu/mapper.py -mapper /home/ubuntu/mapper.py -file /home/ubuntu/reducer.py -reducer /home/ubuntu/reducer.py -input /assignment/"+ file1.filename +" -output /assignment/output1")
    os.system("hadoop fs -cat /asg/out12/part-00000  > /home/ubuntu/output.txt")
    file2=open("output.txt",'r')
    contents=file2.readlines() 
    return render_template("output.html",res=contents)


@app.route('/total_lines',methods = ['POST'])
def lines():
	os.system("hadoop fs -cat /asg/out12/part-00000 | wc -l > /home/ubuntu/output1.txt")
	file3 = open("output1.txt",'r')
	contents = file3.readline()
	html = "<h2>"+contents + "</h2>"
	return html

if __name__=="__main__":
        app.run(host=" ")
	

