
def process_symbol_dut(Dmax, GSmax, output_filename="../xschem/DUTg.sym"):
    with open(output_filename, "w") as f:
        # Static header
        f.write("v {xschem version=3.4.6 file_version=1.2}\n")
        f.write("G {}\nK {type=subcircuit\nformat=\"@name @pinlist @symname\"\ntemplate=\"name=x1\"\n}\n")
        f.write("V {}\nS {}\nE {}\n")

        # Lines
        lines = [
            "L 7 10 -10 10 0 {}",
            "L 7 120 -10 120 0 {}",
            "L 7 -10 50 0 50 {}",
            "L 7 40 -10 40 0 {}",
            "L 7 -10 30 0 30 {}",
            "L 7 -10 130 0 130 {}",
            "L 7 -10 110 0 110 {}"
        ]
        for line in lines:
            f.write(line + "\n")

        # Base pins
        f.write("B 5 7.5 -12.5 12.5 -7.5 {name=B dir=inout}\n")

        # Df loop
        for n in range(2, Dmax + 1):
            x1 = 40 + (n-1) * 80 - 2.5
            x2 = 40 + (n-1) * 80 + 2.5
            f.write(f"B 5 {x1} -12.5 {x2} -7.5 {{name=D{n} dir=inout}}\n")

        # D1, G1, S1
        f.write("B 5 37.5 -12.5 42.5 -7.5 {name=D1 dir=inout}\n")
        f.write("B 5 -12.5 27.5 -7.5 32.5 {name=G1 dir=inout}\n")
        f.write("B 5 -12.5 47.5 -7.5 52.5 {name=S1 dir=inout}\n")

        # G', S2 loop
        for m in range(1, GSmax + 1):
            yG = 30 + 80 * m
            yS = 50 + 80 * m
            f.write(f"B 5 -12.5 {yG - 2.5} -7.5 {yG + 2.5} {{name=Gf'{m} dir=inout}}\n")
            f.write(f"B 5 -12.5 {yS - 2.5} -7.5 {yS + 2.5} {{name=Sf'{m} dir=inout}}\n")

        # Polygon
        px = 60 + 80 * (Dmax + 1)
        py = 60 + 80 * (GSmax + 1)
        f.write(f"P 4 5 0 0 {px} 0 {px} {py} 0 {py} 0 0 {{}}\n")

        # Texts
        f.write("T {@symname} 68.5 74 0 0 0.3 0.3 {}\n")
        f.write("T {@name} 165 -2 0 0 0.2 0.2 {}\n")
        f.write("T {B} 5 16 2 1 0.2 0.2 {}\n")

        # Df' labels
        for n in range(2, Dmax + 1):
            x = 45 + (n-1) * 80
            f.write(f"T {{D{n}}} {x} 25 1 1 0.2 0.2 {{}}\n")

        # Static labels
        f.write("T {D1} 45 25 1 1 0.2 0.2 {}\n")
        f.write("T {G1} 15 26 0 1 0.2 0.2 {}\n")
        f.write("T {S1} 15 46 0 1 0.2 0.2 {}\n")

        # G2 and S2 labels loop
        for m in range(2, GSmax + 1):
            yG = 30 + 80 * (m-1) - 4
            yS = 50 + 80 * (m-1) - 4
            f.write(f"T {{G{m}}} 15 {yG} 0 1 0.2 0.2 {{}}\n")
            f.write(f"T {{S{m}}} 15 {yS} 0 1 0.2 0.2 {{}}\n")

    print(f"Symbol file written to {output_filename}")
