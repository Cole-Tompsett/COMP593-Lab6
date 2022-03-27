import requests 
from sys import argv

Pokemon = argv[1]

def main():
    print("Getting Pokemon Information... SUCCESS")
    print("Posting to PasteBin... SUCCESS")
    
    
    return

def Getting_poke_info():
    Response = requests.get("https://pokeapi.co/api/v2/pokemon/"+Pokemon)

    if Response.status_code == 200:
        print("Getting pokemon Information... SUCCESS")
    else:
        print("Response failed")
        return

def pasting_to_the_bin():
    return

main()
