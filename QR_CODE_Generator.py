import qrcode.constants                                          #make link with necessary library

qr = qrcode.QRCode(                                              #create the variable (qr) which use the imported module (qrcode) and caracterise by the QRCODE function
    version=3,                                                   #from 1 to 10, its a complexity rate which impact the qr code black squares on the final picture
    box_size=5,      
    border=5,
)

qr.add_data('put data')                                          #we add our data (url/picture) inside the variable
qr.make(fit=True)                                                #we precise that the variable is always true

img = qr.make_image(fill_color="black", back_color="white")      #this allow to change the color of the qr code and the background

img.save('QR_name.png')   #génère le fichier png
