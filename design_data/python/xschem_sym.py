import yaml


def read_config():
    try:
        with open("config.yaml", "r") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print("Configuration file 'config.yaml' not found.")
        return None

def process_symbol_dut():

    config = read_config()
    output_filename = config["xschem_dir"]+config["dut_symname"]
    Dmax  = config["DUT"]["block_size"]
    GSmax = config["DUT"]["block_size"]
    with open(output_filename, "w") as f:
        # Static header
        f.write("v {xschem version=3.4.6 file_version=1.2}\n")
        f.write("G {}\nK {type=subcircuit\nformat=\"@name @pinlist @symname\"\ntemplate=\"name=x1\"\n}\n")
        f.write("V {}\nS {}\nE {}\n")

        # Polygon
        px =  80 * (Dmax)
        py =  80 * (GSmax)
        f.write(f"P 4 5 0 0 {px} 0 {px} {py} 0 {py} 0 0 {{}}\n")
        # Static content
        f.write(f"T {{@symname}} {px/2} {py/2} 0 0 0.3 0.3 {{}}\n")
        f.write(f"T {{@name}} {px+10} -2 0 0 0.2 0.2 {{}}\n")
        f.write("T {B} 5 16 2 1 0.2 0.2 {}\n")
        f.write("L 7 10 -10 10 0 {}\n")
        f.write("B 5 7.5 -12.5 12.5 -7.5 {name=B dir=inout}\n")

        # D loop
        for n in range(1, Dmax + 1):
            x = 40 + (n-1) * 80 
            f.write(f"B 5 {x-2.5} -12.5 {x+2.5} -7.5 {{name=D{n} dir=inout}}\n")
            f.write(f"T {{D{n}}} {x+5} 25 1 1 0.15 0.15 {{}}\n")
            f.write(f"L 7 {x} 0 {x} -10 {{}}\n")

        # G2 and S2 labels loop
        for m in range(1, GSmax + 1):
            yG = 30 + 80*(m-1) 
            yS = 50 + 80*(m-1)
            f.write(f"T {{G{m}}} 30 {yG-4} 0 1 0.15 0.15 {{}}\n")
            f.write(f"T {{S{m}}} 30 {yS-4} 0 1 0.15 0.15 {{}}\n")
            f.write(f"B 5 -12.5 {yG - 2.5} -7.5 {yG + 2.5} {{name=G{m} dir=inout}}\n")
            f.write(f"B 5 -12.5 {yS - 2.5} -7.5 {yS + 2.5} {{name=S{m} dir=inout}}\n")
            f.write(f"L 7 -10 {yG} 0 {yG} {{}}\n")
            f.write(f"L 7 -10 {yS} 0 {yS} {{}}\n")

    print(f"Symbol file written to {output_filename}")

def process_schematic_dut():

    config = read_config()
    output_filename = config["xschem_dir"]+config["dut_schname"]
    Dmax  = config["DUT"]["block_size"]
    GSmax = config["DUT"]["block_size"]
    W = config["DUT"]["W"]
    L = config["DUT"]["L"]
    w = W[0]
    l = L[0]
    tap_w = config["DUT"]["w_tap"]
    tap_l = config["DUT"]["l_tap"]
    with open(output_filename, "w") as f:
        # Static heade 
        f.write("v {xschem version=3.4.6 file_version=1.2}\n")
        f.write("G {}\nK {}\nV {}\nS {}\nE {}\n")
        f.write(f"C {{devices/iopin.sym}} 0 0 2 0  {{name=p9 lab=B}}\n")

        cnt=0
        # horizontal loop fro polygons
        for n in range(1, Dmax + 1):
            xpos =  n * 200
            f.write(f"C {{devices/iopin.sym}} {100+xpos-200} 0 1 1  {{name=p6{n} lab=D{n}}}\n")
            for m in range(1, GSmax + 1):
                ypos =  m * 200
                cnt += 1
                f.write(f"P 4 5 {xpos-200} {ypos-200} {xpos} {ypos-200} {xpos} {ypos} {xpos-200} {ypos} {xpos-200} {ypos-200} {{}}\n")
                f.write(f"N {170+xpos-200} {70+ypos-200} {170+xpos-200} {110+ypos-200} {{lab=B}}\n")
                f.write(f"N {170+xpos-200} {170+ypos-200} {170+xpos-200} {190+ypos-200} {{lab=B}}\n")
                f.write(f"N {90+xpos-200} {100+ypos-200} {90+xpos-200} {140+ypos-200} {{lab=S{m}}}\n")
                f.write(f"N {10+xpos-200} {70+ypos-200} {50+xpos-200} {70+ypos-200} {{lab=G{m}}}\n")
                f.write(f"N {90+xpos-200} {20+ypos-200} {90+xpos-200} {40+ypos-200} {{lab=D{n}}}\n")
                f.write(f"N {10+xpos-200} {20+ypos-200} {90+xpos-200} {20+ypos-200} {{lab=D{n}}}\n")
                f.write(f"N {10+xpos-200} {190+ypos-200} {170+xpos-200} {190+ypos-200} {{lab=B}}\n")
                f.write(f"N {10+xpos-200} {140+ypos-200} {90+xpos-200} {140+ypos-200} {{lab=S{m}}}\n")
                f.write(f"N {10+xpos-200} {10+ypos-200} {10+xpos-200} {20+ypos-200} {{lab=D{n}}}\n")
                f.write(f"N {10+xpos-200} {60+ypos-200} {10+xpos-200} {70+ypos-200} {{lab=G{m}}}\n")
                f.write(f"N {10+xpos-200} {130+ypos-200} {10+xpos-200} {140+ypos-200} {{lab=S{m}}}\n")
                f.write(f"N {10+xpos-200} {180+ypos-200} {10+xpos-200} {190+ypos-200} {{lab=B}}\n")
                f.write(f"N {170+xpos-200} {60+ypos-200} {170+xpos-200} {70+ypos-200} {{lab=B}}\n")
                f.write(f"N {90+xpos-200} {70+ypos-200} {170+xpos-200} {70+ypos-200} {{lab=B}}\n")
                f.write(f"C {{lab_pin.sym}} {10+xpos-200} {15+ypos-200} 2 0  {{name=p1{cnt} sig_type=std_logic lab=D{n}}}\n")
                f.write(f"C {{lab_pin.sym}} {10+xpos-200} {60+ypos-200} 2 0  {{name=p2{cnt} sig_type=std_logic lab=G{m}}}\n")
                f.write(f"C {{lab_pin.sym}} {10+xpos-200} {130+ypos-200} 2 0  {{name=p3{cnt} sig_type=std_logic lab=S{m}}}\n")
                f.write(f"C {{lab_pin.sym}} {10+xpos-200} {180+ypos-200} 2 0  {{name=p4{cnt} sig_type=std_logic lab=B}}\n")
                f.write(f"C {{lab_pin.sym}} {170+xpos-200} {60+ypos-200} 1 2  {{name=p5{cnt} sig_type=std_logic lab=sub!}}\n")
                f.write(f"C {{sg13g2_pr/ptap1.sym}} {170+xpos-200} {140+ypos-200} 2 0 {{name=R{cnt} \nmodel=ptap1\nspiceprefix=X\n w={tap_w}\nl={tap_l}}}\n")
                f.write(f"C {{sg13g2_pr/sg13_lv_nmos.sym}} {70+xpos-200} {70+ypos-200} 0 0 {{name=M{cnt} \nmodel=sg13_lv_nmos\nspiceprefix=X\n w={w}\nl={l}\nng=1\nm=1}}\n")
                
        for m in range(1, GSmax + 1):
            ypos = m*200
            f.write(f"C {{devices/iopin.sym}} 0 {70+ypos-200} 2 0  {{name=p7{m} lab=G{m}}}\n")
            f.write(f"C {{devices/iopin.sym}} 0 {140+ypos-200} 2 0  {{name=p8{m} lab=S{m}}}\n")

    print(f"Schematic file written to {output_filename}")

def print_config():
    config = read_config()
    if config:
        print("Configuration:")
        print(config["DUT"]["Lmax"])
        for key, value in config.items():
            print(f"{key}: {value}")
    else:
        print("No configuration available.")
