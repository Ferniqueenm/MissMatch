v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N -100 -290 -100 -200 {lab=#net1}
N 100 -230 100 -200 {lab=#net2}
N -100 -140 -100 -50 {lab=Vss}
N 100 -50 430 -50 {lab=Vss}
N 50 -170 100 -170 {lab=Vss}
N 50 -170 50 -50 {lab=Vss}
N 0 -50 50 -50 {lab=Vss}
N -100 -170 -40 -170 {lab=Vss}
N -40 -170 -40 -50 {lab=Vss}
N -100 -50 -40 -50 {lab=Vss}
N 0 -50 0 30 {lab=Vss}
N -40 -50 0 -50 {lab=Vss}
N -230 -170 -230 -150 {lab=#net3}
N -230 -170 -140 -170 {lab=#net3}
N -230 -190 -230 -170 {lab=#net3}
N -230 -120 -210 -120 {lab=Vss}
N -210 -120 -210 -50 {lab=Vss}
N -230 -90 -230 -50 {lab=Vss}
N -210 -50 -100 -50 {lab=Vss}
N -230 -50 -210 -50 {lab=Vss}
N 100 -400 100 -380 {lab=3.3V}
N -160 -350 -100 -350 {lab=3.3V}
N -160 -400 -160 -350 {lab=3.3V}
N -160 -400 -100 -400 {lab=3.3V}
N -100 -400 -100 -380 {lab=3.3V}
N 100 -400 160 -400 {lab=3.3V}
N 160 -400 160 -350 {lab=3.3V}
N 100 -350 160 -350 {lab=3.3V}
N -10 -400 100 -400 {lab=3.3V}
N -10 -440 -10 -400 {lab=3.3V}
N -100 -400 -10 -400 {lab=3.3V}
N -230 -440 -230 -250 {lab=1.2V}
N -310 -220 -270 -220 {lab=ctrl}
N -310 -170 -310 -120 {lab=ctrl}
N -310 -120 -270 -120 {lab=ctrl}
N -340 -170 -310 -170 {lab=ctrl}
N -340 -170 -340 -10 {lab=ctrl}
N -310 -220 -310 -170 {lab=ctrl}
N -340 -10 170 -10 {lab=ctrl}
N 170 -170 170 -10 {lab=ctrl}
N 140 -170 170 -170 {lab=ctrl}
N -370 -170 -340 -170 {lab=ctrl}
N 390 -250 390 -180 {lab=IO2}
N 480 -250 560 -250 {lab=IO2}
N 560 -250 560 -180 {lab=IO2}
N 390 -120 390 -40 {lab=IO1}
N 480 -40 560 -40 {lab=IO1}
N 560 -120 560 -40 {lab=IO1}
N 160 -400 520 -400 {lab=3.3V}
N 100 -230 250 -230 {lab=#net2}
N 250 -230 250 -150 {lab=#net2}
N 100 -320 100 -230 {lab=#net2}
N 250 -150 350 -150 {lab=#net2}
N 40 -290 660 -290 {lab=#net1}
N 660 -290 660 -150 {lab=#net1}
N -100 -320 -100 -290 {lab=#net1}
N 600 -150 660 -150 {lab=#net1}
N 480 -40 480 20 {lab=IO1}
N 390 -40 480 -40 {lab=IO1}
N 520 -150 560 -150 {lab=3.3V}
N 520 -400 520 -150 {lab=3.3V}
N 390 -250 480 -250 {lab=IO2}
N 480 -440 480 -250 {lab=IO2}
N 40 -350 60 -350 {lab=#net1}
N 40 -350 40 -290 {lab=#net1}
N -100 -290 40 -290 {lab=#net1}
N -60 -350 -30 -350 {lab=#net2}
N -30 -350 -30 -230 {lab=#net2}
N -30 -230 100 -230 {lab=#net2}
N 390 -150 430 -150 {lab=Vss}
N 430 -150 430 -50 {lab=Vss}
N 100 -140 100 -50 {lab=Vss}
N 50 -50 100 -50 {lab=Vss}
C {devices/title.sym} -310 160 0 0 {name=l5 author="Copyright 2025 IHP PDK Authors"}
C {devices/iopin.sym} 480 20 1 0 {name=p1 lab=IO1}
C {devices/iopin.sym} 0 30 1 0 {name=p4 lab=Vss}
C {devices/iopin.sym} 480 -440 3 0 {name=p7 lab=IO2}
C {devices/iopin.sym} -10 -440 3 0 {name=p38 lab=3.3V}
C {devices/ipin.sym} -370 -170 0 0 {name=p3 lab=ctrl}
C {devices/iopin.sym} -230 -440 3 0 {name=p8 lab=1.2V}
C {sg13g2_pr/sg13_hv_pmos.sym} 80 -350 0 0 {name=M2
l=0.4u
w=0.3u
ng=1
m=1
model=sg13_hv_pmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_nmos.sym} -250 -120 0 0 {name=M3
l=0.13u
w=0.15u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_pmos.sym} -250 -220 0 0 {name=M5
l=0.13u
w=0.15u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_nmos.sym} -120 -170 0 0 {name=M6
l=0.13u
w=0.15u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_nmos.sym} 120 -170 0 1 {name=M7
l=0.13u
w=0.15u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
C {sg13g2_pr/sg13_hv_pmos.sym} -80 -350 0 1 {name=M1
l=0.4u
w=0.3u
ng=1
m=1
model=sg13_hv_pmos
spiceprefix=X
}
C {sg13g2_pr/sg13_hv_pmos.sym} 580 -150 0 1 {name=M4
l=0.4u
w=0.3u
ng=1
m=1
model=sg13_hv_pmos
spiceprefix=X
}
C {sg13g2_pr/sg13_hv_nmos.sym} 370 -150 0 0 {name=M8
l=0.45u
w=0.3u
ng=1
m=1
model=sg13_hv_nmos
spiceprefix=X
}
