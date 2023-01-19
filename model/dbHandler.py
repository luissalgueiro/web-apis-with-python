import sqlite3 as SQL

def match_exact(word:str)->list:
    """
    This method will:
    1. Accept string
    2. Search the dictionary for the exact match
    3. If success, return the definition
    4. If not success, return empty list

    Args:
        word (str): word that will be searched

    Returns:
        list: definition of the word 
    """
    
    ## ToDo: Establish connection to the dictionary database
    ## ToDo: Query the database for the exact matches.
    ## ToDo: Clone the connection to the database
    
    db = SQL.connect('data/dictionary.db')
    sql_query  = "select * from entries where word=?"
    match_query = db.execute(sql_query, (word,)).fetchall()
    db.close()
    return match_query

def match_like(word:str) -> list:
    """
    
    Args:
        word (str): input word to be searched.
    Returns:
        list: if success, return description of the list
                if not, return empty list
    """
    ## ToDo: Establish connection to the dictionary database
    ## ToDo: Query the database for the exact matches.
    ## ToDo: Clone the connection to the database
    
    
    db = SQL.connect('data/dictionary.db')
    sql_query  = "select * from entries where word like ? "
    match_query = db.execute(sql_query, ("%"+word+"%",)).fetchall()
    db.close()
    return match_query

    
    return "ToDo"