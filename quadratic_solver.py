import math

class QuadraticSolver:

    #Coefficients of equation
    a, b, c = 1, 0, 0   # a cannot be zero

    discriminant = 0

    def __init__(self, coefficients_a:float, coefficients_b:float = 0, coefficients_c:float = 0):
        self.a = coefficients_a
        self.b = coefficients_b
        self.c = coefficients_c

        self.discriminant = self.get_discriminant()

    def get_discriminant(self) -> float:
        """Function to evaluate discriminant of the equation"""

        d = (self.b * self.b) - 4 * self.a * self.c # b^2 - 4ac
        return d

    def find_roots(self) -> list:
        """Return the roots of the equation as a list using the Quadratic formula"""

        roots = []

        if self.discriminant < 0:
            return roots

        elif self.discriminant == 0:
            x = (-self.b + math.sqrt(self.discriminant)) / (2 * self.a)
            roots.append(x)
            return roots

        else:
            x1 = (-self.b + math.sqrt(self.discriminant)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(self.discriminant)) / (2 * self.a)
            roots = [x1, x2]
            return roots

    def get_plot_values(self) -> dict:
        "Returns the X and Y values of the Quadratic equation for graph plotting"

        x_values = []
        y_values = []

        for x in range(-40, 41):
            y = (self.a * x * x) + (self.b * x) + self.c

            x_values.append(x)
            y_values.append(y)

        return {
                 "x" : x_values,
                 "y" : y_values
               }

if __name__ == "__main__":

    # Example for using QuadraticSolver class
    a = 1.6
    b = 2.1
    c = -1.4

    quad_solver = QuadraticSolver(a, b, c)

    print(f"Discriminant of the euqation : {quad_solver.discriminant}\n")

    print(f"Roots of the euqation : {quad_solver.find_roots()}\n")

    # print(f"X and Y values : {quad_solver.get_plot_values()} \n")

