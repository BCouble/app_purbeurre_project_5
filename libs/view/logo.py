from pyfiglet import Figlet


def create_logo():
    custom_fig = Figlet(font='doom')
    logo = custom_fig.renderText('OC Pur Beurre')

    return logo

