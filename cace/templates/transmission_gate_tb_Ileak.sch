v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 670 -400 670 -380 {
lab=GND}
N 60 100 60 130 {
lab=GND}
N 1030 -400 1030 -380 {
lab=GND}
N 670 -210 670 -200 {
lab=GND}
N 670 -500 670 -460 {
lab=Vdd}
N 670 -290 670 -270 {
lab=V_in}
N 1030 -470 1030 -460 {
lab=en_p}
N 1030 -230 1030 -210 {
lab=GND}
N 1030 -300 1030 -290 {
lab=en_n}
N -130 50 -90 50 {
lab=en_n}
N -130 70 -90 70 {
lab=en_p}
N 310 20 310 40 {
lab=V_out1}
N 310 100 310 110 {
lab=GND}
N 290 20 310 20 {
lab=V_out1}
N 310 -10 310 20 {
lab=V_out1}
N 210 20 230 20 {
lab=#net1}
N -150 20 -90 20 {
lab=#net2}
N -240 20 -210 20 {
lab=V_in}
N 60 -30 60 -20 {
lab=#net3}
N 60 -100 60 -90 {
lab=Vdd}
N 850 100 850 130 {
lab=GND}
N 660 50 700 50 {
lab=en_p}
N 660 70 700 70 {
lab=en_n}
N 1100 -10 1100 20 {
lab=V_in}
N 640 20 700 20 {
lab=#net4}
N 850 -30 850 -20 {
lab=#net5}
N 850 -100 850 -90 {
lab=Vdd}
N 1000 20 1100 20 {
lab=V_in}
N 470 100 470 110 {
lab=GND}
N 470 20 470 40 {
lab=#net6}
N 470 20 580 20 {
lab=#net6}
C {devices/vsource.sym} 670 -430 0 0 {name=Vpow value=CACE\{vdd\}}
C {devices/title.sym} -130 260 0 0 {name=l5 author="Copyright 2023 IHP PDK Authors"}
C {devices/gnd.sym} 60 130 0 0 {name=l2 lab=GND}
C {devices/ammeter.sym} 60 -60 0 0 {name=Vp}
C {devices/gnd.sym} 670 -380 0 0 {name=l1 lab=GND}
C {devices/vsource.sym} 670 -240 0 0 {name=Vin value=CACE\{Vin\}}
C {devices/vsource.sym} 1030 -430 0 0 {name=Ven value=CACE\{Vp\}}
C {devices/gnd.sym} 1030 -380 0 0 {name=l3 lab=GND}
C {devices/gnd.sym} 670 -200 0 0 {name=l4 lab=GND}
C {devices/lab_pin.sym} 670 -290 1 0 {name=p1 sig_type=std_logic lab=V_in}
C {devices/lab_pin.sym} 1030 -470 1 0 {name=p2 sig_type=std_logic lab=en_p}
C {devices/lab_pin.sym} 310 -10 1 0 {name=p3 sig_type=std_logic lab=V_out1}
C {devices/lab_pin.sym} 670 -500 1 0 {name=p4 sig_type=std_logic lab=Vdd}
C {devices/vsource.sym} 1030 -260 0 0 {name=Ven1 value=CACE\{Vn\}}
C {devices/gnd.sym} 1030 -210 0 0 {name=l7 lab=GND}
C {devices/lab_pin.sym} 1030 -300 1 0 {name=p5 sig_type=std_logic lab=en_n}
C {devices/lab_pin.sym} 60 -100 1 0 {name=p6 sig_type=std_logic lab=Vdd}
C {transmission_gate.sym} 60 40 0 0 {name=x1}
C {devices/lab_pin.sym} -240 20 0 0 {name=p7 sig_type=std_logic lab=V_in}
C {devices/lab_pin.sym} -130 70 0 0 {name=p8 sig_type=std_logic lab=en_p}
C {devices/lab_pin.sym} -130 50 0 0 {name=p9 sig_type=std_logic lab=en_n}
C {devices/gnd.sym} 310 110 0 0 {name=l6 lab=GND}
C {devices/vsource.sym} 310 70 0 0 {name=Vout value=1.6}
C {devices/ammeter.sym} 260 20 1 0 {name=Vp1}
C {devices/ammeter.sym} -180 20 1 0 {name=Vp2}
C {devices/gnd.sym} 850 130 0 0 {name=l8 lab=GND}
C {devices/ammeter.sym} 850 -60 0 0 {name=Vp3}
C {devices/lab_pin.sym} 1100 -10 1 0 {name=p10 sig_type=std_logic lab=V_in}
C {devices/lab_pin.sym} 850 -100 1 0 {name=p11 sig_type=std_logic lab=Vdd}
C {transmission_gate.sym} 850 40 0 0 {name=x2}
C {devices/lab_pin.sym} 660 50 0 0 {name=p13 sig_type=std_logic lab=en_p}
C {devices/lab_pin.sym} 660 70 0 0 {name=p14 sig_type=std_logic lab=en_n}
C {devices/ammeter.sym} 610 20 3 0 {name=Vp5}
C {devices/vsource.sym} 470 70 0 0 {name=Vin1 value=1.6}
C {devices/gnd.sym} 470 110 0 0 {name=l9 lab=GND}
C {devices/code_shown.sym} -300 -710 0 0 {name=MODEL1 only_toplevel=true
format="tcleval( @value )"
value="
.lib CACE\{PDK_ROOT\}/CACE\{PDK\}/libs.tech/ngspice/models/cornerMOShv.lib mos_CACE\{corner\}
.lib cornerRES.lib res_typ

.include CACE\{DUT_path\}

.temp CACE\{temperature\}
.param m1_w=CACE\{m1_w\}
.param m2_w=CACE\{m2_w\}
"}
C {devices/code_shown.sym} -290 -420 0 0 {name=NGSPICE1 only_toplevel=true 
value="
.control
save all 
op
let Ileak1=I(Vp1)
let Ileak2=I(Vp5)
echo $&Ileak1 > CACE\{simpath\}/CACE\{filename\}_CACE\{N\}.data
.endc
"}
