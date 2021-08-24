import os
def bulk_renamer():
    i=1
    path ="C:\\Users\\maria\\PycharmProjects\\pythonProject\\images\\"
    for file_name in os.listdir(path):
        photo_names=f"photo{i}.png"
        source= path+file_name
        destination=path+photo_names
        os.rename(source, destination)
        i=i+1
if __name__ =="__main__":
    bulk_renamer()











