use std::io;
use std::cmp::Ordering;
fn main() {
    let mut num1 = String::new();
    let mut num2 = String::new();
    io::stdin().read_line(&mut num1).expect("failed to read line");
    io::stdin().read_line(&mut num2).expect("failed to read line");
    let x:u32 = num1.trim().parse().expect("not integer");
    let y:u32 = num2.trim().parse().expect("not integer");
    
    match x.cmp(&y){
        Ordering::Less => println!("smaller"),
        Ordering::Greater => println!("greater"),
        Ordering::Equal => println!("equal" ),
    }

}
