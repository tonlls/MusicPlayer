<?php

require APPPATH . 'libraries/REST_Controller.php';

class Api extends REST_Controller {

	public function __construct() {
		parent::__construct();
		$this->load->database();
		$this->load->model('Song');
		$this->load->model('Artist');
		$this->load->model('Album');
	}

	public function song_get(){
		$ok=false;
		$in=$this->input->get();

		if(array_key_exists('id',$in)){
			$data=$this->Song->get_by_id($in['id']);
			$ok=true;
		}
		else if(array_key_exists('name',$in)){
			$data=$this->Song->get_by_name($in['name']);
			$ok=true;
		}
		if($true)
			$this->response($data, REST_Controller::HTTP_OK);
		else
			$this->response($data, REST_Controller::HTTP_BAD_REQUEST);
	}
	public function song_post(){
		$ok=false;
		$in=$this->input->post();
		$this->Song->add($in);
		if($true)
			$this->response($data, REST_Controller::HTTP_OK);
		else
			$this->response($data, REST_Controller::HTTP_BAD_REQUEST);
	}
	public function artist_get(){
		$ok=false;
		$in=$this->input->get();

		if(array_key_exists('id',$in)){
			$data=$this->Artist->get_by_id($in['id']);
			$ok=true;
		}
		else if(array_key_exists('name',$in)){
			$data=$this->Artist->get_by_name($in['name']);
			$ok=true;
		}
		if($true)
			$this->response($data, REST_Controller::HTTP_OK);
		else
			$this->response($data, REST_Controller::HTTP_BAD_REQUEST);
	}
	public function artist_post(){
		$ok=false;
		$in=$this->input->post();
		$this->Artist->add($in);
		if($true)
			$this->response($data, REST_Controller::HTTP_OK);
		else
			$this->response($data, REST_Controller::HTTP_BAD_REQUEST);
	}
	public function album_get(){
		$ok=false;
		$in=$this->input->get();

		if(array_key_exists('id',$in)){
			$data=$this->Album->get_by_id($in['id']);
			$ok=true;
		}
		else if(array_key_exists('name',$in)){
			$data=$this->Album->get_by_name($in['name']);
			$ok=true;
		}
		if($true)
			$this->response($data, REST_Controller::HTTP_OK);
		else
			$this->response($data, REST_Controller::HTTP_BAD_REQUEST);
	}
	public function album_post(){
		$ok=false;
		$in=$this->input->post();
		$this->Album->add($in);
		if($true)
			$this->response($data, REST_Controller::HTTP_OK);
		else
			$this->response($data, REST_Controller::HTTP_BAD_REQUEST);
	}
	
}
?>