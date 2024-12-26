use std::io;

fn main() {
    let array = inputArr(); // Capture the returned Vec<String>
    println!("You entered: {:?}", array);
}

fn inputArr() -> Vec<String> {
    let mut array = Vec::new();

    loop {
        let mut num = String::new(); // Create a new String for each iteration
        io::stdin().read_line(&mut num).expect("Failed to read line");
        let input = num.trim();

        if input == "exit" {
            break;
        }

        array.push(input.to_string()); // Add the trimmed input to the array
    }

    array
}
