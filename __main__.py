from Bot import Bot,ConsoleUI




if __name__ == "__main__":
    print('Hello. I am your contact-assistant. What should I do with your contacts?')
    interface=ConsoleUI()
    bot = Bot(interface)
    bot.book.load("auto_save")
    commands = ['Add', 'Search', 'Edit', 'Load', 'Remove', 'Save', 'Congratulate', 'View', 'Exit']
    while True:
        action = input('Type help for list of commands or enter your command\n').strip().lower()
        if action == 'help':
            bot.interface.display_commands(commands)
            action = input('Enter command: ').strip().lower()
            bot.handle(action)
            if action in ['add', 'remove', 'edit']:
                bot.book.save("auto_save")
        elif action=='show_all':
            bot.interface.display_contacts(bot.book.data)
        else:
            bot.handle(action)
            if action in ['add', 'remove', 'edit']:
                bot.book.save("auto_save")
        if action == 'exit':
            break
