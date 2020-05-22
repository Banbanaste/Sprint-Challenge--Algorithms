class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"

    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"

    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # sort the array through built in methods
        # at each place in the array check current "held" value against value at position
        # can only move in one dirrection until the end of the list

        # sort ascending when moving from left to right
        # -> check if held is greater than item at position
        # -> move right if it is
        # -> swap if it isnt
        # -> continue until end of list

        # sort descending when moving right to left
        # -> check if held is less than item at position
        # -> move left if it is
        # -> swap if it isnt
        # -> continue until end of list

        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """

        """ 
        set light on
        continue sorting while light is on
        before each round set light off
        if item was sorted set light on during round
        continue untill light is not turned on 

        while can move right 
        swap if held item is None
        check item against position item
        if None move right
        if item > position item move right
        if item < position item swap items and move right
        stop when you reach end of list

        while can move left
        swap if held item is None
        check item against position item
        if None move left 
        if item < position item move left
        if item > position item swap items and move left
        stop when you reach begining of list
        """

        self.set_light_on()

        while self.light_is_on():

            self.set_light_off()

            while self.can_move_right():
                if self.compare_item() is None:
                    self.swap_item()
                    self.set_light_off()
                elif self.compare_item() == -1:
                    self.set_light_on()
                    self.swap_item()
                elif self.compare_item() == 1:
                    self.set_light_off()
                self.move_right()
            else:
                self.move_right()

            while self.can_move_left():
                self.move_left()
            else:
                self.move_left()


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [4, 27, 1, 18, 28, 17, 20, 2, 44, 50]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
