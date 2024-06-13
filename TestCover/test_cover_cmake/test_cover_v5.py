from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import subprocess
from pathlib import Path
import sys
from PIL import Image, ImageTk

#comando para criar o .EXE 
#pyinstaller --onefile --icon=C:\\Dev\\Python_study\\TestCover\\icons8-slice-48.png test_cover_v5.py

root = tb.Window(themename="superhero")
root.title("Test Cover")
# root.iconbitmap("c:\\Dev\\backend-olimpo-ng\\tools\\CoverageTest\\test_cover_icon.ico")
root.geometry("600x600")

def cronos_coverage():
    comando = f'ninja -C build/win-dbg generate_coverage_report_cronos'
    subprocess.call(comando,shell=True)

def water_meter_coverage():
    comando = f'ninja -C build/win-dbg generate_coverage_report_residencial_water_meter'
    subprocess.call(comando,shell=True)

def zeus_ths_coverage():
    comando = f'ninja -C build/win-dbg generate_coverage_report_zeus_ths'
    subprocess.call(comando,shell=True)

def recloser_coverage():
    comando = f'ninja -C build/win-dbg generate_coverage_report_monophase_recloser'
    subprocess.call(comando,shell=True)

def bulk_coverage():
    comando = f'ninja -C build/win-dbg generate_coverage_report_bulk_meter'
    subprocess.call(comando,shell=True)

def pantheon_coverage():
    comando = f'ninja -C build/win-dbg generate_coverage_pantheon'
    subprocess.call(comando,shell=True)

def gateway_coverage():
    comando = f'ninja -C build/win-dbg generate_coverage_report_gateway'
    subprocess.call(comando,shell=True)

def zeus_ng_coverage():
    comando = f'ninja -C build/win-dbg generate_coverage_report_zeus_ng'
    subprocess.call(comando,shell=True)

def close_app():
    root.quit()

my_label = tb.Label(text="Test Cover - backend OlimpoNg", font=("Garamond",28), bootstyle="success, inverse")
my_label.pack(pady=20)

bulk_button = tb.Button(text="Bulk Coverage", bootstyle="success", width=30, command=bulk_coverage)
bulk_button.pack(pady=10)

cronos_button = tb.Button(text="CronosNgPlus Coverage", bootstyle="success", width=30, command=cronos_coverage)
cronos_button.pack(pady=10)

gateway_button = tb.Button(text="Gateway Coverage", bootstyle="success", width=30, command=gateway_coverage)
gateway_button.pack(pady=10)

pantheon_button = tb.Button(text="Pantheon Coverage", bootstyle="success", width=30, command=pantheon_coverage)
pantheon_button.pack(pady=10)

recloser_coverage_button = tb.Button(text="Recloser Coverage", bootstyle="success", width=30, command=recloser_coverage)
recloser_coverage_button.pack(pady=10)

water_meter_button = tb.Button(text="WaterMeter Coverage", bootstyle="success", width=30, command=water_meter_coverage)
water_meter_button.pack(pady=10)

zeus_ng_button = tb.Button(text="ZeusNg Coverage", bootstyle="success", width=30, command=zeus_ng_coverage)
zeus_ng_button.pack(pady=10)

zeus_ths_button = tb.Button(text="ZeusTHS Coverage", bootstyle="success", width=30, command=zeus_ths_coverage)
zeus_ths_button.pack(pady=10)

close_app_button = tb.Button(text="Quit", bootstyle="success", width=30, command=close_app)
close_app_button.pack(pady=10)

root.mainloop()