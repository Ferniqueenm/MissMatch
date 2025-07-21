v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 110 -590 110 -570 {
lab=GND}
N 470 -590 470 -570 {
lab=GND}
N 110 -400 110 -390 {
lab=GND}
N 110 -690 110 -650 {
lab=Vdd}
N 110 -480 110 -460 {
lab=V_in}
N 470 -660 470 -650 {
lab=en_p}
N 470 -420 470 -400 {
lab=GND}
N 470 -490 470 -480 {
lab=en_n}
N -240 20 -200 20 {
lab=V_in}
N -240 50 -200 50 {
lab=en_n}
N -240 70 -200 70 {
lab=en_p}
N 200 20 200 40 {
lab=V_out1}
N 200 100 200 110 {
lab=GND}
N -50 -100 -50 -90 {
lab=Vdd}
N -50 -30 -50 -20 {
lab=#net1}
N -50 100 -50 110 {
lab=GND}
N 100 20 120 20 {lab=#net2}
N 180 20 200 20 {lab=V_out1}
N 200 -10 200 20 {
lab=V_out1}
C {devices/code_shown.sym} -320 -570 0 0 {name=MODEL only_toplevel=true
format="tcleval( @value )"
value="
.lib cornerMOSlv.lib mos_tt\\
.lib cornerMOShv.lib mos_tt\\
.lib cornerRES.lib res_typ\\
"}
C {devices/code_shown.sym} -330 -460 0 0 {name=NGSPICE only_toplevel=true 
value="
.param temp=27
.param m1_w = 20u
.param m2_w = 20u
.control
save all 
op
let Roff=1.2/I(Vp2)
print I(Vp2) Roff
.endc
"}
C {devices/vsource.sym} 110 -620 0 0 {name=Vpow value=1.2}
C {devices/title.sym} -130 260 0 0 {name=l5 author="Copyright 2023 IHP PDK Authors"}
C {devices/gnd.sym} -50 110 0 0 {name=l2 lab=GND}
C {devices/ammeter.sym} -50 -60 0 0 {name=Vp}
C {devices/gnd.sym} 110 -570 0 0 {name=l1 lab=GND}
C {devices/vsource.sym} 110 -430 0 0 {name=Vin value=1.2}
C {devices/vsource.sym} 470 -620 0 0 {name=Ven value=0}
C {devices/gnd.sym} 470 -570 0 0 {name=l3 lab=GND}
C {devices/gnd.sym} 110 -390 0 0 {name=l4 lab=GND}
C {devices/lab_pin.sym} 110 -480 1 0 {name=p1 sig_type=std_logic lab=V_in}
C {devices/lab_pin.sym} 470 -660 1 0 {name=p2 sig_type=std_logic lab=en_p}
C {devices/lab_pin.sym} 200 -10 1 0 {name=p3 sig_type=std_logic lab=V_out1}
C {devices/lab_pin.sym} 110 -690 1 0 {name=p4 sig_type=std_logic lab=Vdd}
C {devices/vsource.sym} 470 -450 0 0 {name=Ven1 value=1.2}
C {devices/gnd.sym} 470 -400 0 0 {name=l7 lab=GND}
C {devices/lab_pin.sym} 470 -490 1 0 {name=p5 sig_type=std_logic lab=en_n}
C {devices/lab_pin.sym} -50 -100 1 0 {name=p6 sig_type=std_logic lab=Vdd}
C {devices/lab_pin.sym} -240 20 0 0 {name=p7 sig_type=std_logic lab=V_in}
C {devices/lab_pin.sym} -240 70 0 0 {name=p8 sig_type=std_logic lab=en_p}
C {devices/lab_pin.sym} -240 50 0 0 {name=p9 sig_type=std_logic lab=en_n}
C {devices/gnd.sym} 200 110 0 0 {name=l6 lab=GND}
C {devices/ammeter.sym} 150 20 3 0 {name=Vp2}
C {devices/vsource.sym} 200 70 0 0 {name=Vin1 value=0}
C {transmission_gate.sym} -50 40 0 0 {name=x1}
