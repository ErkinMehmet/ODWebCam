import base64
def encodeImageToBase64(imagePath):
    with open(imagePath, "rb") as imageFile:
        encodedString = base64.b64encode(imageFile.read()).decode('utf-8')
    return encodedString

def decodeBase64ToImage(base64String, fileName):
    with open("data/exp/"+fileName, "wb") as imageFile:
        imageFile.write(base64.b64decode(base64String))
        imageFile.close()