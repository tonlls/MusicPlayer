
<?php 
function check_data_insert($data,$required=array('name')){
	$res=true;
	foreach($required as $k){
		$res=$res && array_key_exists($k,$data);
	}
}
function check_data_select($data,$required=array('id','name')){
	$res=false;
	foreach($required as $k){
		$res=$res || array_key_exists($k,$data);
	}
}
?>