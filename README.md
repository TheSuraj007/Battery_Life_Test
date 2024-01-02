## Please follow the instructions below
- Step:1 - Make the proper conection of the battery with the arduino board. Attached the battery wire to the A0 pin of the Arduino board.
- Step:1 - Now connect the Arduino board to the computer and modify the arduino code according to the COMPORT.
- Step:1 - Flash the "Battery_testing_arduino.ino" file to the Arduino UNO board
- Step:2 - After successfully flashing the arduino board, now run the python script. to run the script, enter the following command "python .\battery_test_req.py" on the terminal.
- Step:3 - Now python script will get the battery voltage from the arduino board via UART interface.
- Step:4 - Python script will create a csv file with "battery_data.csv". 
- Step:5 - And after taht it will save the battery voltage along with  the date-time stamp on the csv file.