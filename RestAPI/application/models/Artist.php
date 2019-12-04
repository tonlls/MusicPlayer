<?php
class Artist extends CI_Model {
	public function get_by_id($id){
		$sql='SELECT * FROM artist WHERE id=?;';
		$vals=array($id);
		$res=$this->db->query($sql,$vals);
	}
	public function get_by_name($name){
		$sql='SELECT * FROM artist WHERE name=?;';
		$vals=array($name);
		$res=$this->db->query($sql,$vals);
	}
	public function add($data){
		$sql='INSERT INTO artist(name) VALUES(?);';
		$vals=array($data['name']);
		$this->db->query($sql,$vals);
		return $this->db->insert_id();
	}
}
?>