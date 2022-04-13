import argparse
from tokenize import Exponent

argument_parser = argparse.ArgumentParser(description="Practical Electronic Components")
argument_parser.add_argument('-c', '--components',type=str, required=True ,help="Path to the component list")

args = argument_parser.parse_args()

class VoltageDivider:
    def __init__(self, supply, result, resistors):
        self.supply = float(supply)
        self.result = float(result)
        self.resistors = str(resistors)

    def __readFile(self):
        with open(self.resistors, 'r') as base_file:
            content = base_file.readlines()
        
        filtered = []
        for value in content:
            if value:
                filtered.append(float(value[:-1]))

        return filtered

    def __convert2Scientific(self, number):
        result = "{:e}".format(number).split('e')
        number = float(result[0])
        exponent = int(result[1])
        return number, exponent

    def __make_couples(self):
        # calculate devider ratio
        # (supply - result) / result
        div_ratio = (self.supply - self.result) / self.result
        resistors = self.__readFile() # read the component list and fetch the values
        resistor_couples = []

        for R1 in resistors:

            # calculate the ideal R2 value for the R1
            R2 = R1 * div_ratio
            R2 = self.__convert2Scientific(R2)

            # iterate through the component list to find the best maching component
            minimum_deviation = {'resistor':resistors[0], 'exponent':R2[1] ,'diviation': abs(R2[0] - resistors[0])} # setting the initial values

            for R2_practical in resistors:
                # find the minimum deviation
                current_diviation =  abs(R2[0] - R2_practical)

                if current_diviation  < minimum_deviation['diviation']:
                    minimum_deviation['diviation'] = current_diviation
                    minimum_deviation['resistor'] = R2_practical
                    minimum_deviation['exponent'] = R2[1]


            # now that we have found the most suitable resistor for choosed R1.
            # process the result and store it
            if(minimum_deviation['exponent'] <= 0):
                resistor_couple = {
                    'R1': R1 * 10 ** (-1 * minimum_deviation['exponent']),
                    'R2': minimum_deviation['resistor']
                }
                resistor_couple['voltage'] = round(self.supply * (resistor_couple['R1'] / (resistor_couple['R1'] + resistor_couple['R2'])), 4)
                resistor_couple['d_voltage'] = round(abs(self.result - resistor_couple['voltage']) * 1000)

            else:
                resistor_couple = {
                    'R1': R1,
                    'R2': minimum_deviation['resistor'] * 10 ** (minimum_deviation['exponent'])
                }
                resistor_couple['voltage'] = round(self.supply * (resistor_couple['R1'] / (resistor_couple['R1'] + resistor_couple['R2'])), 4)
                resistor_couple['d_voltage'] = round(abs(self.result - resistor_couple['voltage']) * 1000)

            resistor_couples.append(resistor_couple)

        # now that we have found the necesary couples
        # time to sort it out

        resistor_couples = sorted(resistor_couples, key=lambda data: data['d_voltage'])[:10]

        return resistor_couples

    def __print_results(self, content):
        
        print('+------------+---------+---------+----------------+----------------+')
        print('|    RANK    |    R1   |    R2   |   RESULT (V)   |   DELTA (mV)   |')
        print('+------------+---------+---------+----------------+----------------+')


        for index, row in enumerate(content):
            print("|{:^12}|{:^9}|{:^9}|{:^16}|{:^16}|".format(index + 1, row['R1'], row['R2'], row['voltage'], row['d_voltage']))

        print('+------------+---------+---------+----------------+----------------+')

    def run(self):
        final_content = self.__make_couples()
        self.__print_results(final_content)



def main():
    SUPPLY = float(input("Enter Supply Voltage    -> "))
    RESULT = float(input("Enter resulting Voltage -> "))

    v_divider = VoltageDivider(SUPPLY, RESULT, args.components)
    v_divider.run()


if __name__ == '__main__':
    main()