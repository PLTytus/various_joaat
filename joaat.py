def int32(i:int)->int:
	return i & 0xFFFFFFFF

def signedInt32(i:int)->int:
	return i | (-(i & 0x80000000))

def signedInt8(i:int)->int:
	return i | (-(i & 0x80))

def unsignedInt(i:int)->int:
	return i if i >= 0 else i + (1 << 32)

def hexToStr(h:int)->str:
	return str(h)[2:].upper().rjust(8, "0")

def intToStr(i:int)->str:
	return str(hex(unsignedInt(i)))[2:].upper().rjust(8, "0")

def unsignedHex(h:int)->int:
	return hex(unsignedInt(h))

def strToHex(s:str)->int:
	return hex(int32(int("0x" + s.rjust(8, "0"), 16)))

def joaat(s:str)->dict:
	hash = 0
	for c in s.strip().lower().encode("utf8"):
		hash = int32(hash + signedInt8(c))
		hash = int32(hash + (hash << 10))
		hash = int32(hash ^ (hash >> 6))
	hash = int32(hash + (hash << 3))
	hash = int32(hash ^ (hash >> 11))
	hash = int32(hash + (hash << 15))

	return {
		"unsigned": hash,
		"signed": signedInt32(hash),
		"hex": hex(hash),
		"str": hexToStr(hex(hash)),
	}