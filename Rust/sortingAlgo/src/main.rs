fn bubble_sort(mut arr: Vec<i32>) -> Vec<i32> {
    let n = arr.len();
    for i in 0..n {
        for j in 0..(n - i - 1) {
            if arr[j] > arr[j + 1] {
                arr.swap(j, j + 1);
            }
        }
    }
    arr
}

fn main() {
    let mut numbers = vec![64, 34, 25, 12, 22, 11, 90];
    println!("Unsorted array: {:?}", numbers);

    numbers = bubble_sort(numbers);
    println!("Sorted array: {:?}", numbers);
}
  