import db_conn as db
import text_recognition as tr
import glob
import os
import yolo as yt
#import practice_ebay as ebs
import ebay_req as er
import cv2
import re
threshold=10
fs=glob.glob("images\*f")
fp=glob.glob("images\*p")
images = glob.glob("images\*g")+fs+fp
d={}
for i in images:
    cr,ids=yt.yolo_det(i)
    im=cv2.imread(i)
    for (j,k) in zip(cr,ids):
        x=j[0]
        y=j[1]
        w=j[2]
        h=j[3]
        x=im[y:y+h,x:x+w]
        cv2.imshow("cropped_image",x)
        cv2.waitKey(0)
        r=tr.txt_recog(x)
        if(len(r)!=0):
            for t in r:
                pl=re.sub('[\W_]+', '', t[1]) 
                if(pl in d.keys()):
                    d[pl]+=1
                else:
                    d[pl]=1
        else:
            if(k in d.keys()):
                d[k]+=1
            else:
                d[k]=1
        
print(d)

db.start()
for i in d.keys():
    print(i.lower())
    qr="select * from products where name='"+i.lower()+"';"
    res=db.select_stmt(qr)
##    print(res)
    if(len(res)!=0):
        qr="update products set count="+str(d[i])+" where id="+str(res[0][0])+";"
        db.insert_and_update_stmt(qr)
        if(d[i]<threshold):
            r=er.eb_req(i)
##            print(i)
##            print("Price:"+str(r['searchResult']['item'][0]['sellingStatus']['currentPrice']['value'])+str(r['searchResult']['item'][0]['sellingStatus']['currentPrice']['_currencyId']))
            print(r)
db.close_conn()



