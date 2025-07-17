v {xschem version=3.4.5 file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
N 400 -150 400 -140 {
lab=GND}
N 760 -160 760 -140 {
lab=GND}
N 400 30 400 40 {
lab=GND}
N 200 20 200 40 {
lab=V_out1}
N 400 -260 400 -220 {
lab=VDD}
N 400 -50 400 -30 {
lab=V_in}
N 760 -230 760 -220 {
lab=en_p}
N 760 10 760 30 {
lab=GND}
N 760 -60 760 -50 {
lab=en_n}
N -240 20 -200 20 {
lab=V_in}
N -240 50 -200 50 {
lab=en_n}
N -240 70 -200 70 {
lab=en_p}
N 200 -10 200 20 {
lab=V_out1}
N 100 20 200 20 {
lab=V_out1}
N 200 100 200 110 {
lab=GND}
N -50 -100 -50 -20 {
lab=Vdd}
N -50 100 -50 130 {
lab=VSS}
N 400 -150 500 -150 {
lab=GND}
N 400 -160 400 -150 {
lab=GND}
N 500 -160 500 -150 {
lab=GND}
N 500 -260 500 -220 {
lab=VSS}
C {devices/code_shown.sym} -350 -470 0 0 {name=MODEL only_toplevel=true
format="tcleval( @value )"
value="
.lib CACE\{PDK_ROOT\}/CACE\{PDK\}/libs.tech/ngspice/models/cornerMOSlv.lib mos_CACE\{corner\}
.lib cornerRES.lib res_typ

.include CACE\{DUT_path\}

.temp CACE\{temperature\}
"}
C {devices/code_shown.sym} -320 -300 0 0 {name=NGSPICE only_toplevel=true 
value="
.control
save all 
op
let Ron=(V(V_in)-V(V_out1))/0.001
echo $&Ron > CACE\{simpath\}/CACE\{filename\}_CACE\{N\}.data
.endc
"}
C {devices/vsource.sym} 400 -190 0 0 {name=V1 value=CACE\{vdd\}}
C {devices/title.sym} -130 260 0 0 {name=l5 author="Copyright 2023 IHP PDK Authors"}
C {devices/gnd.sym} 400 -140 0 0 {name=l1 lab=GND}
C {devices/vsource.sym} 400 0 0 0 {name=V3 value=CACE\{vin\}}
C {devices/vsource.sym} 760 -190 0 0 {name=Ven_p value=1.2}
C {devices/gnd.sym} 760 -140 0 0 {name=l3 lab=GND}
C {devices/gnd.sym} 400 40 0 0 {name=l4 lab=GND}
C {devices/lab_pin.sym} 400 -50 1 0 {name=p1 sig_type=std_logic lab=V_in}
C {devices/lab_pin.sym} 760 -230 1 0 {name=p2 sig_type=std_logic lab=en_p}
C {devices/lab_pin.sym} 200 -10 1 0 {name=p3 sig_type=std_logic lab=V_out1}
C {devices/lab_pin.sym} 400 -260 1 0 {name=p4 sig_type=std_logic lab=VDD}
C {devices/vsource.sym} 760 -20 0 0 {name=Ven_n value=0}
C {devices/gnd.sym} 760 30 0 0 {name=l7 lab=GND}
C {devices/lab_pin.sym} 760 -60 1 0 {name=p5 sig_type=std_logic lab=en_n}
C {devices/lab_pin.sym} -50 -100 1 0 {name=p6 sig_type=std_logic lab=Vdd}
C {devices/lab_pin.sym} -240 20 0 0 {name=p7 sig_type=std_logic lab=V_in}
C {devices/lab_pin.sym} -240 70 0 0 {name=p8 sig_type=std_logic lab=en_p}
C {devices/lab_pin.sym} -240 50 0 0 {name=p9 sig_type=std_logic lab=en_n}
C {devices/isource.sym} 200 70 0 0 {name=I0 value=1m}
C {devices/gnd.sym} 200 110 0 0 {name=l6 lab=GND}
C {transmission_gate.sym} -50 40 0 0 {name=x1}
C {devices/vsource.sym} 500 -190 0 0 {name=V2 value=0}
C {devices/lab_pin.sym} 500 -260 1 0 {name=p15 sig_type=std_logic lab=VSS}
C {devices/lab_pin.sym} -50 130 3 0 {name=p17 sig_type=std_logic lab=VSS}
