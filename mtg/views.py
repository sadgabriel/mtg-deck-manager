from django.shortcuts import render, get_object_or_404, redirect
from django.db import connection
from django.http import HttpResponse

def root(request):
    return redirect('/mtg/login')

def login(request):
    message = ""
    
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    if username and password:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM user WHERE username = %s AND password = %s", [username, password])
            user = cursor.fetchall()
            
            if user:
                return redirect(f'/mtg/{user[0][1]}/home')
            else:
                message = "Username or Password Not Vaild"
    return render(request, 'mtg/login.html', {'message': message})

def home(request, username):
    name = request.POST.get('name')
    cost = request.POST.get('cost')
    type = request.POST.get('type')
    text = request.POST.get('text')
    power = request.POST.get('power')
    toughness = request.POST.get('toughness')
    
    search_color = request.POST.get('search_color')
    search_name = request.POST.get('search_name')
    button_type = request.POST.get('button_type')
    
    selected_deck = request.POST.getlist('selected_deck')
    deck_create_name = request.POST.get('deck_create_name')
    
    card_delete = request.POST.get('card_delete')
    
    with connection.cursor() as cursor:
        query = f"SELECT * FROM user WHERE username='{username}'"
        cursor.execute(query)
        user = cursor.fetchone()
        
        if button_type == 'add':
            query = "INSERT INTO card (name, cost, type, text, power, toughness) VALUES (%s, %s, %s, %s, %s, %s)"
            data = (name, cost, type, text, power, toughness)

            cursor.execute(query, data)
        
        if button_type == 'deck_create':
            deck_create = True
            
            if deck_create_name:
                query = "INSERT INTO deck (deckname, username) VALUES (%s, %s)"
                data = (deck_create_name, username)

                cursor.execute(query, data)
        else:
            deck_create = False
            
        if button_type == 'deck_delete' and selected_deck:
            for deckname in selected_deck:
                query = f"DELETE FROM deck WHERE deckname='{deckname}'"
                cursor.execute(query)
                
        if button_type == 'deck_open' and selected_deck:
            return redirect(f'/mtg/{username}/home/{selected_deck[0]}')
                
        if card_delete:
            query = f"DELETE FROM card WHERE name='{card_delete}'"
            cursor.execute(query)
        
        if search_color and search_color != 'reset':
            query = f"SELECT * FROM card WHERE cost LIKE '%{search_color}%'"
            cursor.execute(query)
        elif button_type == 'search':
            query = f"SELECT * FROM card WHERE name LIKE '%{search_name}%'"
            cursor.execute(query)
        else:
            cursor.execute("SELECT * FROM card")
            
        cards = cursor.fetchall()
        
        query = f"SELECT * FROM deck WHERE username='{username}'"
        cursor.execute(query)
        decks = cursor.fetchall()
        
        return render(request, 'mtg/home.html', {'cards': cards, 'decks': decks, 'deck_create': deck_create, 'user': user})
    
def deck(request, username, deckname):
    name = request.POST.get('name')
    cost = request.POST.get('cost')
    type = request.POST.get('type')
    text = request.POST.get('text')
    power = request.POST.get('power')
    toughness = request.POST.get('toughness')
    
    search_color = request.POST.get('search_color')
    search_name = request.POST.get('search_name')
    button_type = request.POST.get('button_type')
    
    card_delete = request.POST.get('card_delete')
    
    clicked_card = request.POST.get('clicked_card')
    removed_card = request.POST.get('removed_card')
    
    with connection.cursor() as cursor:
        query = f"SELECT * FROM user WHERE username='{username}'"
        cursor.execute(query)
        user = cursor.fetchone()
        
        query = f"SELECT * FROM deck WHERE deckname='{deckname}'"
        cursor.execute(query)
        deck = cursor.fetchone()
        
        if button_type == 'exit_deck':
            return redirect(f'/mtg/{username}/home')
        
        if button_type == 'add':
            query = "INSERT INTO card (name, cost, type, text, power, toughness) VALUES (%s, %s, %s, %s, %s, %s)"
            data = (name, cost, type, text, power, toughness)

            cursor.execute(query, data)
            
        if card_delete:
            query = f"DELETE FROM card WHERE name='{card_delete}'"
            cursor.execute(query)
            
        if clicked_card:
            query = f"SELECT number FROM contain WHERE cardname='{clicked_card}'"
            cursor.execute(query)
            contain = cursor.fetchone()
            
            if contain and contain[0] < 4:
                query = f"UPDATE contain SET number={contain[0]+1} WHERE cardname='{clicked_card}'"
                cursor.execute(query)
            elif contain is None:
                query = "INSERT INTO contain (deckname, cardname, number) VALUES (%s, %s, 1)"
                data = (deckname, clicked_card)
                cursor.execute(query, data)
        
        if removed_card:
            query = f"SELECT number FROM contain WHERE cardname='{removed_card}'"
            cursor.execute(query)
            contain = cursor.fetchone()
            
            if contain[0] > 1:
                query = f"UPDATE contain SET number={contain[0]-1} WHERE cardname='{removed_card}'"
                cursor.execute(query)
            else:
                query = f"DELETE FROM contain WHERE cardname='{removed_card}'"
                cursor.execute(query)
        
        if search_color and search_color != 'reset':
            query = f"SELECT * FROM card WHERE cost LIKE '%{search_color}%'"
            cursor.execute(query)
        elif button_type == 'search':
            query = f"SELECT * FROM card WHERE name LIKE '%{search_name}%'"
            cursor.execute(query)
        else:
            cursor.execute("SELECT * FROM card")
            
        cards = cursor.fetchall()
        
        query = f"SELECT cardname, number FROM contain WHERE deckname='{deckname}'"
        cursor.execute(query)
        contains = cursor.fetchall()
        
        
        return render(request, 'mtg/deck.html', {'cards': cards, 'contains': contains, 'user': user, 'deck': deck})