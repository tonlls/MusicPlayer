<?php
class Song extends CI_Model {
	public function __construct() {
		parent::__construct();
		$this->load->database();
	}
	public function get_by_id($id){
		$sql='SELECT * FROM album WHERE id=?;';
		$vals=array($id);
		$res=$this->db->query($sql,$vals);
	}
	public function get_by_name($name){
		$sql='SELECT * FROM album WHERE name=?;';
		$vals=array($name);
		$res=$this->db->query($sql,$vals);
	}
	public function add($data){
		$sql='INSERT INTO album(name,artist_id) VALUES(?,?);';
		$vals=array($data['name'],$data['artist_id']);
		$this->db->query($sql,$vals);
		return $this->db->insert_id();
	}
}
?>