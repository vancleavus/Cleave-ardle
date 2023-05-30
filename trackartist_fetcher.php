<?php

header("Content-Type: application/json");
date_default_timezone_set("America/Chicago");

$requestInputString_json = file_get_contents('php://input');
$requestInputObject_json = json_decode($requestInputString_json, true);

if($requestInputObject_json['requestType'] == 'prettyPlease'){
	$trackNameStoredString = file_get_contents("/usr/local/Cleaveardle/trackname.txt");
	$trackURIStoredString = file_get_contents("/usr/local/Cleaveardle/trackuri.txt");
	$artistNameStoredString = file_get_contents("/usr/local/Cleaveardle/artistname.txt");
	$artistURIStoredString = file_get_contents("/usr/local/Cleaveardle/artisturi.txt");
	$albumNameStoredString = file_get_contents("/usr/local/Cleaveardle/albumname.txt");
	$albumImgStoredString = file_get_contents("/usr/local/Cleaveardle/albumimg.txt");
	$previewURLStoredString = file_get_contents("/usr/local/Cleaveardle/previewurl.txt");
	echo json_encode(array(
		"success" => true,
		"time" => date("h:i:sa"),
		"track_uri" => $trackURIStoredString,
		"track_name" => $trackNameStoredString,
		"artist_name" => $artistNameStoredString,
		"artist_uri" => $artistURIStoredString,
		"album_name" => $albumNameStoredString,
		"album_img" => $albumImgStoredString,
		"preview_url" => $previewURLStoredString
	));
	exit;
}
else{
	echo json_encode(array(
		"success" => false,
		"time" => date("h:i:sa")
	));
	exit;
}
?>
