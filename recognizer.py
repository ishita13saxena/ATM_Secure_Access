import cv2
import face_recognition
from simple_facerec import SimpleFacerec
import os
from playsound import playsound
people=sorted(os.listdir('people'))
f=-1
user=""
cap=cv2.VideoCapture(0)
for i in people:
    print(i)
    sfr =SimpleFacerec()
    sfr.load_encoding_images(f"people/{i}/")
    
    while True:
        ret,frame=cap.read()
        face_locations,face_names=sfr.detect_known_faces(frame)
        num_faces_detected = len(face_locations)
        print(f"Number of faces detected: {num_faces_detected}")
        if(num_faces_detected>2):
            #print(f"Number of faces detected: {num_faces_detected}")
            playsound('alarm.mp3')
            break
        unknown_count=0
        for face_loc,name in zip(face_locations,face_names):
            print(f"Number of faces detected: {num_faces_detected}")
            y1,x2,y2,x1=face_loc[0],face_loc[1],face_loc[2],face_loc[3]
            if(name=="Unknown"):
                unknown_count=unknown_count+1
            cv2.putText(frame,name,(x1,y1-10),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,200),2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
            if (name=="Registered" and num_faces_detected!=1) :
                f=0
                user=i
                break
            if (name=="Registered" and num_faces_detected==1) :
                f=1
                print("SUCCESSFULLY ACCESS GRANTED")
                break
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break
        if(unknown_count==num_faces_detected or f==0 or f==1):
            break

        
    if(f==0 or f==1):
        break
if(f==-1):
    playsound('alarm.mp3')
buddy=sorted(os.listdir('buddy'))
if(f==0):
    for j in buddy:
        print(j)
        sfr1 =SimpleFacerec()
        sfr1.load_encoding_images(f"buddy/{j}/")
        while True:
            ret,frame=cap.read()
            face_locations,face_names=sfr1.detect_known_faces(frame)
            for face_loc,name in zip(face_locations,face_names):
                y1,x2,y2,x1=face_loc[0],face_loc[1],face_loc[2],face_loc[3]
                if name=="Registered":
                    if (user==j) :
                        name="Buddy"
                        f=2
                        print("SUCCESSFULLY ACCESS GRANTED")
                    else:
                        name="Unknown"   
                        f=3 
                cv2.putText(frame,name,(x1,y1-10),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,200),2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
                if(f==2):
                    break
            
            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1)
            if key == 27:
                break
            if(f==3 or f==0 or f==2):
                break
        if(f==2):
            break
    if(f!=2):
        playsound('alarm.mp3')
        

cap.release()
cv2.destroyAllWindows()
    

