v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
B 2 585 -705 1385 -305 {flags=graph

y2=0.62
ypos1=0
ypos2=2
divy=5
subdivy=1
unity=1
x1=0
x2=3.2e-07
divx=5
subdivx=1

dataset=-1
unitx=1
logx=0
logy=0


y1=0.58
rainbow=0

color="4 4 4 4 4 4 4 4"
node="v_in1
v_in2
v_in3
v_in4
v_in5
v_in6
v_in7
v_in8"}
B 2 585 -1135 1385 -735 {flags=graph

y2=1.3
ypos1=0
ypos2=2
divy=5
subdivy=1
unity=1
x1=0
x2=3.2e-07
divx=5
subdivx=1

dataset=-1
unitx=1
logx=0
logy=0


y1=0
rainbow=0



color=4
node=ctrl}
B 2 585 -285 1385 115 {flags=graph

y2=0.25
ypos1=0
ypos2=2
divy=5
subdivy=1
unity=1
x1=0
x2=3.2e-07
divx=5
subdivx=1

dataset=-1
unitx=1
logx=0
logy=0


y1=0.085
rainbow=0

color=9
node=v_out}
N -265 -660 -265 -640 {
lab=GND}
N 350 -425 350 -405 {
lab=V_out}
N -265 -760 -265 -720 {
lab=1.2V}
N 350 -455 350 -425 {
lab=V_out}
N 40 -515 40 -495 {
lab=#net1}
N 40 -585 40 -575 {
lab=1.2V}
N 100 -355 100 -345 {
lab=GND}
N -395 -485 -395 -465 {
lab=GND}
N -395 -555 -395 -545 {
lab=ctrl}
N -390 -300 -390 -280 {
lab=GND}
N -390 -370 -390 -360 {
lab=V_in1}
N -165 -660 -165 -640 {
lab=GND}
N -165 -760 -165 -720 {
lab=3.3V}
N -90 -425 -50 -425 {lab=V_in1}
N -90 -385 -50 -385 {lab=ctrl}
N 170 -515 170 -495 {lab=#net2}
N 170 -585 170 -575 {lab=3.3V}
N 35 -210 35 -190 {lab=1.2V}
N 165 -210 165 -190 {lab=3.3V}
N -250 -80 -190 -80 {lab=ctrl}
N 355 -120 410 -120 {lab=#net3}
N 250 -425 350 -425 {
lab=V_out}
N -340 -655 -340 -635 {
lab=GND}
N -340 -760 -340 -715 {lab=Vclamp}
N -190 -120 -55 -120 {lab=Vclamp}
N -640 -655 -640 -635 {
lab=GND}
N -640 -755 -640 -715 {
lab=VSS}
N -540 -655 -540 -635 {
lab=GND}
N -540 -755 -540 -715 {
lab=VDD}
N 405 -340 405 -325 {lab=GND}
N 350 -345 350 -320 {lab=GND}
N 405 -425 405 -400 {lab=V_out}
N 350 -425 405 -425 {lab=V_out}
N 410 -35 410 -20 {lab=GND}
N 355 -40 355 -15 {lab=GND}
N 410 -120 410 -95 {lab=#net3}
N 355 -120 355 -100 {lab=#net3}
N 245 -120 355 -120 {lab=#net3}
N -110 -80 -55 -80 {lab=#net4}
C {devices/code_shown.sym} -385 -1035 0 0 {name=MODEL only_toplevel=true
format="tcleval( @value )"
value="
.lib cornerMOSlv.lib mos_tt\\
.lib cornerMOShv.lib mos_tt\\
.lib cornerRES.lib res_typ\\
.include sg13g2_stdcell.spice
"}
C {devices/code_shown.sym} 80 -1075 0 0 {name=NGSPICE only_toplevel=true 
value="
.param temp=27
.control
save all 
tran 100p 320n
write tran_lshift.raw
.endc
"}
C {devices/vsource.sym} -265 -690 0 0 {name=Vpow value=1.2}
C {devices/title.sym} -130 260 0 0 {name=l5 author="Copyright 2023 IHP PDK Authors"}
C {devices/launcher.sym} 655 155 0 0 {name=h5
descr="load waves" 
tclcommand="xschem raw_read $netlist_dir/tran_lshift.raw tran"
}
C {devices/gnd.sym} 100 -345 0 0 {name=l2 lab=GND}
C {devices/ammeter.sym} 40 -545 0 0 {name=Vp}
C {devices/gnd.sym} -265 -640 0 0 {name=l1 lab=GND}
C {devices/lab_pin.sym} 350 -455 1 0 {name=p3 sig_type=std_logic lab=V_out}
C {devices/capa.sym} 350 -375 0 0 {name=C1
m=1
value=1p
footprint=1206
device="ceramic capacitor"}
C {devices/gnd.sym} 350 -320 0 0 {name=l6 lab=GND}
C {devices/lab_pin.sym} -265 -760 1 0 {name=p4 sig_type=std_logic lab=1.2V}
C {devices/lab_pin.sym} -90 -385 0 0 {name=p9 sig_type=std_logic lab=ctrl}
C {devices/vsource.sym} -395 -515 0 0 {name=Ven3 value="dc 0 ac 1 pulse(0.0, 1.2, 50n, 1n, 1n, 200n, 1u)"}
C {devices/gnd.sym} -395 -465 0 0 {name=l10 lab=GND}
C {devices/lab_pin.sym} -395 -555 1 0 {name=p11 sig_type=std_logic lab=ctrl}
C {devices/vsource.sym} -390 -330 0 0 {name=Vin2 value="dc 0 ac 1 sin(0.6, 20m, 20meg, 0, 0)"}
C {devices/gnd.sym} -390 -280 0 0 {name=l11 lab=GND}
C {devices/lab_pin.sym} -390 -370 1 0 {name=p12 sig_type=std_logic lab=V_in1}
C {devices/vsource.sym} -165 -690 0 0 {name=Vpow1 value=3.3}
C {devices/gnd.sym} -165 -640 0 0 {name=l3 lab=GND}
C {devices/lab_pin.sym} -165 -760 1 0 {name=p1 sig_type=std_logic lab=3.3V}
C {devices/lab_pin.sym} 40 -585 1 0 {name=p2 sig_type=std_logic lab=1.2V}
C {devices/lab_pin.sym} 170 -585 1 0 {name=p5 sig_type=std_logic lab=3.3V}
C {devices/ammeter.sym} 170 -545 0 0 {name=Vp1}
C {level_shifter.sym} 100 -425 0 0 {name=x1}
C {devices/lab_pin.sym} -90 -425 0 0 {name=p6 sig_type=std_logic lab=V_in1}
C {level_shifter.sym} 95 -120 0 0 {name=x2}
C {devices/lab_pin.sym} 35 -210 1 0 {name=p7 sig_type=std_logic lab=1.2V}
C {devices/lab_pin.sym} 165 -210 1 0 {name=p8 sig_type=std_logic lab=3.3V}
C {sg13g2_stdcells/sg13g2_inv_1.sym} -150 -80 0 0 {name=x3 VDD=VDD VSS=VSS prefix=sg13g2_ }
C {devices/lab_pin.sym} -250 -80 0 0 {name=p10 sig_type=std_logic lab=ctrl}
C {devices/vsource.sym} -340 -685 0 0 {name=Vclamp value=2}
C {devices/gnd.sym} -340 -635 0 0 {name=l4 lab=GND}
C {devices/lab_pin.sym} -340 -760 1 0 {name=p13 sig_type=std_logic lab=Vclamp}
C {devices/lab_pin.sym} -190 -120 0 0 {name=p14 sig_type=std_logic lab=Vclamp}
C {devices/vsource.sym} -640 -685 0 0 {name=Vpow2 value=0}
C {devices/gnd.sym} -640 -635 0 0 {name=l7 lab=GND
value=VDD}
C {devices/lab_pin.sym} -640 -755 1 0 {name=p15 sig_type=std_logic lab=VSS}
C {devices/vsource.sym} -540 -685 0 0 {name=Vpow3 value=1.2V}
C {devices/gnd.sym} -540 -635 0 0 {name=l8 lab=GND
value=VDD}
C {devices/lab_pin.sym} -540 -755 1 0 {name=p17 sig_type=std_logic lab=VDD}
C {res.sym} 405 -370 0 0 {name=R1
value=1k
footprint=1206
device=resistor
m=1}
C {devices/gnd.sym} 405 -325 0 0 {name=l9 lab=GND}
C {devices/capa.sym} 355 -70 0 0 {name=C2
m=1
value=1p
footprint=1206
device="ceramic capacitor"}
C {devices/gnd.sym} 355 -15 0 0 {name=l12 lab=GND}
C {res.sym} 410 -65 0 0 {name=R2
value=1k
footprint=1206
device=resistor
m=1}
C {devices/gnd.sym} 410 -20 0 0 {name=l13 lab=GND}
