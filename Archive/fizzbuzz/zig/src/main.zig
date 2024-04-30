const std = @import("std");
const print = std.debug.print;

pub fn main() !void {
    var elem: u32 = 1;
    while (elem <= 2000000) : (elem += 1) {
        if (elem % 15 == 0) {
            print("fizzbuzz\n", .{});
        } else if (elem % 3 == 0) {
            print("fizz\n", .{});
        } else if (elem % 5 == 0) {
            print("buzz\n", .{});
        } else {
            print("{}\n", .{elem});
        }
    }
}
