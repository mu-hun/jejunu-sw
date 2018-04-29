import processing.sound.*;
SoundFile file_one, file_two;
PImage atom, strom_bg, strom;

int spin_var;
float shake_x, shake_y, scale_var;

int step;

int initx, inity, initwh;

void setup()
{
    size(500, 500);
    background(255);
    
    file_one = new SoundFile(this, "hios_is_awsome.mp3");
    file_two = new SoundFile(this, "i_love_hios_x3.mp3");
    file_one.play();
    file_two.play();
    
    atom = loadImage("image/atom.png");
    strom_bg = loadImage("image/strom_background.png");
    strom = loadImage("image/strom.png");
    
    translate(initx, inity);
    
    initx = 283;
    inity = 212;
    initwh = 115;
    
    imageMode(CENTER);
    
    scale_var = 0.2;
    step = 0;
}

void draw()
{
    switch(step){
        case 0:
        background(255);
        
        shake();
        translate(initx + shake_x, inity + shake_y);
        scale(scale_var);
        scale_var += 0.002;
        spin_var += 5;
        
        if (scale_var > 2) step = 1;if (scale_var > 2) step = 1;
        break;
        
        case 1:
        translate(initx, inity);
        image(strom_bg, -40, 40);
        scale_var -= 0.007;
        spin_var -= 0.7;
        scale(scale_var);
        if (scale_var < 1.1) step = 2;
        break;
        
        case 2:
        translate(initx, inity);
        spin_var -= 1;
    }
    
    imageMode(CENTER);
    image(atom, 0, 0, initwh, initwh);
    
    rotate(radians(spin_var));
    //scale(scale_one);
    image(strom, 0, 0, initwh, initwh);

    println(scale_var);
}

void shake()
{
    shake_x += random(-2, 2);
    shake_y += random(-2, 2);
    
}
