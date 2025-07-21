v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 870 -830 870 -740 {lab=Drain}
N 790 -740 870 -740 {lab=Drain}
N 700 -830 700 -740 {lab=Drain}
N 790 -740 790 -670 {lab=Drain}
N 700 -740 790 -740 {lab=Drain}
N 790 -670 980 -670 {lab=Drain}
N 980 -670 980 -510 {lab=Drain}
N 1070 -830 1070 -740 {lab=Drain}
N 1160 -740 1240 -740 {lab=Drain}
N 1240 -830 1240 -740 {lab=Drain}
N 1160 -740 1160 -670 {lab=Drain}
N 1070 -740 1160 -740 {lab=Drain}
N 980 -670 1160 -670 {lab=Drain}
N 700 -970 700 -890 {lab=Dsense}
N 790 -970 870 -970 {lab=Dsense}
N 870 -970 870 -890 {lab=Dsense}
N 1070 -970 1070 -890 {lab=Dforce}
N 1160 -970 1240 -970 {lab=Dforce}
N 1240 -970 1240 -890 {lab=Dforce}
N 790 -1090 1360 -1090 {lab=Dsense}
N 790 -1090 790 -970 {lab=Dsense}
N 700 -970 790 -970 {lab=Dsense}
N 1160 -1060 1360 -1060 {lab=Dforce}
N 1160 -1060 1160 -970 {lab=Dforce}
N 1070 -970 1160 -970 {lab=Dforce}
N 1280 -860 1300 -860 {lab=ctrl_n}
N 1300 -1160 1300 -860 {lab=ctrl_n}
N 1000 -1160 1300 -1160 {lab=ctrl_n}
N 1000 -1230 1000 -1160 {lab=ctrl_n}
N 990 -860 1030 -860 {lab=ctrl_p}
N 990 -1130 990 -860 {lab=ctrl_p}
N 930 -1130 990 -1130 {lab=ctrl_p}
N 930 -1230 930 -1130 {lab=ctrl_p}
N 620 -1130 930 -1130 {lab=ctrl_p}
N 620 -1130 620 -860 {lab=ctrl_p}
N 620 -860 660 -860 {lab=ctrl_p}
N 910 -860 960 -860 {lab=ctrl_n}
N 960 -1160 960 -860 {lab=ctrl_n}
N 960 -1160 1000 -1160 {lab=ctrl_n}
N 1070 -860 1110 -860 {lab=#net1}
N 1110 -860 1110 -640 {lab=#net1}
N 1200 -860 1240 -860 {lab=#net2}
N 1200 -860 1200 -640 {lab=#net2}
N 830 -860 870 -860 {lab=#net3}
N 830 -860 830 -640 {lab=#net3}
N 700 -860 740 -860 {lab=#net4}
N 740 -860 740 -640 {lab=#net4}
N 740 -580 740 -540 {lab=Vss}
N 1350 -1000 1350 -540 {lab=Vss}
N 1350 -1000 1360 -1000 {lab=Vss}
N 1330 -1030 1360 -1030 {lab=1.2V}
N 1330 -1030 1330 -560 {lab=1.2V}
N 1200 -560 1330 -560 {lab=1.2V}
N 1200 -580 1200 -560 {lab=1.2V}
N 830 -560 1200 -560 {lab=1.2V}
N 830 -580 830 -560 {lab=1.2V}
N 1110 -540 1350 -540 {lab=Vss}
N 1110 -580 1110 -540 {lab=Vss}
N 740 -540 1110 -540 {lab=Vss}
C {devices/iopin.sym} 1360 -1000 0 0 {name=p4 lab=Vss}
C {devices/ipin.sym} 1000 -1230 1 0 {name=p3 lab=ctrl_n}
C {devices/iopin.sym} 1360 -1030 0 0 {name=p8 lab=1.2V}
C {devices/iopin.sym} 1360 -1090 0 0 {name=p13 lab=Dsense}
C {devices/iopin.sym} 980 -510 1 0 {name=p14 lab=Drain}
C {devices/iopin.sym} 1360 -1060 0 0 {name=p15 lab=Dforce}
C {sg13g2_pr/sg13_lv_nmos.sym} 680 -860 0 0 {name=M4
l=0.13u
w=0.15u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_pmos.sym} 890 -860 0 1 {name=M8
l=0.13u
w=0.30u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_pmos.sym} 1260 -860 0 1 {name=M9
l=0.13u
w=\{m2_w\}
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_nmos.sym} 1050 -860 0 0 {name=M10
l=0.13u
w=\{m1_w\}
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
C {title-3.sym} 200 150 0 0 {name=l2 author="IHP Open PDK Authors 2025" title="Drain line control circuit" rev=1.0 lock=true}
C {devices/ipin.sym} 930 -1230 1 0 {name=p1 lab=ctrl_p}
C {sg13g2_pr/ptap1.sym} 740 -610 2 0 {name=R1
model=ptap1
spiceprefix=X
w=10.0e-6
l=1.0e-6
}
C {sg13g2_pr/ntap1.sym} 1200 -610 2 0 {name=R2
model=ntap1
spiceprefix=X
w=25.0e-6
l=1.0e-6
}
C {sg13g2_pr/ptap1.sym} 1110 -610 2 0 {name=R3
model=ptap1
spiceprefix=X
w=25.0e-6
l=1.0e-6
}
C {sg13g2_pr/ntap1.sym} 830 -610 2 0 {name=R4
model=ntap1
spiceprefix=X
w=10.0e-6
l=1.0e-6
}
