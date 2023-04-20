#!/usr/bin/python3
"""
    Entry point of the command interpreter.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
        Implementation of cmd module for HBNB command prompt.
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
            Quit command to exit the program.
        """
        return True

    def do_eof(self, arg):
        """
            EOF command to exit the program.
        """
        print()
        return True

    def emptyline(self):
        """
            Do not execute anything when an empty line + ENTER is passed.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
