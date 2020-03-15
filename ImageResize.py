from PIL import Image
import sys
import os

def imageResize(img,tSize):
    ratio = img.size[0]/img.size[1]
    if(ratio<1):
        output = img.resize((int(tSize*ratio),tSize),Image.NEAREST)
    else:
        output = img.resize((tSize,int(tSize/ratio)),Image.NEAREST)
    return output

	
def main():
	if(os.path.exists("./output/") == False):
		os.mkdir('output')
	
	if( len(sys.argv) != 2 ):
		print("Usage: " + sys.argv[0].split("\\")[-1] + " <size>")
		return
	tSize = int(sys.argv[1])

	for imgName in os.listdir("."):
		if(imgName.find(".png")!=-1):
			img = Image.open(imgName)
			outputImg = imageResize(img,tSize)
			outputImg.save("./output/" + imgName.split('.')[0] + "_resize.png")
			print("Image complete: " + imgName.split('.')[0] + "_resize.png")
		
if __name__ == '__main__':
    main()