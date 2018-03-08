from csvfile import generator

def blank_to_na(s):
    if s == "":
        return "NA"
    else:
        return s
    
class DataSlice(object):
    def __init__(self, accelerometer, gravity, acceleration, gyroscope, light, mag_field, orientation, proximity, sound, location, satellites, time, date_time):
        self.accelerometer = accelerometer
        self.gravity = gravity
        self.acceleration = acceleration
        self.gyroscope = gyroscope
        self.light = light
        self.mag_field = mag_field
        self.orientation = orientation
        self.proximity = proximity
        self.sound = sound
        self.location = location
        self.satellites = satellites
        self.time = time
        self.date_time = date_time


    def __str__(self):
        return  ("Accelerometer: " + str(list(map(lambda s: blank_to_na(s), self.accelerometer)))
                 + "\nGravity sensor: " + str(list(map(lambda s: blank_to_na(s),self.gravity)))
                 + "\nAcceleration: " + str(list(map(lambda s: blank_to_na(s),self.acceleration)))
                 + "\nGyroscope: " + str(list(map(lambda s: blank_to_na(s),self.gyroscope)))
                 + "\nLight sensor: " + blank_to_na(str(self.light))
                 + "\nMagnetic Field sensor: " + str(list(map(lambda s: blank_to_na(s), self.mag_field)))
                 + "\nOrentation sensor: " + str(list(map(lambda s: blank_to_na(s),self.orientation)))
                 + "\nProximity sensor: " + blank_to_na(str(self.proximity))
                 + "\nSound Level: " + blank_to_na(str(self.sound))
                 + "\nLocation Data: " + str(list(map(lambda s: blank_to_na(s), self.location)))
                 + "\nSatellites: " + blank_to_na(str(self.satellites))
                 + "\nTime Since Start: " + blank_to_na(str(self.time))
                 + "\nDate " + blank_to_na(str(self.date_time + "\n")))

    def csv(self):
        return (",".join(self.accelerometer) + "," +
                ",".join(self.gravity) + "," +
                ",".join(self.acceleration) + "," +
                ",".join(self.gyroscope) + 
                "," + self.light + ","
                ",".join(self.mag_field) + "," +
                ",".join(self.orientation) + "," +
                "," + self.proximity + 
                "," + self.sound + ","
                ",".join(self.location) + 
                "," + self.satellites +
                "," + self.time +
                "," + self.date_time)
        

def csv_next_slice():
    for line in generator():
        sl = DataSlice(tuple(line[0:3]), tuple(line[3:6]), tuple(line[6:9]), tuple(line[9:12]), line[12], tuple(line[13:16]), tuple(line[16:19]), line[19], line[20], tuple(line[21:28]), line[28], line[29], line[30])
        yield(sl)


