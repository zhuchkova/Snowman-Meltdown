# Snowman ASCII Art stages
STAGES = [
     # Stage 0: Full snowman
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
     # Stage 1: Bottom part starts melting
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
     # Stage 2: Only the head remains
     """
      ___  
     /___\\ 
     (o o) 
     """,
     # Stage 3: Snowman completely melted
     """
      ___  
     /___\\ 
     """
 ]

########## COLORS (ANSI) #############
class C:
    RESET = "\033[0m"
    BOLD = "\033[1m"

    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"

# Define helping functions for color printing

def cprint(text, color=""):
    print(f"{color}{text}{C.RESET}")

def cinput(prompt, color=C.GREEN):
    return input(f"{color}{prompt}{C.RESET}")

def print_stages(text):
    return cprint(text, C.MAGENTA)

def print_word(word):
    return cprint(f"Word: {word}", C.CYAN)

def game_over(word):
    cprint(f"Game Over! The word was: {word}", C.RED + C.BOLD)

def success(text):
    cprint(text, C.BLUE + C.BOLD)

def info(text):
    cprint(text, C.YELLOW)

###########################################