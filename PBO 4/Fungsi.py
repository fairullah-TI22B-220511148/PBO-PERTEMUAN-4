def hitung_luas_Selimut(textselimut):
  
     r = float( JariJari.get())
     T = float( Tinggi.get())

     LS = round (2*22/7*r*T) 
  

def hitung_luas_Permukaan(textpermukaan):
  
     r = float( JariJari.get())
     T = float( Tinggi.get())

     LP = round (2*(22/7)*r*T+2*(22/7)*(r*r)) 
  

def hitung_Volume(teksvolume):
    
     r = float( JariJari.get())
     T = float( Tinggi.get())

     V = round ((22/7)*(r*r)*T)

   

def hitung():
  hitung_luas_Selimut()
  hitung_luas_Permukaan()
  hitung_Volume()


