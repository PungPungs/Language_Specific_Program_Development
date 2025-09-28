#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")] // hide console window on Windows in release
#![allow(rustdoc::missing_crate_level_docs)] // it's an example


use std::io::Write;
use std::fs::OpenOptions;

use eframe::egui;
use regex::Regex;
use chrono::{Local};


fn main() -> eframe::Result {
    env_logger::init();
    let options = eframe::NativeOptions { // 창의 옵션을 담는 구조체
        viewport: egui::ViewportBuilder::default()
        .with_inner_size([330.0, 200.0])
        .with_min_inner_size([330.0, 200.0])
        .with_max_inner_size([330.0, 200.0]),
        ..Default::default()
    };
    eframe::run_native(
        "Survey Note",
        options,
        Box::new(|_cc| {
            // This gives us image support:
            Ok(Box::<MyApp>::default())
        }),
    )
}


struct MyApp {
    line_num: String,
    line_space: String,
    ways: [&'static str; 4],
    start_way: String,
    end_way: String,
    now_line : String,
    next_line : String,
    start_time : String,
    end_time : String,
    note : std::fs::File,
}

impl Default for MyApp {
    fn default() -> Self {
        Self {
            line_num: String::new(),
            line_space: String::new(),
            ways: ["W", "E", "N", "S"],
            start_way: "W".to_string(), // 초기 선택값
            end_way : "E".to_string(),
            now_line : String::new(),
            next_line : String::new(),
            start_time : String::new(),
            end_time : String::new(),
            note : OpenOptions::new().create(true).append(true).open(format!("{}.csv", Local::now().format("%Y%m%d"))).expect(""),
        }
    }
}

impl eframe::App for MyApp {
    fn update(&mut self, ctx: &egui::Context, _frame: &mut eframe::Frame) {
        egui::CentralPanel::default().show(ctx, |ui| {
            ui.horizontal(|ui|{
                ui.label("Line Name");
                ui.text_edit_singleline(&mut self.line_num);
            });
            ui.horizontal(|ui|{
                ui.label("Line Spacing");
                ui.text_edit_singleline(&mut self.line_space);

            });

            ui.horizontal(|ui|{
                ui.label("Way");
                egui::ComboBox::new("start_way", "")
                    .selected_text(&self.start_way) // 현재 선택된 값 표시
                    .show_ui(ui, |ui| {
                        for way in self.ways {
                            ui.selectable_value(&mut self.start_way, way.to_string(), way);
                        }
                    });
                ui.label(">>");
                egui::ComboBox::new("end_way", "")
                    .selected_text(&self.end_way) // 현재 선택된 값 표시
                    .show_ui(ui, |ui| {
                        for way in self.ways {
                            ui.selectable_value(&mut self.end_way, way.to_string(), way);
                        }
                    });
            });

            egui::Grid::new("grid").show(ui, |ui|{
                ui.label("Now Line");
                ui.label(&self.now_line);
                ui.end_row();
                ui.label("Next Line");
                ui.label(&self.next_line);
                ui.end_row();
                ui.label("Start Time");
                ui.label(&self.start_time);
                ui.end_row();
                ui.label("End Time");
                ui.label(&self.end_time);
                ui.end_row();
            });

            ui.horizontal(|ui|{
                let start = ui.button("Start");
                if start.clicked() {
                    if self.line_num.len() == 0 {
                        return;
                    }
                    let re: Regex = Regex::new(r"^(.+?)(\d+(?:\.\d+)?)(m)$").unwrap();

                    if let Some(caps) = re.captures(&self.line_num){
                        let line_base = &caps[1];
                        let number = &caps[2];
                        let unit = &caps[3];
                        if self.line_space.is_empty() == false {
                            let number : f32 = number.parse::<f32>().unwrap() + self.line_space.parse::<f32>().unwrap(); 
                            self.next_line = format!("{}{}{}",line_base, number, unit);
                        }

                    }
                    self.now_line = self.line_num.to_string();
                    self.start_time = Local::now().format("%H:%M:%S").to_string();

                }
                let end = ui.button("End");
                if end.clicked() {
                    self.end_time = Local::now().format("%H:%M:%S").to_string();
                    
                    let temp: [&str; 5] = [
                        &self.line_num,
                        &self.start_time,
                        &self.end_time,
                        &self.start_way,
                        &self.end_way,
                        ];
                        
                        match self.note.write_all(format!("{}\r\n", temp.join(",")).as_bytes()){
                            Ok(_) => println!("success"),
                            Err(e) => print!("error : {}", e),
                        };
                        self.now_line = self.next_line.clone();
                        self.line_num = self.next_line.clone();
                        self.next_line = String::new();
                }
            });
        });
    }
}
