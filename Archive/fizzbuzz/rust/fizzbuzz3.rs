static FBSTR: &'static [u8; 135] = b"

fizz

buzz
fizz


fizz
buzz

fizz


fizzbuzz
";

use std::io;
use std::io::Write;
use std::ops::IndexMut;
use std::mem::{self, MaybeUninit};
use std::{ptr, slice, str};


pub struct Buffer {
    bytes: [MaybeUninit<u8>; I128_MAX_LEN],
}

impl Buffer {
    /// This is a cheap operation; you don't need to worry about reusing buffers
    /// for efficiency.
    #[inline]
    pub fn new() -> Buffer {
        let bytes = [MaybeUninit::<u8>::uninit(); I128_MAX_LEN];
        Buffer { bytes }
    }

    /// Print an integer into this buffer and return a reference to its string
    /// representation within the buffer.
    pub fn format<I: Integer>(&mut self, i: I) -> &str {
        i.write(unsafe {
            &mut *(&mut self.bytes as *mut [MaybeUninit<u8>; I128_MAX_LEN]
                as *mut <I as Sealed>::Buffer)
        })
    }
}

pub trait Integer: Sealed {}

pub trait Sealed: Copy {
        type Buffer: 'static;
        fn write(self, buf: &mut Self::Buffer) -> &str;
    }


const DEC_DIGITS_LUT: &[u8] = b"\
      0001020304050607080910111213141516171819\
      2021222324252627282930313233343536373839\
      4041424344454647484950515253545556575859\
      6061626364656667686970717273747576777879\
      8081828384858687888990919293949596979899";
macro_rules! impl_Integer {
    ($($max_len:expr => $t:ident),* as $conv_fn:ident) => {$(
        impl Integer for $t {}

        impl Sealed for $t {
            type Buffer = [MaybeUninit<u8>; $max_len];

            #[allow(unused_comparisons)]
            #[inline]
            fn write(self, buf: &mut [MaybeUninit<u8>; $max_len]) -> &str {
                let is_nonnegative = self >= 0;
                let mut n = if is_nonnegative {
                    self as $conv_fn
                } else {
                    // convert the negative num to positive by summing 1 to it's 2 complement
                    (!(self as $conv_fn)).wrapping_add(1)
                };
                let mut curr = buf.len() as isize;
                let buf_ptr = buf.as_mut_ptr() as *mut u8;
                let lut_ptr = DEC_DIGITS_LUT.as_ptr();

                unsafe {
                    // need at least 16 bits for the 4-characters-at-a-time to work.
                    if mem::size_of::<$t>() >= 2 {
                        // eagerly decode 4 characters at a time
                        while n >= 10000 {
                            let rem = (n % 10000) as isize;
                            n /= 10000;

                            let d1 = (rem / 100) << 1;
                            let d2 = (rem % 100) << 1;
                            curr -= 4;
                            ptr::copy_nonoverlapping(lut_ptr.offset(d1), buf_ptr.offset(curr), 2);
                            ptr::copy_nonoverlapping(lut_ptr.offset(d2), buf_ptr.offset(curr + 2), 2);
                        }
                    }

                    // if we reach here numbers are <= 9999, so at most 4 chars long
                    let mut n = n as isize; // possibly reduce 64bit math

                    // decode 2 more chars, if > 2 chars
                    if n >= 100 {
                        let d1 = (n % 100) << 1;
                        n /= 100;
                        curr -= 2;
                        ptr::copy_nonoverlapping(lut_ptr.offset(d1), buf_ptr.offset(curr), 2);
                    }

                    // decode last 1 or 2 chars
                    if n < 10 {
                        curr -= 1;
                        *buf_ptr.offset(curr) = (n as u8) + b'0';
                    } else {
                        let d1 = n << 1;
                        curr -= 2;
                        ptr::copy_nonoverlapping(lut_ptr.offset(d1), buf_ptr.offset(curr), 2);
                    }

                    if !is_nonnegative {
                        curr -= 1;
                        *buf_ptr.offset(curr) = b'-';
                    }
                }

                let len = buf.len() - curr as usize;
                let bytes = unsafe { slice::from_raw_parts(buf_ptr.offset(curr), len) };
                unsafe { str::from_utf8_unchecked(bytes) }
            }
        }
    )*};
}

const I8_MAX_LEN: usize = 4;
const U8_MAX_LEN: usize = 3;
const I16_MAX_LEN: usize = 6;
const U16_MAX_LEN: usize = 5;
const I32_MAX_LEN: usize = 11;
const U32_MAX_LEN: usize = 10;
const I64_MAX_LEN: usize = 20;
const U64_MAX_LEN: usize = 20;
const I128_MAX_LEN: usize = 40;

impl_Integer!(
    I8_MAX_LEN => i8,
    U8_MAX_LEN => u8,
    I16_MAX_LEN => i16,
    U16_MAX_LEN => u16,
    I32_MAX_LEN => i32,
    U32_MAX_LEN => u32
    as u32);

fn main() {
    let max = 15000000u32;
    let loops = max / 15;
    let remainder = max - (max % 15);

    let stdout = io::stdout();
    let mut stdout = stdout.lock();
    let mut out: Vec<u8> = Vec::with_capacity(max as usize * 9);
    for _ in 0..loops {
        let _ = out.write(FBSTR);
    }
    let mut buffer = Buffer::new();
    {
        let mut i = 1u32;
        for l in 0..loops {
            let l = ((l*15) * 9) as usize;
            let _ = write!(&mut out.index_mut(l+0..l+9), "{}", buffer.format(i)); //1
            let _ = write!(&mut out.index_mut(l+9..l+18), "{}", buffer.format(i + 1)); //2
            let _ = write!(&mut out.index_mut(l+27..l+36), "{}", buffer.format(i + 3)); //4
            let _ = write!(&mut out.index_mut(l+54..l+63), "{}", buffer.format(i + 6)); //7
            let _ = write!(&mut out.index_mut(l+63..l+72), "{}", buffer.format(i + 7)); //8
            let _ = write!(&mut out.index_mut(l+90..l+99), "{}", buffer.format(i + 10)); //11
            let _ = write!(&mut out.index_mut(l+108..l+117), "{}", buffer.format(i + 12)); //13
            let _ = write!(&mut out.index_mut(l+117..l+126), "{}", buffer.format(i + 13)); //14

            i += 15;
        }
    }

    for i in remainder + 1..max + 1 {
        match (i % 3 == 0, i % 5 == 0) {
            (false, false) => writeln!(&mut out, "{}", i),
            (true, false) => writeln!(&mut out, "fizz"),
            (false, true) => writeln!(&mut out, "buzz"),
            (true, true) => writeln!(&mut out, "fizzbuzz"),
        };
    }
    let _ = stdout.write(&out);
}

