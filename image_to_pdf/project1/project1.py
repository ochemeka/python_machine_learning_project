# from PyPDF2 import PdfFileMerger
# import os
# #var = os.getcwd() For extracting from enother folder
# merger = PdfFileMerger()
# for items in os.listdir():
#   if items.endswith('.pdf'):
#     merger.append(items)
# merger.write("Final_pdf.pdf")
# merger = PdfFileMerger()
# with open(originalFile, 'rb') as fin:
#     merger.append(PdfFileReader(fin))
# os.remove(originalFile)
# merger.close()
#
# from PIL import Image
#
# image_1 = Image.open('a.jpg')
# image_2 = Image.open('b.jpg')
# image_3 = Image.open('c.jpg')
# image_4 = Image.open('d.jpg')
#
# im_1 = image_1.convert('RGB')
# im_2 = image_2.convert('RGB')
# im_3 = image_3.convert('RGB')
# im_4 = image_4.convert('RGB')
#
# image_list = [im_2, im_3, im_4]
#
# im_1.save(r'C:\Users\Ron\Desktop\Test\my_images.pdf', save_all=True, append_images=image_list)
from PIL import Image

images = [
    # Image.open("/Users/apple/Desktop/" + f)
    Image.open("images/" + f)

    for f in ["a.jpg", "b.jpg", "c.jpeg", "d.jpg"]
]

pdf_path = "images/final.pdf"

images[0].save(
    pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:]
)
