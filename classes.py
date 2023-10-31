def display_sub_message(word):
    print('You are in the sub menu')
    print(f"You have selected {word} option\n")

def return_to_main_menu():
    main_menu = Main_Menu()
    main_menu.run()

from abc import ABC 

class Application_Screen(ABC):

    def run(self):

        options_list = list(self.OPTIONS_DICT.keys())

        while (True):
            self.display_screen()

            try:
                option_input = int(input('Please enter an option ->'))
                option = options_list[option_input-1]

                if (self.__class__.__name__ == 'Main_Menu'):
                    object = self.OPTIONS_DICT[option]()
                    object.run()
                else:
                    self.OPTIONS_DICT[option](option)
            except TypeError:
                self.OPTIONS_DICT[option]()
            except ValueError:
                print('Please enter a number between 1 and ' + len(self.OPTIONS_DICT))
            except IndexError:
                print('Not a valid option.')
                print('Please enter a number between 1 and ' + len(self.OPTIONS_DICT))


    def display_screen(self):
        print(self.SCREEN_TITLE)
        print(' ---------------------------')

        for index, value in enumerate(self.OPTIONS_DICT.keys()):
            print(f"{index+1}) {value}")

class Query_Screen(Application_Screen):

    OPTIONS_DICT = {'List Brokers': display_sub_message,
            'List all Shares': display_sub_message,
            'Lookup trade by trade id': display_sub_message,
            'Search for trade': display_sub_message,
            'Return to main menu': return_to_main_menu}
    SCREEN_TITLE = 'Query'

    def __init__(self):
        pass

class Export_Screen(Application_Screen):

    OPTIONS_DICT = {'Fetch Trades by Share_id': display_sub_message,
            'Fetch Trades by Broker_id': display_sub_message,
            'Fetch Trades by date_range': display_sub_message,
            'Return to main menu': return_to_main_menu}
    SCREEN_TITLE = 'Export Trade Data'

    def __init__(self):
        pass

class Reporting_Screen(Application_Screen):

    OPTIONS_DICT = {'Number of trades per broker': display_sub_message,
            'Share price history for a specified share_id': display_sub_message,
            'Proportion of trades traded on each exchange': display_sub_message,
            'Return to main menu': return_to_main_menu}
    SCREEN_TITLE = 'Reporting'

    def __init__(self):
        pass

class Main_Menu(Application_Screen):

    SCREEN_TITLE = 'Trade System Tools'

    OPTIONS_DICT = {'Query': Query_Screen,
            'Export trade data': Export_Screen,
            'Reporting': Reporting_Screen,
            'Exit': exit}

    def __init__(self):
        pass



