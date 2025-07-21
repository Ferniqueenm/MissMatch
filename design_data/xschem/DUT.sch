v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
P 4 5 0 0 200 0 200 210 0 210 0 0 {}
P 4 5 200 0 400 0 400 210 200 210 200 0 {}
P 4 5 0 210 200 210 200 420 0 420 0 210 {}
P 4 5 200 210 400 210 400 420 200 420 200 210 {}
N 90 80 170 80 {lab=#net1}
N 170 80 170 120 {lab=#net1}
N 170 180 170 200 {lab=B}
N 90 110 90 150 {lab=S1}
N 10 80 50 80 {lab=G1}
N 90 30 90 50 {lab=D1}
N 10 30 90 30 {lab=D1}
N 10 200 170 200 {lab=B}
N 10 150 90 150 {lab=S1}
N 10 20 10 30 {lab=D1}
N 10 70 10 80 {lab=G1}
N 10 140 10 150 {lab=S1}
N 10 190 10 200 {lab=B}
N 290 80 370 80 {lab=#net2}
N 370 80 370 120 {lab=#net2}
N 370 180 370 200 {lab=B}
N 290 110 290 150 {lab=S1}
N 210 80 250 80 {lab=G1}
N 290 30 290 50 {lab=D2}
N 210 30 290 30 {lab=D2}
N 210 200 370 200 {lab=B}
N 210 150 290 150 {lab=S1}
N 210 20 210 30 {lab=D2}
N 210 70 210 80 {lab=G1}
N 210 140 210 150 {lab=S1}
N 210 190 210 200 {lab=B}
N 90 290 170 290 {lab=#net3}
N 170 290 170 330 {lab=#net3}
N 170 390 170 410 {lab=B}
N 90 320 90 360 {lab=S2}
N 10 290 50 290 {lab=G2}
N 90 240 90 260 {lab=D1}
N 10 240 90 240 {lab=D1}
N 10 410 170 410 {lab=B}
N 10 360 90 360 {lab=S2}
N 10 230 10 240 {lab=D1}
N 10 280 10 290 {lab=G2}
N 10 350 10 360 {lab=S2}
N 10 400 10 410 {lab=B}
N 290 290 370 290 {lab=#net4}
N 370 290 370 330 {lab=#net4}
N 370 390 370 410 {lab=B}
N 290 320 290 360 {lab=S2}
N 210 290 250 290 {lab=G2}
N 290 240 290 260 {lab=D2}
N 210 240 290 240 {lab=D2}
N 210 410 370 410 {lab=B}
N 210 360 290 360 {lab=S2}
N 210 230 210 240 {lab=D2}
N 210 280 210 290 {lab=G2}
N 210 350 210 360 {lab=S2}
N 210 400 210 410 {lab=B}
C {devices/iopin.sym} 0 50 2 0 {name=p13 lab=S1
}
C {devices/iopin.sym} 0 30 2 0 {name=p15 lab=G1}
C {sg13g2_pr/sg13_lv_nmos.sym} 70 80 0 0 {name=M1
l=\{dut_l\}
w=\{dut_w\}
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
C {sg13g2_pr/ptap1.sym} 170 150 2 0 {name=R3
model=ptap1
spiceprefix=X
w=10.0e-6
w=2.0e-6
}
C {devices/iopin.sym} 100 0 1 1 {name=p1 lab=D1}
C {devices/iopin.sym} 0 0 0 1 {name=p2 lab=B}
C {lab_pin.sym} 10 20 2 0 {name=p3 sig_type=std_logic lab=D1}
C {lab_pin.sym} 10 70 2 0 {name=p4 sig_type=std_logic lab=G1}
C {lab_pin.sym} 10 140 2 0 {name=p5 sig_type=std_logic lab=S1}
C {lab_pin.sym} 10 190 2 0 {name=p6 sig_type=std_logic lab=B}
C {sg13g2_pr/sg13_lv_nmos.sym} 270 80 0 0 {name=M2
l=\{dut_l\}
w=\{dut_w\}
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
C {sg13g2_pr/ptap1.sym} 370 150 2 0 {name=R1
model=ptap1
spiceprefix=X
w=10.0e-6
w=2.0e-6
}
C {lab_pin.sym} 210 20 2 0 {name=p7 sig_type=std_logic lab=D2}
C {lab_pin.sym} 210 70 2 0 {name=p8 sig_type=std_logic lab=G1}
C {lab_pin.sym} 210 140 2 0 {name=p9 sig_type=std_logic lab=S1}
C {lab_pin.sym} 210 190 2 0 {name=p10 sig_type=std_logic lab=B}
C {sg13g2_pr/sg13_lv_nmos.sym} 70 290 0 0 {name=M3
l=\{dut_l\}
w=\{dut_w\}
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
C {sg13g2_pr/ptap1.sym} 170 360 2 0 {name=R2
model=ptap1
spiceprefix=X
w=10.0e-6
w=2.0e-6
}
C {lab_pin.sym} 10 230 2 0 {name=p11 sig_type=std_logic lab=D1}
C {lab_pin.sym} 10 280 2 0 {name=p12 sig_type=std_logic lab=G2}
C {lab_pin.sym} 10 350 2 0 {name=p14 sig_type=std_logic lab=S2}
C {lab_pin.sym} 10 400 2 0 {name=p16 sig_type=std_logic lab=B}
C {sg13g2_pr/sg13_lv_nmos.sym} 270 290 0 0 {name=M4
l=\{dut_l\}
w=\{dut_w\}
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
C {sg13g2_pr/ptap1.sym} 370 360 2 0 {name=R4
model=ptap1
spiceprefix=X
w=10.0e-6
w=2.0e-6
}
C {lab_pin.sym} 210 230 2 0 {name=p17 sig_type=std_logic lab=D2}
C {lab_pin.sym} 210 280 2 0 {name=p18 sig_type=std_logic lab=G2}
C {lab_pin.sym} 210 350 2 0 {name=p19 sig_type=std_logic lab=S2}
C {lab_pin.sym} 210 400 2 0 {name=p20 sig_type=std_logic lab=B}
C {devices/iopin.sym} 0 330 2 0 {name=p21 lab=S2}
C {devices/iopin.sym} 0 310 2 0 {name=p22 lab=G2}
C {devices/iopin.sym} 300 0 1 1 {name=p23 lab=D2}
