use std::io;

fn main() {

    println!("what do you want to do?");
    let mut questionFull = String::new();
    io::stdin().read_line(&mut questionFull).expect("failed");
    let question = questionFull.trim();
    if question == "square"{
        square();
    }

    else if question == "rectangle"{
        rect();
    }

    else{
        println!("uhh.");
        
    }



    
}


fn square(){
    let mut heightSTR = String::new();
    io::stdin().read_line(&mut heightSTR).expect("failed");
    let height: i32 = heightSTR.trim().parse().expect("not an int");

    let mut widthSTR = String::new();
    io::stdin().read_line(&mut widthSTR).expect("failed");
    let width: i32 = widthSTR.trim().parse().expect("not an int");

    println!("{:?}", height*width);
}


fn rect(){
    let mut heightSTR = String::new();
    io::stdin().read_line(&mut heightSTR).expect("failed");
    let height: i32 = heightSTR.trim().parse().expect("not an int");

    let mut widthSTR = String::new();
    io::stdin().read_line(&mut widthSTR).expect("failed");
    let width: i32 = widthSTR.trim().parse().expect("not an int");

    println!("{:?}", height*width);
}