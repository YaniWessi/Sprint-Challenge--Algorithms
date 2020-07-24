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
    # for i in range(len(l)-1):

    #     for j in range(0, l-i-1):
    #         if l[j] > l[j+1]:
    #             swap_item(j)
    # trade 'none' for the first item
        self.swap_item()
        # turn on light and start loop checking for light=on
        self.set_light_on()
        while self.light_is_on():
            # turn the light off here
            # loop will automatically exit unless a condition turns light on
            self.set_light_off()
            # loop that causes robot to move right if it can move right
            # this loop moves the biggest item to the end of the list
            while self.can_move_right():
                self.move_right()
                # if the held item is less than item at current pos, swap
                if self.compare_item() < 0:
                    self.swap_item()
            # at the end of list. if the held item is bigger than the last item, swap
            if self.compare_item() > 0:
                self.swap_item()
            # we already know last item is the highest value from the first pass-through, so
            # if robot can move left, move it left. we don't want to compare held item to last item
            if self.can_move_left():
                self.move_left()
            # a loop that checks for:
            # if the robot can move left and the held item is bigger than item at current position
            # swap the bigger held item with the smaller item at current position, then move left
            # this loop moves smaller items to the left of the list. if held item is bigger, swap
            # loop exits when we get to a value that is bigger than the held item
            while self.can_move_left() and self.compare_item() >= 0:
                self.swap_item()
                self.move_left()
            # this loop makes sure we are not back at the beginning. 'None' is at the beginning
            # if we are at the beginning, everything was successfully sorted, and dont turn on light
            # if we are not at the beginning of the list, move to the beginning, and turn on light
            while self.compare_item() != None:
                self.move_left()
                # if the light is not on, turn it on
                # the outer loop will continue for as long as the light is on
                if not self.light_is_on():
                    self.set_light_on()
        # after all the looping, we are back at the beginning and holding the first, smallest item
        # swap the held item back for 'none'
        self.swap_item()


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1,
         45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
