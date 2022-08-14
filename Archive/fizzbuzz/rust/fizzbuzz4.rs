use std::io::Write;

fn main() {
    let max = 15000000u32;

    let stdout = std::io::stdout();
    let mut stdout = stdout.lock();
    let mut out: Vec<u8> = Vec::with_capacity(max as usize * 9);
    for i in 0..=max {
        match (i % 3 == 0, i % 5 == 0) {
            (false, false) => writeln!(&mut out, "{}", i),
            (true, false) => writeln!(&mut out, "fizz"),
            (false, true) => writeln!(&mut out, "buzz"),
            (true, true) => writeln!(&mut out, "fizzbuzz"),
        };
    }
    let _ = stdout.write(&out);
}
