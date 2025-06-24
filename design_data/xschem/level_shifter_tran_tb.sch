v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
B 2 585 -705 1385 -305 {flags=graph

y2=1.5
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


y1=0.5
rainbow=0

color="4 6"
node="v_in1
v_out"}
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



color="4 6 7 8 9"
node="ctrl
x1.d1
x1.d2
x1.g1
x1.g2"}
B 2 585 -285 1385 115 {flags=graph

y2=1.8
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


y1=-0.21
rainbow=0

color="9 4 6"
node="v_g
v_s
v_d"}
N 165 -720 165 -700 {
lab=GND}
N 165 -820 165 -780 {
lab=1.2V}
N -335 -785 -335 -765 {
lab=GND}
N -335 -855 -335 -845 {
lab=ctrl}
N -330 -600 -330 -580 {
lab=GND}
N -330 -670 -330 -660 {
lab=V_in1}
N 265 -720 265 -700 {
lab=GND}
N 265 -820 265 -780 {
lab=3.3V}
N 385 -720 385 -700 {
lab=GND}
N 385 -820 385 -780 {
lab=Vcl}
N 180 -400 180 -370 {lab=1.2V}
N 240 -400 240 -370 {lab=3.3V}
N 310 -400 310 -370 {lab=Vcl}
N 180 -310 180 -280 {lab=#net1}
N 240 -310 240 -280 {lab=#net2}
N 310 -310 310 -280 {lab=#net3}
N 240 -140 240 -120 {lab=GND}
N 50 -170 90 -170 {lab=ctrl}
N -170 -210 90 -210 {lab=#net4}
N -150 -230 90 -230 {lab=#net5}
N -150 -290 -150 -230 {lab=#net5}
N -170 -290 -150 -290 {lab=#net5}
N -170 -370 -130 -370 {lab=V_in1}
N -130 -370 -130 -250 {lab=V_in1}
N -15 -250 90 -250 {lab=V_in1}
N 440 -110 440 -100 {lab=GND}
N 440 -190 440 -170 {lab=V_s}
N 390 -200 440 -200 {lab=V_s}
N 390 -220 530 -220 {lab=V_g}
N 530 -125 530 -100 {lab=GND}
N 530 -220 530 -185 {lab=V_g}
N 530 -230 530 -220 {lab=V_g}
N 440 -190 455 -190 {lab=V_s}
N 440 -200 440 -190 {lab=V_s}
N -15 -290 -15 -250 {lab=V_in1}
N -130 -250 -15 -250 {lab=V_in1}
N 240 140 240 165 {lab=GND}
N 65 110 90 110 {lab=ctrl}
N -135 35 -135 60 {lab=#net6}
N -165 35 -135 35 {lab=#net6}
N -15 80 90 80 {lab=V_in2}
N -135 80 -135 120 {lab=V_in2}
N -165 120 -135 120 {lab=V_in2}
N 390 70 465 70 {lab=V_d}
N 465 70 465 100 {lab=V_d}
N 465 70 475 70 {lab=V_d}
N -135 60 90 60 {lab=#net6}
N -70 -595 -70 -575 {
lab=GND}
N -70 -665 -70 -655 {
lab=V_in2}
N -15 30 -15 80 {lab=V_in2}
N -135 80 -15 80 {lab=V_in2}
C {devices/code_shown.sym} -385 -1035 0 0 {name=MODEL only_toplevel=true
format="tcleval( @value )"
value="
.lib cornerMOSlv.lib mos_tt\\
.lib cornerMOShv.lib mos_tt\\
.lib cornerRES.lib res_typ\\
.include sg13g2_stdcell.spice
.include sg13g2_bondpad.lib
"}
C {devices/code_shown.sym} 80 -1075 0 0 {name=NGSPICE only_toplevel=true 
value="
.param temp=27
.control
save all 
tran 50p 320n
write tran_lshift.raw
.endc
"}
C {devices/vsource.sym} 165 -750 0 0 {name=Vpow value=1.2}
C {devices/title.sym} -130 260 0 0 {name=l5 author="Copyright 2023 IHP PDK Authors"}
C {devices/launcher.sym} 655 155 0 0 {name=h5
descr="load waves" 
tclcommand="xschem raw_read $netlist_dir/tran_lshift.raw tran"
}
C {devices/gnd.sym} 240 -120 0 0 {name=l2 lab=GND}
C {devices/ammeter.sym} 180 -340 0 0 {name=Vp}
C {devices/gnd.sym} 165 -700 0 0 {name=l1 lab=GND}
C {devices/capa.sym} 530 -155 0 0 {name=C1
m=1
value=100f
footprint=1206
device="ceramic capacitor"}
C {devices/lab_pin.sym} 165 -820 1 0 {name=p4 sig_type=std_logic lab=1.2V}
C {devices/lab_pin.sym} 50 -170 0 0 {name=p9 sig_type=std_logic lab=ctrl}
C {devices/vsource.sym} -335 -815 0 0 {name=Ven3 value="dc 0 ac 1 pulse(0.0, 1.2, 50n, 1n, 1n, 200n, 1u)"}
C {devices/gnd.sym} -335 -765 0 0 {name=l10 lab=GND}
C {devices/lab_pin.sym} -335 -855 1 0 {name=p11 sig_type=std_logic lab=ctrl}
C {devices/vsource.sym} -330 -630 0 0 {name=Vin2 value="dc 0 ac 1 sin(1.0, 500m, 20meg, 0, 0)"}
C {devices/gnd.sym} -330 -580 0 0 {name=l11 lab=GND}
C {devices/lab_pin.sym} -330 -670 1 0 {name=p12 sig_type=std_logic lab=V_in1}
C {devices/vsource.sym} 265 -750 0 0 {name=Vpow1 value=3.3}
C {devices/gnd.sym} 265 -700 0 0 {name=l3 lab=GND}
C {devices/lab_pin.sym} 265 -820 1 0 {name=p1 sig_type=std_logic lab=3.3V}
C {devices/lab_pin.sym} 180 -400 1 0 {name=p2 sig_type=std_logic lab=1.2V}
C {devices/lab_pin.sym} 240 -400 1 0 {name=p5 sig_type=std_logic lab=3.3V}
C {devices/ammeter.sym} 240 -340 0 0 {name=Vp1}
C {devices/lab_pin.sym} -15 -290 1 0 {name=p6 sig_type=std_logic lab=V_in1}
C {devices/ammeter.sym} 310 -340 0 0 {name=Vp2}
C {devices/lab_pin.sym} 310 -400 1 0 {name=p7 sig_type=std_logic lab=Vcl}
C {devices/vsource.sym} 385 -750 0 0 {name=Vpow2 value=-0.2}
C {devices/gnd.sym} 385 -700 0 0 {name=l4 lab=GND}
C {devices/lab_pin.sym} 385 -820 1 0 {name=p8 sig_type=std_logic lab=Vcl}
C {res.sym} 440 -140 0 0 {name=R1
value=1k
footprint=1206
device=resistor
m=1}
C {devices/gnd.sym} 440 -100 0 0 {name=l7 lab=GND}
C {sg13g2_pr/bondpad.sym} -210 -210 3 0 {name=X2
model=bondpad
spiceprefix=X
size=80u
shape=0
padtype=0
}
C {sg13g2_pr/bondpad.sym} -210 -290 3 0 {name=X3
model=bondpad
spiceprefix=X
size=80u
shape=0
padtype=0
}
C {sg13g2_pr/bondpad.sym} -210 -370 3 0 {name=X4
model=bondpad
spiceprefix=X
size=80u
shape=0
padtype=0
}
C {devices/gnd.sym} 530 -100 0 0 {name=l8 lab=GND}
C {devices/lab_pin.sym} 530 -230 1 0 {name=p13 sig_type=std_logic lab=V_g}
C {devices/lab_pin.sym} 455 -190 2 0 {name=p14 sig_type=std_logic lab=V_s}
C {level_shifter_hor.sym} 240 -210 0 0 {name=x1}
C {level_shifter_ver.sym} 240 70 0 0 {name=x5}
C {devices/lab_pin.sym} 180 0 1 0 {name=p3 sig_type=std_logic lab=1.2V}
C {devices/lab_pin.sym} 300 0 1 0 {name=p10 sig_type=std_logic lab=3.3V}
C {devices/gnd.sym} 240 165 0 0 {name=l6 lab=GND}
C {devices/lab_pin.sym} 65 110 0 0 {name=p15 sig_type=std_logic lab=ctrl}
C {sg13g2_pr/bondpad.sym} -205 35 3 0 {name=X6
model=bondpad
spiceprefix=X
size=80u
shape=0
padtype=0
}
C {sg13g2_pr/bondpad.sym} -205 120 3 0 {name=X7
model=bondpad
spiceprefix=X
size=80u
shape=0
padtype=0
}
C {devices/gnd.sym} 465 160 0 0 {name=l9 lab=GND}
C {devices/lab_pin.sym} 475 70 2 0 {name=p16 sig_type=std_logic lab=V_d}
C {devices/lab_pin.sym} -15 30 1 0 {name=p17 sig_type=std_logic lab=V_in2}
C {devices/vsource.sym} -70 -625 0 0 {name=Vin1 value="dc 0 ac 1 sin(1.0, 800m, 20meg, 0, 0)"}
C {devices/gnd.sym} -70 -575 0 0 {name=l12 lab=GND}
C {devices/lab_pin.sym} -70 -665 1 0 {name=p18 sig_type=std_logic lab=V_in2}
C {devices/capa.sym} 465 130 0 0 {name=C2
m=1
value=1p
footprint=1206
device="ceramic capacitor"}
