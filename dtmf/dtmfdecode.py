import wave
def read_wav():
	fin = open('p2.wav','r')
	n = fin.getnframes()
	d = fin.readframes(n)
	fin.close()
	
	data = []
	for i in range(n):
		#LS8bit = inv_endian(ord(d[2*i]))
		#MS8bit = inv_endian(ord(d[2*i+1]))
		LS8bit, MS8bit = ord(d[2*i]),ord(d[2*i+1])
		data.append((MS8bit<<8)+LS8bit)
	return data 


# Decoder takes a DTMF signal file (.wav), sampled at 44,000
# 16-bit samples per second, and decode the corresponding symbol X.

def decoder():
	data = read_wav()
	temp = []	
	for f1 in F1:
		for f2 in F2:
			diff = 0
			for i in range(FR): #assume phase has not shifted dramatically	
				p = i*1.0/FR
				S=int(scale+scale*(sin(p*f1*PI2)+sin(p*f2*PI2))/2)
				diff += abs(S-data[i])
			temp.append((diff,f1,f2))
	f1,f2 = min(temp)[1:] #retrieve the frequency of minimum signal distortion 
	i, j = F1.index(f1), F2.index(f2)	
	X = keys[4*i+j]
	print 'Decoded key is: ', X
	return X
