<?php
class Song extends CI_Model {
	public function get_by_id($id){
		$sql='SELECT * FROM song WHERE id=?;';
		$vals=array($id);
		$res=$this->db->query($sql,$vals);
	}
	public function get_by_name($name){
		$sql='SELECT * FROM song WHERE name=?;';
		$vals=array($name);
		$res=$this->db->query($sql,$vals);
	}
	public function add($data){
		$sql='INSERT INTO song(name,artist_id,album_id,data) VALUES(?,?,?,?);';
		$vals=array($data['name'],$data['artist_id'],$data['album_id'],$data['data']);
		$this->db->query($sql,$vals);
		return $this->db->insert_id();
	}
}
?>