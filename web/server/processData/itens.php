<?php

class itens{
    public $name;
    public $weight;
    public $description;
    public $type;
    public $image;
    public $default_img;

    function setName($name){
        $this->name = $name;
    }

    function setWeight($weight){
        $this->weight = $weight;
    }

    function setDesc($desc){
        $this->description = $desc;
    }

    function setType($type){
        $this->type = $type;
    }

    function setImage($img){
        $this->image = $img;
    }
}

?>