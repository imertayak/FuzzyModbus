FuzzyModbus v0.4
=====================
ModbusTCP Fuzzing and DoS Tool.(Python 3)

Install and Usage:
-------------
$> git clone https://github.com/imertayak/FuzzyModbus.git && cd FuzzyModbus

$> pip install -r requirements.txt

$> chmod +x FuzzyModbus.py

$> ./FuzzyModbus.py [OPTIONS]

### Command line options:

```
-h or --help	Help Menu

-f or --func-code <Code> Modbus Function Code

-F or --flood	OPTIONAL Modbus Flood/DoS Attack

-t or --target <IP_Addr>	Target Modbus Server IP Address

-p or --port <Port>	DEFAULT=502 Target Modbus Server Port

-u or --uid <UID>	DEFAULT=1 Unit ID

-a or --address <Reg_Addr>	DEFAULT=0 First Register Address

-c or --count <Count>	DEFAULT=1 Count of Registers to read/write

-i or --input <value> DEFAULT_BIT=0/DEFAULT_REG=666 Input Value to write

```

### Supported Function Codes

```
Read Coils			Func. Code = 1

Read Discrete Inputs		Func. Code = 2

Read Holding Registes		Func. Code = 3

Read Input Registers		Func. Code = 4

Write Single Coil		Func. Code = 5

Write Single Register		Func. Code = 6

Write Multiple Coils		Func. Code = 15

Write Multiple Registers	Func. Code = 16

```
