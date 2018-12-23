import numpy as np

def movimiento(r,origen, destino, pivote,matriz,n_rosquillas):
	if r >= 1:
		movimiento(r-1,origen,pivote,destino,matriz,n_rosquillas)
		muevedisco(matriz,origen,destino,n_rosquillas)
		movimiento(r-1,pivote,destino,origen,matriz,n_rosquillas)

def muevedisco(matriz, origen,destino,n_rosquillas):
	print("Disco de",origen,"a",destino)
	a=next((i for i, x in enumerate(matriz[:,0]) if x!=0), n_rosquillas) 
	b=next((i for i, x in enumerate(matriz[:,1]) if x!=0), n_rosquillas)
	c=next((i for i, x in enumerate(matriz[:,2]) if x!=0), n_rosquillas)
	if origen=="A":
		if destino=="B":
			matriz[b-1,1]=matriz[a,0]
		else:
			matriz[c-1,2]=matriz[a,0]
		matriz[a,0]=0
	if origen=="B":
		if destino=="A":
			matriz[a-1,0]=matriz[b,1]
		else:
			matriz[c-1,2]=matriz[b,1]
		matriz[b,1]=0
	if origen=="C":
		if destino=="A":
			matriz[a-1,0]=matriz[c,2]
		else:
			matriz[b-1,1]=matriz[c,2]
		matriz[c,2]=0
	print(matriz)

def juegoTorre(n_rosquillas):
	matriz=np.zeros((n_rosquillas,3))
	matriz[:n_rosquillas,0]=range(1,n_rosquillas+1)
	movimiento(r=n_rosquillas,origen="A",destino="C",pivote="B", matriz=matriz,n_rosquillas=n_rosquillas)

######### Tower of Hanoi ########
def main():
	juegoTorre(4)
if __name__ == "__main__": 
	main()
