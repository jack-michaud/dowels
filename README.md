# Acoustic Dampening Panel Project

## Description
This project involves creating an acoustic dampening panel that utilizes random lengths of square dowels to create varied reflections, thus dissipating sound energy effectively. The panel is designed to operate within the frequency range of 500-20000 Hz and measures 10x10 cm.

## Current Status
An optimal solution has been found for cutting dowels using a mixed-integer programming (MIP) approach, which minimizes material waste and maximizes the use of available resources. As of the latest update, an optimal solution requires 15 dowels for 1000-20000 Hz and 30 dowels for 500-20000 Hz.

## Installation

To run the optimization script, you need to have Python installed, along with Google's OR-Tools library. Use the following command to install OR-Tools via pip:

```
pip install ortools
```

## Usage

Execute the script to determine the optimal distribution of dowel cuts for the acoustic panel. The script includes constraints such as the kerf from cutting the dowels using a Japanese pull saw and the maximum dowel capacity. It outputs the number and length of cuts for each dowel. Run the script using:

```
python main.py
```

## Contributing

We welcome contributions to improve the algorithm further or adapt the script to different conditions or requirements. Feel free to fork the project, make changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```

