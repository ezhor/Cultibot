import serial, time

def currentMoistureRawLevel():
        arduino = serial.Serial("/dev/ttyUSB0", 9600, timeout=10)
        time.sleep(5)
        arduino.reset_input_buffer()
        arduino.reset_output_buffer()
        arduino.write("?\n".encode())
        arduino.readline() # Ignore echo data
        data = int(arduino.readline())
        arduino.close()
        return data

if __name__ == "__main__":
    print(str(currentMoistureRawLevel()))