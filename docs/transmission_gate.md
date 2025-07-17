# transmission_gate

- Description: A simple HV transmission gate
- PDK: ihp-sg13g2

## Authorship

- Designer: IHP-Authors
- Company: IHP
- Created: None
- License: Apache 2.0
- Last modified: None

## Pins

- VDD
  + Description: Positive analog power supply
  + Type: power
  + Direction: inout
  + Vmin: 2.9
  + Vmax: 3.3
- VSS
  + Description: Analog ground
  + Type: ground
  + Direction: inout

## Default Conditions

- vdd
  + Description: Analog power supply voltage
  + Display: Vdd
  + Unit: V
  + Typical: 3.0
- vin
  + Description: Input voltage
  + Display: Vin
  + Unit: V
  + Typical: 1.6
- Vp
  + Description: Input voltage
  + Display: Vin
  + Unit: V
  + Typical: 2.9
- Vn
  + Description: Input voltage
  + Display: Vin
  + Unit: V
  + Typical: 0.0
- m1_w
  + Description: N transistor width
  + Display: m1_w
  + Typical: 4e-05
- m2_w
  + Description: P transistor width
  + Display: m2_w
  + Typical: 4e-05
- corner
  + Description: Process corner
  + Display: Corner
  + Typical: tt
- temperature
  + Description: Ambient temperature
  + Display: Temp
  + Unit: °C
  + Typical: 27

## Symbol

![Symbol of transmission_gate](transmission_gate_symbol.svg)

## Schematic

![Schematic of transmission_gate](transmission_gate_schematic.svg)
