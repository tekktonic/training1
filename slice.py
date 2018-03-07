from csvfile import generator
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
        return  ("Accelerometer: " + str(self.accelerometer)
                 + "\nGravity sensor: " + str(self.gravity)
                 + "\nAcceleration: " + str(self.acceleration)
                 + "\nGyroscope: " + str(self.gyroscope)
                 + "\nLight sensor: " + str(self.light)
                 + "\nMagnetic Field sensor: " + str(self.mag_field)
                 + "\nOrentation sensor: " + str(self.orientation)
                 + "\nProximity sensor: " + str(self.proximity)
                 + "\nSound Level: " + str(self.sound)
                 + "\nLocation Data: " + str(self.location)
                 + "\nTime Since Start: " + str(self.time)
                 + "\nDate " + str(self.date_time + "\n"))

    def csv(self):
        return (",".join(self.accelerometer) +
                ",".join(self.gravity) +
                ",".join(self.acceleration) +
                ",".join(self.gyroscope) +
                ",".join(self.light))
def csv_next_slice():
    first_line = True
    for line in generator():
        if first_line:
            continue
        sl = DataSlice(tuple(line[0:3]), tuple(line[3:6]), tuple(line[6:9]), tuple(line[9:12]), line[12], tuple(line[12:15]), tuple(line[15:18]), line[18], line[19], tuple(line[20:27]), line[28], line[29], line[30])
        yield(sl)

for sl in csv_next_slice():
    sl.csv()
    break
