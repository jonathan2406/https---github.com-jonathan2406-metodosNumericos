class TaylorApproximation:
    def __init__(self, times, distances):
        self.times = times
        self.distances = distances
        self.velocities = [0.0] * len(self.times)

    def forward_difference(self, i):
        h = self.times[i+1] - self.times[i]
        return (self.distances[i+1] - self.distances[i]) / h

    def backward_difference(self, i):
        h = self.times[i] - self.times[i-1]
        return (self.distances[i] - self.distances[i-1]) / h

    def central_difference(self, i_minus, i_plus):
        h = self.times[i_plus] - self.times[i_minus]
        return (self.distances[i_plus] - self.distances[i_minus]) / h

    def compute_velocities(self):
        n = len(self.times)

        # Velocidad en el primer punto (aproximación hacia adelante)
        self.velocities[0] = self.forward_difference(0)

        # Velocidad en los puntos intermedios (aproximación central o hacia adelante/hacia atrás)
        for i in range(1, n-1):
            found_central = False
            # Buscar el intervalo más grande posible para diferencia central
            for j in range(1, min(i, n-i-1) + 1):
                if self.times[i] - self.times[i-j] == self.times[i+j] - self.times[i]:
                    self.velocities[i] = self.central_difference(i-j, i+j)
                    found_central = True
                    break

            if not found_central:
                # Si no se encuentra un intervalo adecuado, utilizar la diferencia hacia adelante o hacia atrás
                if i < n // 2:
                    self.velocities[i] = self.forward_difference(i)
                else:
                    self.velocities[i] = self.backward_difference(i)

        # Velocidad en el último punto (aproximación hacia atrás)
        self.velocities[-1] = self.backward_difference(n-1)

    def calcular_velocidad_en_x0(self, x0, h):
        # Buscar los índices para x0 - h y x0 + h
        i = self.times.index(x0)
        i_forward = self.times.index(round(x0 + h, 2)) if round(x0 + h, 2) in self.times else None
        i_backward = self.times.index(round(x0 - h, 2)) if round(x0 - h, 2) in self.times else None

        if i_forward is not None and i_backward is not None:
            return self.central_difference(i_backward, i_forward)
        elif i_forward is not None:
            return self.forward_difference(i)
        elif i_backward is not None:
            return self.backward_difference(i)


    def display_velocities(self):
        for i in range(len(self.times)):
            print(f"Velocidad en t = {self.times[i]}s: v = {self.velocities[i]} m/s")


times = [1.20, 1.29, 1.30, 1.31, 1.40]
distances = [11.59006, 13.78176, 14.04276, 14.30741, 16.86187]

taylor_approx = TaylorApproximation(times, distances)

x0 = 1.3
h = 0.1
velocidad_x0 = taylor_approx.calcular_velocidad_en_x0(x0, h)
print(f"Velocidad en t = {x0}s con h = {h}: v = {velocidad_x0} m/s")

h = 0.01
velocidad_x0 = taylor_approx.calcular_velocidad_en_x0(x0, h)
print(f"Velocidad en t = {x0}s con h = {h}: v = {velocidad_x0} m/s")
