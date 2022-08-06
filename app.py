from pdf2image import convert_from_path
import os

'''
    To run the code poppler must be installed in the path
    The pdf file must be in the same directory as the python script
    
'''


try:
    def convert(file,cnt):
        images = convert_from_path(file, 500,poppler_path=r"C:\Program Files\poppler-22.04.0\Library\bin")
        counter = 1
        for i in range(len(images)):
            images[i].save(file[0:2]+str(cnt)+"-"+ str(i) +'.jpg', 'JPEG')
except Exception as ex:
    print(ex)
path = r"C:\Users\HP\Desktop\Projects\Mongo_Crud"
dir_list = os.listdir(path)
print(dir_list)
count=1
for pdf in dir_list:
    
    if pdf.endswith(".pdf"):
     convert(pdf,count)
     count+=1
'''
        
'''
for item in dir_list:
    if item.endswith(".pdf"):
        os.remove(os.path.join(path, item))