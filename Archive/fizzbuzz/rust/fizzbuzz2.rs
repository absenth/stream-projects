use std::io::Write;

fn main() {
    let mut stdout = std::io::stdout();
    for i in 1..=15000000 {
        match (i % 3, i % 5) {
            (0, 0) => writeln!(&mut stdout, "fizzbuzz"),
            (0, _) => writeln!(&mut stdout, "fizz"),
            (_, 0) => writeln!(&mut stdout, "buzz"),
            (_, _) => writeln!(&mut stdout, "{}", i),
        };
    }
}
