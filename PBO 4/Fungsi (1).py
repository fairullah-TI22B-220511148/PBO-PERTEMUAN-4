#bola
def hitung_luas_Bola(textjarijari):
  
     r = float( textjarijari )

     LB = round (4*(22/7)*r*r) 

     return LB 
  
def hitung_Volume(textjarijari):
    
     r = float( textjarijari )
     
     V = round (4/3*(22/7)*(r*r*r))

     return V

#kerucut

  
def hitung_luas_Selimut(teksjarijari,teksgarispelukis):
  
     r = float( teksjarijari )
     s = float( teksgarispelukis )

     LS = round (22/7*r*s) 

     return LS
  
def hitung_luas_Permukaan(teksjarijari,teksgarispelukis):
  
     r = float( teksjarijari)
     s = float( teksgarispelukis )

     LP = round ((22/7)*r*s+(22/7)*(r*r)) 
  
     return LP
def hitung_Volumep(teksjarijari,tekstinggi):
    
     r = float( teksjarijari )
     T = float( tekstinggi )

     vp = round (1/3*(22/7)*(r*r)*T)

     return vp


#limassegitiga

def hitung_luas(LuasSisi1,LuasSisi2,LuasSisi3,LuasSisi4):
  
     Ls1 = float( LuasSisi1 )
     Ls2 = float( LuasSisi2 )
     Ls3 = float( LuasSisi3 )
     Ls4 = float( LuasSisi4 ) 
    

     L = round (Ls1+Ls2+Ls3+Ls4) 

     return L

def hitung_volume(LuasAlas,Tinggi):
    
     La = float(LuasAlas)
     t  = float(Tinggi)

     K = round ( 1/6*La*t)

     return K

#limas segiempapt

def hitung_luas(LuasSisi1,LuasSisi2,LuasSisi3,LuasSisi4,LuasSisi5):
  
     Ls1 = float( LuasSisi1)
     Ls2 = float( LuasSisi2)
     Ls3 = float( LuasSisi3)
     Ls4 = float( LuasSisi4)
     Ls5 = float( LuasSisi5)

     L = round (Ls1+Ls2+Ls3+Ls4+Ls5 ) 

     return L


def hitung_volume(LuasAlas,Tinggi):
    
     La = float(LuasAlas)
     t  = float(Tinggi)

     K = round ( 1/3*La*t)

     return K 

#balok

def hitung_luas(panjang,lebar,tinggi):
  
     p = float(panjang)

     l = float(lebar)
      
     t = float(tinggi)
   
     L = round ((2 * p * l) + ( 2 * p * t ) + ( 2 * l * t) ) 

     return L

def hitung_volume(panjang,lebar,tinggi):
    
     p = float(panjang)

     l = float(lebar)
      
     t = float(tinggi)

     K = round ( p * l * t)

     return K

#silinder

def hitung_luas_Selimut(JariJari,Tinggi):
  
     r = float( JariJari )
     T = float( Tinggi )

     LS = round (2*22/7*r*T) 

     return LS

def hitung_luas_Permukaan(JariJari,Tinggi):
  
     r = float( JariJari)
     T = float( Tinggi)

     LP = round (2*(22/7)*r*T+2*(22/7)*(r*r)) 

     return LP

def hitung_Volume(JariJari,Tinggi):
    
     r = float( JariJari)
     T = float( Tinggi)

     V = round ((22/7)*(r*r)*T)

     return V






#kubus

def hitung_luas(txtrusuk):
  
   R = float(txtrusuk)
   
   L= round( 6* R **2) 

   return L

def hitung_volume(txtrusuk):
    
   R = float(txtrusuk)

   K = round (R ** 3)

   return K






#prismasegitiga



def hitung_volume_segitiga(txtsisi1,txtsisi2,txtsisi3,txttinggi_prisma,txtalas,txttinggi):
    S_1 = float(txtsisi1)
    S_2 = float(txtsisi2)
    S_3 = float(txtsisi3)
    T = float(txttinggi_prisma)
    a = float(txtalas)
    t = float(txttinggi)
    
    ks = round(S_1 + S_2 + S_3)

    return ks



def hitung_luas_Selimut(txttinggi_prisma,txtvolume_segitiga):
    T = float (txttinggi_prisma)
    ks =float (txtvolume_segitiga)
    
    LS = (ks * T)

    return LS


def hitung_luas_Permukaan(txtvolume_segitiga,txttinggi_prisma,txtalas,txttinggi):
    ks = float (txtvolume_segitiga)
    T = float(txttinggi_prisma)
    a = float(txtalas)
    t = float(txttinggi)
    
    LP = (ks * T * a * t)

    return LP

def hitung_volume(txttinggi_prisma,txtalas,txttinggi):
    T = float(txttinggi_prisma)
    a = float(txtalas)
    t = float(txttinggi)

    V = (1/2*a*t*T)

    return V