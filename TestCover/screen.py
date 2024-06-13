import subprocess
from pathlib import Path
from ttkbootsrap.constants import *
import ttkbootstrap
import tkinter as tk
import sys
from PIL import Image, ImageTk

# comando para criar o .EXE = pyinstaller --onefile --icon=C:\\Dev\\Python_study\\TestCover\\icons8-slice-48.png screen.py
# "C:\\Dev\\Python_study\\TestCover\\icons8-slice-48.png"

caminho_string_1 = "%CD%\\source\\src\\devices\\cronos_ng_plus"
caminho1 = Path(caminho_string_1)

caminho_string_2 = "%CD%\\source\\src\\services\\cronos_ng_plus"
caminho2 = Path(caminho_string_2)

caminho_string_3 = "%CD%\\source\\src\\services\\cronos_ng_plus\\commands"
caminho3 = Path(caminho_string_3)

caminho_string_water1 = "%CD%\\source\\src\\devices\\bulk_meter"
caminhowater1 = Path(caminho_string_water1)

caminho_string_water2 = "%CD%\\source\\src\\services\\bulk_meter"
caminhowater2 = Path(caminho_string_water2)

caminho_string_water_3 = "%CD%\\source\\src\\services\\bulk_meter\\commands"
caminhowater3 = Path(caminho_string_water_3)

caminho_string_water_4 = "%CD%\\source\\libraries\\eletra_sdk\\src\\protocols\\modbus"
caminhowater4 = Path(caminho_string_water_4)

caminho_string_water_5 = "C:\\Dev\\Eletra-SDK\\source\\src\\services\\bulk_meter\\commands"
caminhowater5 = Path(caminho_string_water_5)

caminho_string_recloser_1 = "%CD%\\source\\src\\devices\\monophase_recloser"
caminho_recloser1 = Path(caminho_string_recloser_1)

caminho_string_recloser_2 = "%CD%\\source\\src\\devices\\monophase_recloser\\commands"
caminho_recloser2 = Path(caminho_string_recloser_2)

caminho_string_recloser_3 = "%CD%\\source\\src\\devices\\monophase_recloser\\firmware_update"
caminho_recloser3 = Path(caminho_string_recloser_3)

caminho_string_recloser_4 = "%CD%\\source\\src\\services\\monophase_recloser"
caminho_recloser4 = Path(caminho_string_recloser_4)

water_string_1 = "%CD%\\source\\src\\devices\\residencial_water_meter"
water1 = Path(water_string_1)

water_string_2 = "%CD%\\source\\src\\devices\\residencial_water_meter\\commands"
water2 = Path(water_string_2)

water_string_3 = "%CD%\\source\\src\\services\\residencial_water_meter"
water3 = Path(water_string_3)

water_string_4 = "%CD%\\source\\src\\services\\residencial_water_meter\\commands"
water4 = Path(water_string_4)

zeus_ths_string_1 = "%CD%\\source\\src\\devices\\zeus_ths"
zeus_ths1 = Path(zeus_ths_string_1)

zeus_ths_string_2 = "%CD%\\source\\src\\devices\\zeus_ths\\commands"
zeus_ths2 = Path(zeus_ths_string_2)

zeus_ths_string_3 = "%CD%\\source\\src\\devices\\zeus_ths\\ext_commands"
zeus_ths3 = Path(zeus_ths_string_3)

# zeus_ths_string_4 = "%CD%\\source\\src\\devices\\zeus_ths\\utils"
zeus_ths_string_4 = "%CD%\\source\\src\\devices\\zeus_ths\\utils"
zeus_ths4 = Path(zeus_ths_string_4)  

zeus_ths_string_5 = "%CD%\\source\\src\\services\\zeus_ths"
zeus_ths5 = Path(zeus_ths_string_5)

zeus_ths_string_6 = "%CD%\\source\\src\\services\\zeus_ths\\commands"
zeus_ths6 = Path(zeus_ths_string_6)

zeus_ths_string_7 = "%CD%\\source\\src\\services\\zeus_ths\\ext_commands"
zeus_ths7 = Path(zeus_ths_string_7)

zeus_string_1 = "%CD%\\source\\src\\devices\\zeus"
zeus1 = Path(zeus_string_1)

zeus_string_2 = "%CD%\\source\\src\\devices\\zeus\\commands"
zeus2 = Path(zeus_string_2)

zeus_string_3 = "%CD%\\source\\src\\devices\\zeus\\commands\\permanent_log"
zeus3 = Path(zeus_string_3)

zeus_string_4 = "%CD%\\source\\src\\services\\zeus"
zeus4 = Path(zeus_string_4)

zeus_string_5 = "%CD%\\source\\src\\services\\zeus\\commands"
zeus5 = Path(zeus_string_5)

caminho_string_app = "%CD%\\build\\win-dbg\\source\\tests\\foo.exe"
caminho_app =   Path(caminho_string_app)

caminho_app_bulk = "%CD%\\build\\win-dbg\\source\\tests\\EletraSdkBulkTests.exe"
caminho_bulk = Path(caminho_app_bulk)

caminho_app_recloser = "%CD%\\build\\win-dbg\\source\\tests\\EletraSdkRecloserTests.exe"
caminho_recloser_final = Path(caminho_app_recloser)

caminho_water_res = "%CD%\\build\\win-dbg\\source\\tests\\EletraSdkResidencialWaterMeterTests.exe"
caminho_app_water = Path(caminho_water_res)

caminhozeus = "%CD%\\build\\win-dbg\\source\\tests\\EletraSdkZeusTests.exe"
caminho_app_zeus = Path(caminhozeus)

caminhoths = "%CD%\\build\\win-dbg\\source\\tests\\EletraSdkZeusThsTests.exe"
caminho_app_zeus_ths = Path(caminhoths)

caminhocronosng = "%CD%\\build\\win-dbg\\source\\tests\\EletraSdkCronosNgTests.exe"
caminho_app_cronos = Path(caminhocronosng)

caminhoutils1 = "%CD%\\source\\src\\utils"
caminho_utils_1 = Path(caminhoutils1)

caminhoutils2 = "%CD%\\source\\src\\utils\\access_security"
caminho_utils_2 = Path(caminhoutils2)

caminhoutils3 = "%CD%\\source\\src\\utils\\design_patterns"
caminho_utils_3 = Path(caminhoutils3)

caminhoutils4 = "%CD%\\source\\src\\utils\\firmware_update"
caminho_utils_4 = Path(caminhoutils4)

caminhoutils5 = "%CD%\\source\\src\\utils\\par"
caminho_utils_5 = Path(caminhoutils5)

caminhoutils6 = "%CD%\\source\\src\\services\\utils"
caminho_utils_6 = Path(caminhoutils6)

caminhoutils7 = "%CD%\\source\\src\\protocols\\abnt"
caminho_utils_7 = Path(caminhoutils7)

caminhoutils8 = "%CD%\\source\\src\\protocols\\dlms"
caminho_utils_8 = Path(caminhoutils8)

# caminhoutils9 = "%CD%\\source\\src\\protocols\\dlms\\classes\\activity_calendar
# caminho_utils_9 = Path(caminhoutils9)

caminhoutils10 = "%CD%\\source\\src\\protocols\\dlms\\classes\\image_transfer"
caminho_utils_10 = Path(caminhoutils10)

caminhoutils11 = "%CD%\\source\\src\\protocols\\dlms\\classes\\profile_generic"
caminho_utils_11 = Path(caminhoutils11)

caminhoutils12 = "%CD%\\source\\src\\protocols\\dlms\\cosem"
caminho_utils_12 = Path(caminhoutils12)

caminhoutils13 = "%CD%\\source\\src\\protocols\\dlms\\link_layer"
caminho_utils_13 = Path(caminhoutils13)

caminhoutils14 = "%CD%\\source\\src\\protocols\\emode"
caminho_utils_14 = Path(caminhoutils14)

caminhoutils15 = "%CD%\\source\\src\\protocols\\hxd"
caminho_utils_15 = Path(caminhoutils15)

caminhoutils16 = "%CD%\\source\\src\\protocols\\hxg_water_meter"
caminho_utils_16 = Path(caminhoutils16)

caminhoutils17 = "%CD%\\source\\src\\protocols\\pima"
caminho_utils_17 = Path(caminhoutils17)

caminhoutils18 = "%CD%\\source\\src\\protocols\\utc"
caminho_utils_18 = Path(caminhoutils18)

caminhoapputils = "%CD%\\build\\win-dbg\\source\\tests\\UtilsTests.exe"
caminho_utils_app = Path(caminhoapputils)

caminholib = "%CD%\\source\\libraries\\eletra_sdk\\src\\protocols\\modbus"
caminho_lib_modbus = Path(caminholib)

caminhoexeib = "%CD%\\build\\win-dbg\\source\\libraries\\eletra_sdk\\tests\\TestEletraSDK.exe"
caminho_exe_libs = Path(caminhoexeib)

def coverage_test_from_CRONOS_NG():
    comando = f'OpenCppCoverage.exe --sources={caminho1} --sources={caminho2} --sources={caminho3} --export_type=html -- {caminho_app_cronos}'
    subprocess.call(comando,shell=True)

def coverage_test_from_Bulk_Meter():
    comando = f'OpenCppCoverage.exe --sources={caminhowater1} --sources={caminhowater2} --sources={caminhowater3} --export_type=html -- {caminho_bulk}'
    subprocess.call(comando,shell=True)

def coverage_test_from_RECLOSER():
    comando = f'OpenCppCoverage.exe --sources={caminho_recloser1} --sources={caminho_recloser2} --sources={caminho_recloser3} --sources={caminho_recloser4} --export_type=html -- {caminho_recloser_final}'
    subprocess.call(comando,shell=True)

def coverage_test_from_WATER():
    comando = f'OpenCppCoverage.exe --sources={water1} --sources={water2} --sources={water3} --sources={water4} --export_type=html -- {caminho_app_water}'
    subprocess.call(comando,shell=True)

def coverage_test_from_ZEUS_NG():
    comando1 = f'OpenCppCoverage.exe --sources=%CD%\\source\\devices\\zeus_ng\\src\\services\\zeus_ng --sources=%CD%\\source\\devices\\zeus_ng\\src\\services\\zeus_ng\\commands --sources=%CD%\\source\\devices\\zeus_ng\\src\\zeus_ng --sources=%CD%\\source\\devices\\zeus_ng\\src\\zeus_ng\\commands --sources=%CD%\\source\\devices\\zeus_ng\\src\\zeus_ng\\models --sources=%CD%\\source\\devices\\zeus_ng\\src\\zeus_ng\\models\\permanent_change_log --export_type=html -- "%CD%\\build\\win-dbg\\source\\tests\\EletraSdkZeusNgTests.exe"'
    subprocess.call(comando1,shell=True)

def coverage_test_from_ZEUS_THS():
    comando = f'OpenCppCoverage.exe --sources={zeus_ths1} --sources={zeus_ths2} --sources={zeus_ths3} --sources={zeus_ths4} --sources={zeus_ths5} --sources={zeus_ths6} --sources={zeus_ths7} --export_type=html -- {caminho_app_zeus_ths}'
    subprocess.call(comando,shell=True)

def coverage_test_from_ZEUS():
    comando = f'OpenCppCoverage.exe --sources={zeus1} --sources={zeus2} --sources={zeus3} --sources={zeus4} --sources={zeus5} --export_type=html -- {caminho_app_zeus}'
    subprocess.call(comando,shell=True)

def coverage_test_from_Utils():
    comando = f'OpenCppCoverage.exe  --sources={caminho_utils_1} --sources={caminho_utils_2} --sources={caminho_utils_3} --sources={caminho_utils_4} --sources={caminho_utils_5} --sources={caminho_utils_6} --sources={caminho_utils_7} --sources={caminho_utils_8} --sources={caminho_utils_10} --sources={caminho_utils_11} --sources={caminho_utils_12} --sources={caminho_utils_13} --sources={caminho_utils_14} --sources={caminho_utils_15} --sources={caminho_utils_16} --sources={caminho_utils_17} --sources={caminho_utils_18} --export_type=html -- {caminho_utils_app}'
    subprocess.call(comando,shell=True)

def coverage_test_lib_mobdus():
    comando = f'OpenCppCoverage.exe --sources={caminho_lib_modbus} --export_type=html -- {caminho_exe_libs}'
    subprocess.call(comando,shell=True)

def fechar_aplicativo():
    root.quit()

root = tk.Tk()
root.geometry("600x600")
root.iconbitmap('TestCover/icons8-slice-48.png')
root.title("Gerador de Relatório de Cobertura")

button_frame = tk.Frame(root)
button_frame.pack(pady=30)

button1 = tk.Button(button_frame, text="Cobertura do Cronos NG", command=coverage_test_from_CRONOS_NG, width=40)
button1.pack(anchor="center")

tk.Label(button_frame, text="").pack()

button2 = tk.Button(button_frame, text="Cobertura do medidor Bulk", command=coverage_test_from_Bulk_Meter, width=40)
button2.pack(anchor="center")

tk.Label(button_frame, text="").pack()

button3 = tk.Button(button_frame, text="Cobertura do Religador", command=coverage_test_from_RECLOSER, width=40)
button3.pack(anchor="center")

tk.Label(button_frame, text="").pack()

button4 = tk.Button(button_frame, text="Cobertura do medidor de Água", command=coverage_test_from_WATER, width=40)
button4.pack(anchor="center")

tk.Label(button_frame, text="").pack()

button5 = tk.Button(button_frame, text="Cobertura do ZEUS NG", command=coverage_test_from_ZEUS_NG, width=40)
button5.pack(anchor="center")

tk.Label(button_frame, text="").pack()

button6 = tk.Button(button_frame, text="Cobertura do ZEUS THS", command=coverage_test_from_ZEUS_THS, width=40)
button6.pack(anchor="center")

tk.Label(button_frame, text="").pack()

button7 = tk.Button(button_frame, text="Cobertura do ZEUS", command=coverage_test_from_ZEUS, width=40)
button7.pack(anchor="center")

tk.Label(button_frame, text="").pack()

button8 = tk.Button(button_frame, text="Cobertura da Utils", command=coverage_test_from_Utils, width=40)
button8.pack(anchor="center")

tk.Label(button_frame, text="").pack()

button9 = tk.Button(button_frame, text="Cobertura da Lib Modbus", command=coverage_test_lib_mobdus, width=40)
button9.pack(anchor="center")

tk.Label(button_frame, text="").pack()

buttonclose = tk.Button(button_frame, text="Fechar aplicativo", command=fechar_aplicativo, width=40)
buttonclose.pack(anchor="center")

tk.Label(button_frame, text="").pack()

root.mainloop()