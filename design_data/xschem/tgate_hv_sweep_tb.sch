v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
T {used to run ngspice sweep in parallel} 1250 -1130 0 0 0.3 0.3 {layer=11}
T {used to check OP, AC and TRAN} 690 -1140 0 0 0.3 0.3 {layer=11}
T {Ctrl-Click to execute launcher} 40 -1100 0 0 0.3 0.3 {layer=11}
T {.save file can be created with IHP->"Create FET and BIP .save file"} 40 -1000 0 0 0.3 0.3 {layer=11}
T {each printed value will be saved in csv file} 1610 -670 0 0 0.3 0.3 {layer=11}
T {possible parameter sweep types:
Auto:Begin:TotalPoints:End
Lin:Begin:StepSize:End
Dec:Begin:PointsPerDecade:End
Log:Begin:TotalPoints:End} 1590 -430 0 0 0.3 0.3 {layer=11}
T {set num_threads to 1 for small circuits} 1520 -890 0 0 0.3 0.3 {layer=11}
N 30 -350 30 -330 {
lab=GND}
N 120 -350 120 -330 {
lab=GND}
N 260 -210 260 -200 {
lab=GND}
N 30 -450 30 -410 {
lab=Vdd}
N 260 -290 260 -270 {
lab=V_in}
N 120 -420 120 -410 {
lab=en_p}
N 40 -170 40 -150 {
lab=GND}
N 40 -240 40 -230 {
lab=en_n}
N 380 -300 420 -300 {
lab=V_in}
N 380 -270 420 -270 {
lab=en_n}
N 380 -250 420 -250 {
lab=en_p}
N 820 -300 820 -280 {
lab=V_out1}
N 570 -420 570 -410 {
lab=Vdd}
N 570 -350 570 -340 {
lab=#net1}
N 570 -220 570 -210 {
lab=GND}
N 720 -300 740 -300 {lab=#net2}
N 800 -300 820 -300 {lab=V_out1}
N 820 -330 820 -300 {
lab=V_out1}
C {devices/title.sym} 245 -55 0 0 {name=l5 author="Patrick Fath"}
C {launcher.sym} 100 -1055 0 0 {name=h3
descr=SimulateNGSPICE
tclcommand="
# Setup the default simulation commands if not already set up
# for example by already launched simulations.
set_sim_defaults
puts $sim(spice,1,cmd) 

# Change the Xyce command. In the spice category there are currently
# 5 commands (0, 1, 2, 3, 4). Command 3 is the Xyce batch
# you can get the number by querying $sim(spice,n)
set sim(spice,1,cmd) \{ngspice  \\"$N\\" -a\}

# change the simulator to be used (Xyce)
set sim(spice,default) 0

# Create FET and BIP .save file
mkdir -p $netlist_dir
write_data [save_params] $netlist_dir/[file rootname [file tail [xschem get current_name]]].save

# run netlist and simulation
xschem netlist
simulate
"}
C {code_shown.sym} 25 -885 0 0 {
name=TT_MODELS
only_toplevel=true
value="
** IHP models
.lib cornerMOSlv.lib mos_tt
.lib cornerMOShv.lib mos_tt
.lib cornerHBT.lib hbt_typ
.lib cornerRES.lib res_typ
.lib cornerCAP.lib cap_typ
"
spice_ignore=false
      }
C {simulator_commands_shown.sym} 685 -1055 0 0 {name=OP_AC_TRAN
simulator=ngspice
only_toplevel=false 
value="
.param temp=27
.param c1_val=1p
.param r1_val=100Meg
.param m1_w_val=0.15u
.param m2_w_val=0.15u
.param l_val=0.13u
.include inv_sweep_tb.save
.options warn=1

.control
set num_threads=1
save all
op
write inv_sweep_tb.raw
set appendwrite
ac dec 1001 1 100G
write inv_sweep_tb.raw
let gain_lin = abs(inv_out)
let gain_dB = vdb(inv_out)
meas ac gain_passband_dB max gain_dB
let gain_fc_dB = gain_passband_dB-3
meas ac fc_l when gain_dB = gain_fc_dB
meas ac fc_u when gain_dB = gain_fc_dB cross=last
let GBW = gain_lin[0] * (fc_u-fc_l)
print gain_passband_dB
print fc_l
print fc_u
print GBW
plot gain_dB xlimit 1 100G ylabel 'small signal gain'
tran 10p 30n
write inv_sweep_tb.raw
plot inv_in inv_out
.endc
"
spice_ignore=true}
C {simulator_commands_shown.sym} 1245 -1045 0 0 {name=SWEEP_SIM
simulator=ngspice
only_toplevel=false 
value="
.param temp=27
.param m1_w=25.0u
.param m2_w=20.0u

.param temp=27
.param Iload=500u
.control
save all 

set num_threads 1
dc I0 -5m 5m 1.1u
let Ron=(V(V_in)-V(V_out1))/I(Vp2)
meas dc Ronmax max Ron
echo results_sweep_begin
print Ronmax
echo results_sweep_end
set color0=white
set color1=black
set color2=red
set color3=blue
set color4=green
plot Ron title 'RON resistance' xlabel 'current' ylabel 'Ron'
.endc
"
}
C {devices/launcher.sym} 100 -1020 0 0 {name=h1
descr="OP annotate" 
tclcommand="xschem annotate_op"
}
C {code_shown.sym} 1260 -490 0 0 {name=SWEEP_SETTINGS
only_toplevel=false
value="
**nr_workers=50
**sort_results_index=0

**parameter_sweep_begin
**m1_w=Auto:1.0u:40:40u
**m2_w=Auto:1.0u:40:40u
**parameter_sweep_end

**results_plot_begin
**Ronmax
**results_plot_end
"
}
C {launcher.sym} 1310 -195 0 0 {name=h2
descr=SimulatePARALLEL
tclcommand="
# Setup the default simulation commands if not already set up
# for example by already launched simulations.
set_sim_defaults
puts $sim(spice,1,cmd) 

# Change the Xyce command. In the spice category there are currently
# 5 commands (0, 1, 2, 3, 4). Command 3 is the Xyce batch
# you can get the number by querying $sim(spice,n)
set sim(spice,1,cmd) \{ngspice  \\"$N\\" -a\}

# change the simulator to be used (Xyce)
set sim(spice,default) 0

# Create FET and BIP .save file
mkdir -p $netlist_dir
write_data [save_params] $netlist_dir/[file rootname [file tail [xschem get current_name]]].save

# run netlist and simulation
xschem netlist
python3 $\{PDK_ROOT\}/$\{PDK\}/libs.tech/xschem/sg13g2_tests/ngspice_parallel_sweep.py [file tail [xschem get current_name]]
"}
C {devices/vsource.sym} 30 -380 0 0 {name=Vpow value=3.3}
C {devices/gnd.sym} 570 -210 0 0 {name=l6 lab=GND}
C {devices/ammeter.sym} 570 -380 0 0 {name=Vp}
C {devices/gnd.sym} 30 -330 0 0 {name=l7 lab=GND}
C {devices/vsource.sym} 260 -240 0 0 {name=Vin value=0.1}
C {devices/vsource.sym} 120 -380 0 0 {name=Ven value=3.3}
C {devices/gnd.sym} 120 -330 0 0 {name=l8 lab=GND}
C {devices/gnd.sym} 260 -200 0 0 {name=l9 lab=GND}
C {devices/lab_pin.sym} 260 -290 1 0 {name=p6 sig_type=std_logic lab=V_in}
C {devices/lab_pin.sym} 120 -420 1 0 {name=p7 sig_type=std_logic lab=en_p}
C {devices/lab_pin.sym} 820 -330 1 0 {name=p8 sig_type=std_logic lab=V_out1}
C {devices/lab_pin.sym} 30 -450 1 0 {name=p9 sig_type=std_logic lab=Vdd}
C {devices/vsource.sym} 40 -200 0 0 {name=Ven1 value=0}
C {devices/gnd.sym} 40 -150 0 0 {name=l10 lab=GND}
C {devices/lab_pin.sym} 40 -240 1 0 {name=p10 sig_type=std_logic lab=en_n}
C {devices/lab_pin.sym} 570 -420 1 0 {name=p11 sig_type=std_logic lab=Vdd}
C {devices/lab_pin.sym} 380 -300 0 0 {name=p12 sig_type=std_logic lab=V_in}
C {devices/lab_pin.sym} 380 -250 0 0 {name=p13 sig_type=std_logic lab=en_p}
C {devices/lab_pin.sym} 380 -270 0 0 {name=p14 sig_type=std_logic lab=en_n}
C {devices/isource.sym} 820 -250 0 0 {name=I0 value=\{Iload\}}
C {devices/gnd.sym} 820 -160 0 0 {name=l11 lab=GND}
C {devices/ammeter.sym} 770 -300 3 0 {name=Vp2}
C {devices/vsource.sym} 820 -190 0 0 {name=Vin1 value=0.1}
C {transmission_gate_hv.sym} 570 -280 0 0 {name=x1}
