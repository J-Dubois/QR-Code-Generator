import qrcode.constants #fait le lien avec la librairie nécessaire

qr = qrcode.QRCode(  #créer la variable qr qui utilise le module importé -> qrcode et est caractérisé par la fonction QRCODE
    version=3,       #de 1 à 10, barème de complexité des carrés noir du qr code sur l'image
    box_size=5,      
    border=5,
)

qr.add_data('put data')   #on insère dans notre variable nos données (url/images)
qr.make(fit=True)         #on précise que la variable est forcément vraie

img = qr.make_image(fill_color="black", back_color="white")      #permet de gérer les couleurs du qr code

img.save('QR_name.png')   #génère le fichier png
