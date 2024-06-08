#!/usr/bin/env python3

# Gafgtyt_tor botnet encryption scheme that I reverse engineered from the decryption code.

# Origin: https://blog.netlab.360.com/gafgtyt_tor-and-necro-are-on-the-move-again/

strings = [
	'"?>K!tF>iorZ:ww_uBw3Bw',
	"~-6mvgmv",
	"1-|",
	"cD|",
	"ej~-",
	"51,U",
	"c~6",
	"6c-",
	"-,6",
	"6D7,,mv",
	"j,",
	"jdd",
	"jge",
	".~7DU,1v6m",
	"7~~",
	"6p,",
	"v6c",
	"dx,",
	"7DU",
	"|6e",
	"aDbwwtr3bw",
	"aQuq",
	"aEcc",
	"74tw!",
	"1;t=",
	"|x,<",
	"=ru_Brf_"
]

plaintext_strings = [
	"wvp3te7pkfczmnnl.onion",
	"LDSERVER",
	"UDP",
	"TCP",
	"HOLD",
	"JUNK",
	"TLS",
	"STD",
	"DNS",
	"SCANNER",
	"ON",
	"OFF",
	"OVH",
	"BLACKNURSE",
	"ALL",
	"SYN",
	"RST",
	"FIN",
	"ACK",
	"PSH",
	"WChnnecihn",
	"W.1",
	"WxTT",
	"Agent",
	"User",
	"PING",
	"rc.local"
]

def sbox(input, key, alphabet): # This is a simple substitution matrix
	# Inverse key & alphabet to encode instead of decoding.
	i = 0
	manipulated = ""
	while ( i < len(input,)):
		for table_idx in range(len(alphabet)):
			if input[i] == key[table_idx]:
				manipulated = manipulated + alphabet[table_idx]
		i += 1

	return manipulated

alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ. '
key = '%q*KC)&F98fsr2to4b3yi_:wB>z=;!k?"EAZ7.D-md<ex5U~h,j|$v6c1ga+p@un'


i = 0
for entry in strings:
	if sbox(entry, key, alphabet) in plaintext_strings:
		print("Success: " + str(i) + ": " + sbox(entry, key, alphabet))
	else:
		print("Error: " + str(i) + ": " + sbox(entry, key, alphabet))
	i += 1
