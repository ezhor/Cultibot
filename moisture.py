import serial, time, configparser

def currentMoistureRaw() -> int:
        arduino = serial.Serial("/dev/ttyUSB0", 9600, timeout=10)
        time.sleep(5)
        arduino.reset_input_buffer()
        arduino.reset_output_buffer()
        arduino.write("?\n".encode())
        arduino.readline() # Ignore echo data
        data = int(arduino.readline())
        arduino.close()
        return data

def rawToNormalized(rawValue: int) -> int:
        config = configparser.ConfigParser()
        config.read("../config.txt")
        min = int(config["Moisture"]["min"])
        max = int(config["Moisture"]["max"])
        maxDelta = min - max
        valueDelta = rawValue - max
        normalizedDelta = round(100 - (100 * valueDelta / maxDelta))
        return normalizedDelta


if __name__ == "__main__":
    print(str(rawToNormalized(currentMoistureRaw())) + "%")
