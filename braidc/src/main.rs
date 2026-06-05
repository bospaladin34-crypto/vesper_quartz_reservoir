use nom::{
    bytes::complete::tag,
    IResult,
};

// INITIAL RUST-BASED BRAID PARSER
fn parse_snap_directive(input: &str) -> IResult<&str, &str> {
    tag("ENFORCE_SNAP 91")(input)
}

fn main() {
    let input = "ENFORCE_SNAP 91";
    match parse_snap_directive(input) {
        Ok((remaining, output)) => {
            println!("[+] BRAIDC PARSED GEOMETRIC DIRECTIVE: {}", output);
        },
        Err(_) => println!("[!] BRAIDC SYNTAX ERROR: HEURISTIC DRAG DETECTED."),
    }
}
