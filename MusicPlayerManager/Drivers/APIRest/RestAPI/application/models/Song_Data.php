<?php
class Song_Data extends CI_Model {
	public function __construct() {
		parent::__construct();
		$this->load->database();
		$this->load->helper('check_helper');
	}
	public function get($id){
		$sql='SELECT * FROM song_data WHERE song_id=?;';
		$vals=array($id);
		$res=$this->db->query($sql,$vals);
	}
	public function add($data){
		$sql='INSERT INTO song_data(song_id,data) VALUES(?,?);';
		$vals=array($data['id'],$data['data']);
		$this->db->query($sql,$vals);
		return $this->db->insert_id();
	}
}
?>