use std::io::process::Command;

fn main() {
    let _process = Command::new("sleep").arg("5").spawn();

    println!("reached the end of main");
}
