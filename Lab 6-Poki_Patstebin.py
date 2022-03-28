import requests 
from sys import argv



def main():
    Pokemon = argv[1]

    Poke_Name = Getting_poke_info(Pokemon)
    
    poke_ability = poke_abilities(Poke_Name)
    

    pastebin_url = pasting_to_the_bin(poke_ability[1],poke_ability[0])
    
    print(pastebin_url)

    return

#gets information about the pokemon
def Getting_poke_info(Pokemon):

    print("Getting pokemon Information...", end=' ')
    Response = requests.get("https://pokeapi.co/api/v2/pokemon/"+Pokemon)

    if Response.status_code == 200:
        print("SUCCESS")
        dict_response = Response.json() 
        return(dict_response)
    else:
        print("Response failed")
        return

#lists the abilities of the pokemon and makes a title for the pastebin post
def poke_abilities(pokedict):
    title = pokedict['name'] + "'s abilities"

    poke_info = ""
    for pokeability in pokedict['abilities']:
        poke_info += "-"+pokeability['ability']['name']+"\n"
    
    return(poke_info,title)
    

#makes a pastebin post and returns the url back to the user
def pasting_to_the_bin(title, body):
    
    print("Posting to PasteBin...", end=' ')

    Params = {
        'api_dev_key':"f4R0OTFza_qTQ1NZJYLjoCeLqoHQux4X",
        'api_option':"paste",
        'api_paste_code': body,
        'api_paste_name': title
    }
    pastebin_response = requests.post("https://pastebin.com/api/api_post.php", data=Params)
    
    if pastebin_response.status_code == 200:
        print("SUCCESS")
        return(pastebin_response.text)
    else:
        print("Response Failed")
        return(pastebin_response.status_code)
main()
