# Decoder

To implement the decoder we use [LibreLane](https://github.com/librelane/librelane).

## Prerequisites

1. Install Nix according to the LibreLane docs: https://librelane.readthedocs.io/en/latest/getting_started/common/nix_installation/index.html
2. Install the latest PDK for ihp-sg13g2 using ciel: https://github.com/fossi-foundation/ciel
3. Use the `ihp` branch of LibreLane: https://github.com/librelane/librelane/tree/ihp

## Implementation

Enable an environment with the `ihp` branch of LibreLane and run:

```
$ make
```

This will run the `decoder` Makefile target to build the decoder, and the `copy-final` target to copy the final directory of the latest run into the main folder.

To view the latest run using the OpenROAD GUI, run:

```
$ make view
```
