v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 750 -280 840 -280 {lab=#net4}
N 750 -400 840 -400 {lab=#net5}
N 750 -540 840 -540 {lab=#net6}
N 450 -650 450 -630 {lab=#net7}
N 450 -650 490 -650 {lab=#net7}
N 490 -720 490 -650 {lab=#net7}
N 610 -650 610 -630 {lab=#net8}
N 610 -650 650 -650 {lab=#net8}
N 750 -650 750 -630 {lab=#net9}
N 750 -650 790 -650 {lab=#net9}
N 450 -570 450 -540 {lab=#net6}
N 340 -540 450 -540 {lab=#net6}
N 610 -570 610 -540 {lab=#net6}
N 450 -540 610 -540 {lab=#net6}
N 750 -570 750 -540 {lab=#net6}
N 610 -540 750 -540 {lab=#net6}
N 450 -510 450 -490 {lab=#net7}
N 450 -510 490 -510 {lab=#net7}
N 490 -650 490 -510 {lab=#net7}
N 450 -380 450 -360 {lab=#net7}
N 450 -380 490 -380 {lab=#net7}
N 450 -300 450 -280 {lab=#net4}
N 340 -280 450 -280 {lab=#net4}
N 610 -300 610 -280 {lab=#net4}
N 450 -280 610 -280 {lab=#net4}
N 750 -300 750 -280 {lab=#net4}
N 610 -280 750 -280 {lab=#net4}
N 750 -430 750 -400 {lab=#net5}
N 610 -400 750 -400 {lab=#net5}
N 610 -430 610 -400 {lab=#net5}
N 450 -400 610 -400 {lab=#net5}
N 450 -430 450 -400 {lab=#net5}
N 340 -400 450 -400 {lab=#net5}
N 750 -380 750 -360 {lab=#net9}
N 750 -380 790 -380 {lab=#net9}
N 790 -510 790 -380 {lab=#net9}
N 610 -380 610 -360 {lab=#net8}
N 610 -380 650 -380 {lab=#net8}
N 650 -510 650 -380 {lab=#net8}
N 610 -510 610 -490 {lab=#net8}
N 610 -510 650 -510 {lab=#net8}
N 650 -650 650 -510 {lab=#net8}
N 750 -510 750 -490 {lab=#net9}
N 750 -510 790 -510 {lab=#net9}
N 790 -650 790 -510 {lab=#net9}
N 380 -330 430 -330 {lab=#net10}
N 550 -330 590 -330 {lab=#net10}
N 690 -330 730 -330 {lab=#net10}
N 690 -330 690 -180 {lab=#net10}
N 690 -600 730 -600 {lab=#net10}
N 690 -460 690 -330 {lab=#net10}
N 690 -460 730 -460 {lab=#net10}
N 690 -600 690 -460 {lab=#net10}
N 550 -600 590 -600 {lab=#net10}
N 550 -330 550 -180 {lab=#net10}
N 550 -460 550 -330 {lab=#net10}
N 550 -460 590 -460 {lab=#net10}
N 550 -600 550 -460 {lab=#net10}
N 380 -600 430 -600 {lab=#net10}
N 380 -330 380 -180 {lab=#net10}
N 380 -460 430 -460 {lab=#net10}
N 380 -460 380 -330 {lab=#net10}
N 380 -600 380 -460 {lab=#net10}
N 550 -180 690 -180 {lab=#net10}
N 380 -180 550 -180 {lab=#net10}
N 260 -180 380 -180 {lab=#net10}
N 790 -710 790 -650 {lab=#net9}
N 650 -720 650 -650 {lab=#net8}
N 790 -380 790 -260 {lab=#net9}
N 650 -380 650 -260 {lab=#net8}
N 490 -380 490 -260 {lab=#net7}
N 490 -510 490 -380 {lab=#net7}
N 1150 -490 1150 -470 {lab=#net11}
N 1100 -400 1150 -400 {lab=#net12}
N 1150 -410 1150 -400 {lab=#net12}
N 1150 -340 1150 -310 {lab=#net13}
C {devices/title.sym} 200 -60 0 0 {name=l5 author="Copyright 2023 IHP PDK Authors"}
C {res3.sym} 450 -600 0 0 {name=R2
R=1
W=1
L=1
model=rpoly
spiceprefix=X
m=1}
C {res3.sym} 450 -460 0 0 {name=R3
R=1
W=1
L=1
model=rpoly
spiceprefix=X
m=1}
C {res3.sym} 450 -330 0 0 {name=R4
R=1
W=1
L=1
model=rpoly
spiceprefix=X
m=1}
C {res3.sym} 610 -600 0 0 {name=R5
R=1
W=1
L=1
model=rpoly
spiceprefix=X
m=1}
C {res3.sym} 610 -460 0 0 {name=R6
R=1
W=1
L=1
model=rpoly
spiceprefix=X
m=1}
C {res3.sym} 610 -330 0 0 {name=R7
R=1
W=1
L=1
model=rpoly
spiceprefix=X
m=1}
C {res3.sym} 750 -600 0 0 {name=R8
R=1
W=1
L=1
model=rpoly
spiceprefix=X
m=1}
C {res3.sym} 750 -460 0 0 {name=R9
R=1
W=1
L=1
model=rpoly
spiceprefix=X
m=1}
C {res3.sym} 750 -330 0 0 {name=R10
R=1
W=1
L=1
model=rpoly
spiceprefix=X
m=1}
C {switch.sym} 490 -750 0 0 {name=G1 TABLE="1.0 1G 2.0 10"}
C {switch.sym} 650 -750 0 0 {name=G2 TABLE="1.0 1G 2.0 10"}
C {switch.sym} 790 -740 0 0 {name=G3 TABLE="1.0 1G 2.0 10"}
C {switch.sym} 490 -230 0 0 {name=G4 TABLE="1.0 1G 2.0 10"}
C {switch.sym} 650 -230 0 0 {name=G5 TABLE="1.0 1G 2.0 10"}
C {switch.sym} 790 -230 0 0 {name=G6 TABLE="1.0 1G 2.0 10"}
C {switch.sym} 310 -280 1 0 {name=G7 TABLE="1.0 1G 2.0 10"}
C {switch.sym} 310 -400 1 0 {name=G8 TABLE="1.0 1G 2.0 10"}
C {switch.sym} 310 -540 1 0 {name=G9 TABLE="1.0 1G 2.0 10"}
C {switch.sym} 870 -280 1 0 {name=G10 TABLE="1.0 1G 2.0 10"}
C {switch.sym} 870 -400 1 0 {name=G11 TABLE="1.0 1G 2.0 10"}
C {switch.sym} 870 -540 1 0 {name=G12 TABLE="1.0 1G 2.0 10"}
C {res3.sym} 1030 -400 0 0 {name=R14
R=1
W=1
L=1
model=rpoly
spiceprefix=X
m=1}
C {res.sym} 1150 -440 0 0 {name=R15
value=1k
footprint=1206
device=resistor
m=1}
C {res.sym} 1150 -370 0 0 {name=R16
value=1k
footprint=1206
device=resistor
m=1}
