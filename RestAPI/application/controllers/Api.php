<?php

require APPPATH . 'libraries/REST_Controller.php';

class Api extends REST_Controller {

	public function __construct() {
		parent::__construct();
		$this->load->model('Song');
		$this->load->model('Song_Data');
		$this->load->model('Artist');
		$this->load->model('Album');
		$this->load->helper('check_helper');
	}

	public function song_data_get(){
		$in=$this->input->get();
		if(check_data_select($in)){
			$data=$this->Song_Data->get($in['id']);
			$this->response($data, REST_Controller::HTTP_OK);
		}
		else
			$this->response($data, REST_Controller::HTTP_BAD_REQUEST);
	}
	public function song_data_post(){
		$in=$this->input->post();
		if(check_data_insert($in)){
			$this->Song_Data->add($in);
			$this->response($data, REST_Controller::HTTP_OK);
		}
		else
			$this->response($data, REST_Controller::HTTP_BAD_REQUEST);
	}

	public function song_get(){
		$in=$this->input->get();
		if(check_data_select($in)){
			if(array_key_exists('id',$in)){
				$data=$this->Song->get_by_id($in['id']);
			}
			else if(array_key_exists('name',$in)){
				$data=$this->Song->get_by_name($in['name']);
			}
			$this->response($data, REST_Controller::HTTP_OK);
		}
		else
			$this->response($data, REST_Controller::HTTP_BAD_REQUEST);
	}
	public function song_post(){
		$in=$this->input->post();
		if(check_data_insert($in)){
			$this->Song->add($in);
			$this->response($data, REST_Controller::HTTP_OK);
		}
		else
			$this->response($data, REST_Controller::HTTP_BAD_REQUEST);
	}
	public function artist_get(){
		$in=$this->input->get();
		if(check_data_select($in)){
			if(array_key_exists('id',$in)){
				$data=$this->Artist->get_by_id($in['id']);
			}
			else if(array_key_exists('name',$in)){
				$data=$this->Artist->get_by_name($in['name']);
			}
			$this->response($data, REST_Controller::HTTP_OK);
		}
		else
			$this->response($data, REST_Controller::HTTP_BAD_REQUEST);
	}
	public function artist_post(){
		$in=$this->input->post();
		if(check_data_insert($in)){
			$this->Artist->add($in);
			$this->response($data, REST_Controller::HTTP_OK);
		}
		else
			$this->response($data, REST_Controller::HTTP_BAD_REQUEST);
	}
	public function album_get(){
		$in=$this->input->get();
		if(check_data_select($in)){
			if(array_key_exists('id',$in)){
				$data=$this->Album->get_by_id($in['id']);
			}
			else if(array_key_exists('name',$in)){
				$data=$this->Album->get_by_name($in['name']);
			}
			$this->response($data, REST_Controller::HTTP_OK);
		}
		else
			$this->response($data, REST_Controller::HTTP_BAD_REQUEST);
	}
	public function album_post(){
		$in=$this->input->post();
		if(check_data_insert($in)){
			$this->Album->add($in);
			$this->response($data, REST_Controller::HTTP_OK);
		}
		else
			$this->response($data, REST_Controller::HTTP_BAD_REQUEST);
	}
	
}
?>