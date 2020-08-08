#! /usr/bin/python3
# written by m3rt (v0.1 17.10.2018)

import sys
import os
import time
from getopt import *
from pyModbusTCP.client import *
from subprocess import call

def clear():
    _ = call('clear' if os.name =='posix' else 'cls')

def readCoils(rq_type,client,bit_addr,bit_nb):

    client.open()
    print("!! Function Code 1 Read Coils executed !!")

    if rq_type == "single":
        rq = client.read_coils(int(bit_addr),int(bit_nb))
        for i,j in enumerate(rq):
            print("["+str(int(bit_addr)+i)+": "+str(j)+"] ", end="")
        client.close()
        exit(0)

    elif rq_type == "flood":
        while True:
            rq = client.read_coils(int(bit_addr),int(bit_nb))
            for i,j in enumerate(rq):
                if i == len(rq) - 1:
                    print("["+str(int(bit_addr)+i)+": "+str(j)+"] ", end="\n")
                else:
                    print("["+str(int(bit_addr)+i)+": "+str(j)+"] ", end=" ")
            #clear()
        client.close()
        exit(0)

    else:
        print ("Wrong Request Type")
        client.close()
        exit(1)

def readDiscreteInputs(rq_type,client,bit_addr,bit_nb):

    client.open()
    print ("!! Function Code 2 Read Discrete Inputs executed !!")
    if rq_type == "single":
        rq = client.read_discrete_inputs(int(bit_addr),int(bit_nb))
        for i,j in enumerate(rq):
            print("["+str(int(bit_addr)+i)+": "+str(j)+"] ", end="")
        client.close()
        exit(0)

    elif rq_type == "flood":
        while True:
            rq = client.read_discrete_inputs(int(bit_addr),int(bit_nb))
            for i,j in enumerate(rq):
                if i == len(rq) - 1:
                    print("["+str(int(bit_addr)+i)+": "+str(j)+"] ", end="\n")
                else:
                    print("["+str(int(bit_addr)+i)+": "+str(j)+"] ", end=" ")
        client.close()
        exit(0)

    else:
        print ("Wrong Request Type")
        client.close()
        exit(1)

def readHoldingRegisters(rq_type,client,reg_addr,reg_nb):

    client.open()
    print ("!! Function Code 3 Read Holding Registers executed !!")
    if rq_type == "single":
        rq = client.read_holding_registers(int(reg_addr),int(reg_nb))
        for i,j in enumerate(rq):
            print("["+str(int(reg_addr)+i)+": "+str(j)+"] ", end="")
        client.close()
        exit(0)

    elif rq_type == "flood":
        while True:
            rq = client.read_holding_registers(int(reg_addr),int(reg_nb))
            for i,j in enumerate(rq):
                if i == len(rq) - 1:
                    print("["+str(int(reg_addr)+i)+": "+str(j)+"] ", end="\n")
                else:
                    print("["+str(int(reg_addr)+i)+": "+str(j)+"] ", end=" ")
        client.close()
        exit(0)

    else:
        print ("Wrong Request Type")
        client.close()
        exit(1)

def readInputRegisters(rq_type,client,reg_addr,reg_nb):

    client.open()
    print ("!! Function Code 4 Read Input Registers executed !!")
    if rq_type == "single":
        rq = client.read_input_registers(int(reg_addr),int(reg_nb))
        for i,j in enumerate(rq):
            print("["+str(int(reg_addr)+i)+": "+str(j)+"] ", end="")
        client.close()
        exit(0)

    elif rq_type == "flood":
        while True:
            rq = client.read_input_registers(int(reg_addr),int(reg_nb))
            for i,j in enumerate(rq):
                if i == len(rq) - 1:
                    print("["+str(int(reg_addr)+i)+": "+str(j)+"] ", end="\n")
                else:
                    print("["+str(int(reg_addr)+i)+": "+str(j)+"] ", end=" ")
        client.close()
        exit(0)

    else:
        print ("Wrong Request Type")
        client.close()
        exit(1)

def writeSingleCoil(rq_type,client,bit_addr,input_bit):

    client.open()
    print ("!! Function Code 5 Write Single Coil executed !!")
    if rq_type == "single":
        rq = client.write_single_coil(int(bit_addr),int(input_bit))
        print(rq)
        client.close()
        exit(0)

    elif rq_type == "flood":
        while True:
            rq = client.write_single_coil(int(bit_addr),int(input_bit))
            print(rq)
        client.close()
        exit(0)

    else:
        print ("Wrong Request Type")
        client.close()
        exit(1)

def writeSingleRegister(rq_type,client,reg_addr,input_reg):

    client.open()
    print ("!! Function Code 6 Write Single Register executed !!")
    if rq_type == "single":
        rq = client.write_single_register(int(reg_addr),int(input_reg))
        print(rq)
        client.close()
        exit(0)

    elif rq_type == "flood":
        while True:
            rq = client.write_single_register(int(reg_addr),int(input_reg))
            print(rq)
        client.close()
        exit(0)

    else:
        print ("Wrong Request Type")
        client.close()
        exit(1)

def writeMultipleCoils(rq_type,client,bit_addr,bit_nb,input_bit):

    client.open()
    values = [int(input_bit)]*int(bit_nb)
    print ("!! Function Code 15 Write Multiple Coils executed !!")
    if rq_type == "single":
        rq = client.write_multiple_coils(int(bit_addr),values)
        print(rq)
        client.close()
        exit(0)

    elif rq_type == "flood":
        while True:
            rq = client.write_multiple_coils(int(bit_addr),values)
            print(rq)
        client.close()
        exit(0)

    else:
        print ("Wrong Request Type")
        client.close()
        exit(1)

def writeMultipleRegisters(rq_type,client,reg_addr,reg_nb,input_reg):

    client.open()
    values = [int(input_reg)]*int(reg_nb)
    print ("!! Function Code 16 Write Multiple Registers executed !!")
    if rq_type == "single":
        rq = client.write_multiple_registers(int(reg_addr),values)
        print(rq)
        client.close()
        exit(0)

    elif rq_type == "flood":
        while True:
            rq = client.write_multiple_registers(int(reg_addr),values)
            print(rq)
        client.close()
        exit(0)

    else:
        print ("Wrong Request Type")
        client.close()
        exit(1)

def usageExit():
    print ('FuzzyModbus v0.4')
    print ('ModbusTCP Fuzzing Tool by m3rt Github: @imertayak\n')
    print ('-h or --help\tHelp Menu')
    print ('-f or --func-code <Code>\tModbus Function Code')
    print ('-F or --flood\tOPTIONAL Modbus Flood/DoS Attack')
    print ('-t or --target <IP_Addr>\tTarget Modbus Server IP Address')
    print ('-p or --port <Port>\tDEFAULT=502 Target Modbus Server Port')
    print ('-u or --uid <UID>\tDEFAULT=1 Unit ID')
    print ('-a or --address <Reg_Addr>\tDEFAULT=0 First Register Address')
    print ('-c or --count <Count>\tDEFAULT=1 Count of Registers to read/write')
    print ('-i or --input <value>\tDEFAULT_BIT=0/DEFAULT_REG=666 Input Value to write')
    print ('\nSupported Function Codes:')
    print ('\tRead Coils\t\t\tFunc. Code = 1')
    print ('\tRead Discrete Inputs\t\tFunc. Code = 2')
    print ('\tRead Holding Registes\t\tFunc. Code = 3')
    print ('\tRead Input Registers\t\tFunc. Code = 4')
    print ('\tWrite Single Coil\t\tFunc. Code = 5')
    print ('\tWrite Single Register\t\tFunc. Code = 6')
    print ('\tWrite Multiple Coils\t\tFunc. Code = 15')
    print ('\tWrite Multiple Registers\tFunc. Code = 16')
    sys.exit(1)

def main():

    try:
        opts, args = getopt(sys.argv[1:], 'hf:Ft:p:u:a:c:i:', ['help','func-code=','target=','port=','uid=','address=','count=','input='])
    except GetoptError:
        usageExit()

    for opt,arg in opts:
        if opt in ('-h','--help'):
            usageExit()
        if opt in ('-f','--func-code'):
            func = arg
        if opt in ('-F','--flood'):
            rq_type = 'flood'
        if opt in ('-t','--target'):
            ip_addr = arg
        if opt in ('-p','--port'):
            port = arg
        if opt in ('-u','--uid'):
            uid = arg
        if opt in ('-a','--address'):
            bit_addr=reg_addr = arg
        if opt in ('-c','--count'):
            bit_nb=reg_nb = arg
        if opt in ('-i','--input'):
            input_bit=input_reg = arg
        if not opts:
            print ("May the arguments with you!\n")
            usageExit()

    try:
        func
    except:
        func = '1'
    try:
        rq_type
    except:
        rq_type = "single"
    try:
        ip_addr
    except:
        print ("Please give me a target address!\n")
        usageExit()
    try:
        port
    except:
        port = "502"
    try:
        uid
    except:
        uid = "1"
    try:
        bit_addr
    except:
        bit_addr=reg_addr = "0"
    try:
        bit_nb
    except:
        bit_nb=reg_nb = "1"
    try:
        input_bit
    except:
        input_bit = "0"
        input_reg = "666"

    client = ModbusClient(ip_addr,int(port),int(uid),auto_open=None)

    if func == "1":
        readCoils(rq_type,client,bit_addr,bit_nb)
    elif func == "2":
        readDiscreteInputs(rq_type,client,bit_addr,bit_nb)
    elif func == "3":
        readHoldingRegisters(rq_type,client,reg_addr,reg_nb)
    elif func == "4":
        readInputRegisters(rq_type,client,reg_addr,reg_nb)
    elif func == "5":
        writeSingleCoil(rq_type,client,bit_addr,input_bit)
    elif func == "6":
        writeSingleRegister(rq_type,client,reg_addr,input_reg)
    elif func == "15":
        writeMultipleCoils(rq_type,client,bit_addr,bit_nb,input_reg)
    elif func == "16":
        writeMultipleRegisters(rq_type,client,reg_addr,reg_nb,input_reg)
    else:
        print ("Wrong Function Code. Supported Func. Codes: 1, 2, 3, 4, 5, 6, 15, 16")
        usageExit()

if __name__ == '__main__':
    main()
