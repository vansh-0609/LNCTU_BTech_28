class solution:
    def largestaltitude(self,gain):

        altitude = 0
        max_altitude = 0

        for i in gain:
            altitude = altitude + i
            max_altitude = max(max_altitude,altitude)

        return max_altitude
