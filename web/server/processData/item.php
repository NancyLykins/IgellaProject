<?php
class Item {
    public $name;
    public $weight;
    public $weightUnity;
    public $description;
    public $type;
    public $image;
    public $default_img;

    public function setName($name){
        $this->name = $name;
    }

    public function setWeight($weight){
        $this->weight = $weight;
    }

    public function setWeightUnity($unity){
        $this->weightUnity = $unity;
    }

    public function setDesc($desc){
        $this->description = $desc;
    }

    public function setType($type){
        $this->type = $type;
    }

    public function setImage($img){
        $this->image = $img;
    }

    public function getName(){
        return $this->name;
    }
}

$item = new Item();
$item->setName($_POST["name"]);
echo $item->getName();
echo "<h1>" . $_POST["weight"] . "</h1>";
?>
