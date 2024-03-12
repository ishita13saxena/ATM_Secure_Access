import os
import pymongo
import cv2
import numpy as np
import pandas as pd
import warnings
import tkinter as tk
warnings.filterwarnings("ignore")


def Generate_Data(Name,buddyname):


    def pushmongo(key,bkey):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        dblist = myclient.list_database_names()
        mydb = myclient["users"]
        mydict = [{"Name":key, "buddy_Name":bkey}]
        
    def input_information():
        name=Name
        Buddyname=buddyname
        parent_dir="people/"
        buddy_dir="buddy/"
        final_path=name
        buddy_path = Buddyname
        path=os.path.join(parent_dir,final_path)
        buddy_path= os.path.join(buddy_dir, final_path)
        pushmongo(name,Buddyname)   ## Pushing in mongoDB database
        l=[]
        l.append(path)
        l.append(buddy_path)
        return l
        
    ######## Entering the required details#################
    r=input_information()
    path=r[0]
    path2=r[1]

    os.makedirs(path)   ##Creating the path
    #########################Joining the paths#######################

    pic_no=0

    #####################Loading the harcascade classifier#################
    fa=cv2.CascadeClassifier('FaceDetection/faces.xml')
    cap=cv2.VideoCapture(0)

    ret=True

    while ret:
        ret,frame=cap.read()
        #######Detecting the Faces##################
        frame=cv2.flip(frame,1)
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=fa.detectMultiScale(gray,1.3,5)

        for (x,y,w,h) in faces:
            cropped=frame[y:y+h,x:x+w]
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2,cv2.LINE_AA)
            #face_aligned = face_aligner.align(frame, frame_gray, face)
            pic_no=pic_no+1
            cv2.imwrite(path+'/'+str(pic_no)+'.jpg',cropped)
        cv2.imshow('frame',frame)
        cv2.waitKey(100)

        if( (pic_no>30) | (0XFF==ord('a'))):
            break

    cap.release()
    cv2.destroyAllWindows()
    os.makedirs(path2)   ##Creating the path
    #########################Joining the paths#######################

    pic_no=0

    #####################Loading the harcascade classifier#################
    fa=cv2.CascadeClassifier('FaceDetection/faces.xml')
    cap=cv2.VideoCapture(0)

    ret=True

    while ret:
        ret,frame=cap.read()
        #######Detecting the Faces##################
        frame=cv2.flip(frame,1)
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=fa.detectMultiScale(gray,1.3,5)

        #
        for (x,y,w,h) in faces:
            cropped=frame[y:y+h,x:x+w]
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2,cv2.LINE_AA)
            #face_aligned = face_aligner.align(frame, frame_gray, face)
            pic_no=pic_no+1
            cv2.imwrite(path2+'/'+str(pic_no)+'.jpg',cropped)
        cv2.imshow('frame',frame)
        cv2.waitKey(100)

        if( (pic_no>30) | (0XFF==ord('a'))):
            break

    cap.release()
    cv2.destroyAllWindows()
    return

Generate_Data("ananya","alia")
