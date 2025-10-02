use std::fs::File;
use regex::Regex;
use std::io::Read;

fn main() -> std::io::Result<()>{
    let base_path = "RawGPS2025-08-28.log";
    let mut file = File::open(base_path)?;
    let mut buffer = Vec::new();
    file.read_to_end(&mut buffer)?;
    
    Ok(())


}