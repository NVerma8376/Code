use std::io;

fn main() {
    let mut dec = String::new();
    println!("Enter decimal number:");
    io::stdin().read_line(&mut dec).expect("Failed to read input");

    let mut bin = String::new();
    println!("Enter binary number:");
    io::stdin().read_line(&mut bin).expect("Failed to read input");

    let decimal = to_dec(&bin);
    let binary = to_bin(&dec);
    println!("Binary representation: {}", binary);
    println!("Decimal representation: {:?}", decimal);
}

fn to_bin(input: &str) -> i32 {
    let mut bin = 0;
    let mut base = 1;

    let mut dec: i32 = input.trim().parse().expect("Not an integer");

    while dec > 0 {
        let divi: i32 = dec % 2; 
        bin += divi * base;      
        base *= 10;              
        dec /= 2;                
    }

    bin
}


fn to_dec(input: &str) -> i32 {

    let mut dec = 0;
    let mut temp = 1;
    let mut bin = input.trim();

    for letter in bin.chars().rev(){
        if letter == '1'{
            dec += temp;
        }
        temp = temp*2
    }  

    dec 
}