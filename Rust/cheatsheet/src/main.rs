use std::io;
fn main() {

    let mut inputs = Vec::new();
    for i in 1..=5{
        println!("Input number {:?}", i);
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("failed");
        inputs.push(input.trim().to_string());
    }println!("your inputs were {:?}", inputs);

    println!("Find index of number:");
    let mut num = String::new();
    io::stdin().read_line(&mut num).expect("failed");
    let num = num.trim();
    let mut found = false;
    for (index, item) in inputs.iter().enumerate(){
        if item == num{
            found = true;
            println!("found" );
            println!("at index {:?}", index);
            break;
        }   
    }if !found{
        println!("not found")
    }
}
