import smbus

class I2CClass:

    def __init__(self):
        channel = 1
        bus = smbus.SMBus(channel)
        EQ_BassLow_chip = 0x2C
        EQ_High_chip = 0x2D
        EQ_pass_chip = 0x28
        break_10_chip = 0x2A
        break_100_chip = 0x2B
        break_M_12 = 0x2E
        break_M_34 = 0x2F

    # pot is 0 for RDAC1, 1 for RDAC2
    def MegpotI2C(self, chipAddress, pot, value):
        instruction = (pot << 7)    # pot is the MSB
        self.bus.write_i2c_block_data(chipAddress, instruction, [value])

    # pot is 0, 1, 2, or 3 for the respective RDAC
    def KpotI2C(self, chipAddress, pot, value):
        instruction = 0x10 + pot
        self.bus.write_i2c_block_data(chipAddress, instruction, [value])

    # pot is 0, 1, 2, or 3 for the respective RDAC
    # this function sets the startup value for the 5144
    def KpotSetStarting(self, chipAddress, pot):
        instruction = 0x70 + pot
        self.bus.write_i2c_block_data(chipAddress, instruction, [0x01])

    def send_EQ_bass_freq(self, value):
        self.MegpotI2C(self.EQ_BassLow_chip, 0, value)

    def send_EQ_low_freq(self, value):
        self.MegpotI2C(self.EQ_BassLow_chip, 1, value)

    def send_EQ_high_freq(self, value):
        self.MegpotI2C(self.EQ_High_chip, 0, value)

    def send_EQ_bass_pass(self, value):
        self.KpotI2C(self.EQ_pass_chip, 0, value)

    def send_EQ_low_pass(self, value):
        self.KpotI2C(self.EQ_pass_chip, 2, value)

    def send_EQ_high_pass(self, value):
        self.KpotI2C(self.EQ_pass_chip, 1, value)

    def send_EQ_treble_pass(self, value):
        self.KpotI2C(self.EQ_pass_chip, 3, value)

    def send_break_10_1(self, value):
        self.KpotI2C(self.break_10_chip, 0, value)

    def send_break_10_2(self, value):
        self.KpotI2C(self.break_10_chip, 1, value)

    def send_break_10_3(self, value):
        self.KpotI2C(self.break_10_chip, 2, value)

    def send_break_10_4(self, value):
        self.KpotI2C(self.break_10_chip, 3, value)

    def send_break_100_1(self, value):
        self.KpotI2C(self.break_100_chip, 0, value)

    def send_break_100_2(self, value):
        self.KpotI2C(self.break_100_chip, 1, value)

    def send_break_100_3(self, value):
        self.KpotI2C(self.break_100_chip, 2, value)

    def send_break_100_4(self, value):
        self.KpotI2C(self.break_100_chip, 3, value)

    def send_break_M_1(self, value):
        self.MegpotI2C(self.break_M_12, 0, value)

    def send_break_M_2(self, value):
        self.MegpotI2C(self.break_M_12, 1, value)

    def send_break_M_3(self, value):
        self.MegpotI2C(self.break_M_34, 0, value)

    def send_break_M_4(self, value):
        self.MegpotI2C(self.break_M_34, 1, value)


    # These functions set the starting value of the chosen pot to the current value
    # Should I have it that you pass a value and I set it to that, or just current?

    def set_break_10_1(self, value):
        self.KpotSetStarting(self.break_10_chip, 0)

    def set_break_10_2(self, value):
        self.KpotSetStarting(self.break_10_chip, 1)

    def set_break_10_3(self, value):
        self.KpotSetStarting(self.break_10_chip, 2)

    def set_break_10_4(self, value):
        self.KpotSetStarting(self.break_10_chip, 3)

    def set_break_100_1(self, value):
        self.KpotSetStarting(self.break_100_chip, 0)

    def set_break_100_2(self, value):
        self.KpotSetStarting(self.break_100_chip, 1)

    def set_break_100_3(self, value):
        self.KpotSetStarting(self.break_100_chip, 2)

    def set_break_100_4(self, value):
        self.KpotSetStarting(self.break_100_chip, 3)

    def set_EQ_bass_pass(self, value):
        self.KpotSetStarting(self.EQ_pass_chip, 0)

    def set_EQ_low_pass(self, value):
        self.KpotSetStarting(self.EQ_pass_chip, 2)

    def set_EQ_high_pass(self, value):
        self.KpotSetStarting(self.EQ_pass_chip, 1)

    def set_EQ_treble_pass(self, value):
        self.KpotSetStarting(self.EQ_pass_chip, 3)
