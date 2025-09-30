use std::{fs::{self, File}, io::{BufRead, BufReader}};
use regex::Regex;
use std::io::Write;

fn main() -> std::io::Result<()> {
    let base_path = "./Logs";
    let re = Regex::new(r"^RawGPS").unwrap();
    let check = Regex::new(r"^\$GPGGA,[^*]*\*[0-9A-F]{2}$").unwrap();
    let entries = fs::read_dir(base_path)?;

    for entry in entries {
        let entry = entry?;
        let file_name = entry.file_name().to_string_lossy().to_string(); // 여기서 변수에 담아줌

        if re.is_match(&file_name) {
            let fs = File::open(entry.path())?;
            let reader = BufReader::new(fs);
            let mut new_contents = String::new();

            for line in reader.lines() {
                let line = line?;
                if check.is_match(&line) {
                    new_contents.push_str(&line);
                    new_contents.push('\n');
                }
            }
            let mut file = File::create(entry.path())?; // 기존 내용 덮어쓰기
            file.write_all(new_contents.as_bytes())?;

        }
    }
    Ok(())
}
