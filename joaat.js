function int32(i){
	return i & 0xFFFFFFFF;
}

function signedInt32(i){
	return i | (-(i & 0x80000000));
}

function signedInt8(i){
	return i | (-(i & 0x80));
}

function joaat(s){
	s = unescape(encodeURIComponent(s.toLowerCase()));
	
	var hash = 0;

	for(let i = 0; i < s.length; i++){
		hash = int32(hash + signedInt8(s.charCodeAt(i)));
		hash = int32(hash + (hash << 10));
		hash = int32(hash ^ (hash >>> 6));
	}

	hash = int32(hash + (hash << 3));
	hash = int32(hash ^ (hash >>> 11));
	hash = int32(hash + (hash << 15));

	return hash;
}