<?php

function int32($i){
	return $i & 0xFFFFFFFF;
}

function signedInt32($i){
	return $i | (-($i & 0x80000000));
}

function signedInt8($i){
	return $i | (-($i & 0x80));
}

function joaat($str){
	$hash = 0;
	foreach(str_split(mb_strtolower($str)) as $c){
		$hash = int32($hash + signedInt8(ord($c)));
		$hash = int32($hash + ($hash << 10));
		$hash = int32($hash ^ ($hash >> 6));
	}
	$hash = int32($hash + ($hash << 3));
	$hash = int32($hash ^ ($hash >> 11));
	$hash = int32($hash + ($hash << 15));
	
	return [
		"hex" => strtoupper(dechex($hash)),
		"unsigned" => $hash,
		"signed" => signedInt32($hash),
	];
}

?>