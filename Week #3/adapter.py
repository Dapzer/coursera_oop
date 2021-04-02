class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def lighten(self, grid):
        self.adaptee.set_dim((len(grid[0]), len(grid)))
        light = [(i2, i1) for i1, e1 in enumerate(grid) for i2, e2 in enumerate(e1) if e2 == 1]
        obstacles = [(i2, i1) for i1, e1 in enumerate(grid) for i2, e2 in enumerate(e1) if e2 == -1]
        print(light)
        print(obstacles)
        self.adaptee.set_lights(light)
        self.adaptee.set_obstacles(obstacles)

        return self.adaptee.generate_lights()
