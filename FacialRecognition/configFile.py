import csv

def write_list_to_csv(file_path, data):
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)

def read_list_from_csv(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            return row

imageDatabase = "/Users/utadiparthi/FacialRecognition/Users"
modelPath = "/Users/utadiparthi/FacialRecognition/Model/Model.yml"
cascadePath = "haarcascade_frontalface_default.xml"
csvPath = "/Users/utadiparthi/FacialRecognition/names.csv"