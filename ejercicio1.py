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

    def display_velocities(self):
        for i in range(len(self.times)):
            print(f"Velocidad en t = {self.times[i]}s: v = {self.velocities[i]} m/s")

# ejercicio 1
times = [0, 3, 5, 8, 10, 13]
distances = [0, 225, 383, 623, 742, 993]

taylor_approx = TaylorApproximation(times, distances)

taylor_approx.compute_velocities()

taylor_approx.display_velocities()
