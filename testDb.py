import sys
import sqlite3
from sqlite3 import Error

createExtractionTable = """CREATE TABLE Extractions (
                                extract_id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
                                date date,
                                status TINYINT
                            );"""
createCoinsTable = """CREATE TABLE Coins (
                            ticker_id varchar(255) NOT NULL UNIQUE PRIMARY KEY,
                            name varchar(255)NOT NULL,
                            coin_id varchar(255) NOT NULL,
                            extract_id INTEGER,
                        CONSTRAINT fk_extract_id
                            FOREIGN KEY(extract_id)
                            REFERENCES Extractions(extract_id)
                        );"""

createPlatformsTable = """CREATE TABLE Platforms (
                        platform_id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
                        name varchar(255) NOT NULL,
                        nb_crypto_currencies INTEGER,
                        extract_id INTEGER,
                    CONSTRAINT fk_extract_id
                        FOREIGN KEY (extract_id)
                        REFERENCES Extractions(extract_id)
                );"""

createPricePlatformsCoinsTable = """CREATE TABLE Prices_platforms_coins (
                                    prices_id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
                                    prices float,
                                    platform_id INTEGER,
                                    extract_id INTEGER,
                                    ticker_id varchar(255) NOT NULL,
                                CONSTRAINT fk_platform_id
                                    FOREIGN KEY (platform_id)
                                    REFERENCES Platforms(platform_id),
                                CONSTRAINT fk_extract_id
                                    FOREIGN KEY (extract_id)
                                    REFERENCES Extractions(extract_id),
                                CONSTRAINT fk_ticker_id
                                    FOREIGN KEY (ticker_id)
                                    REFERENCES Coins(ticker_id)
                                );"""

createTweetsTable = """CREATE TABLE Tweets (
                            URL varchar(255) NOT NULL UNIQUE PRIMARY KEY,
                            date date,
                            content varchar(255) NOT NULL,
                            nb_likes INTEGER,
                            nb_retweets INTEGER,
                            extract_id INTEGER,
                            ticker_id varchar(255) NOT NULL,
                            indicator1 FLOAT,
                            indicator2 FLOAT,
                            indicator3 FLOAT,
                            indicator4 FLOAT,
                    CONSTRAINT fk_extract_id
                        FOREIGN KEY(extract_id)
                        REFERENCES Extractions(extract_id),
                    CONSTRAINT fk_ticker_id
                        FOREIGN KEY (ticker_id)
                        REFERENCES Coins(ticker_id)
                    );"""

dropExtractionTable = "drop table Extractions;"
dropCoinsTable = "drop table Coins;"
dropPlatformsTable = "drop table Platforms;"
dropPricePlatformsCoinsTable = "drop table Prices_platforms_coins;"
dropTweetsTable = "drop table Tweets;"
	
createTablesQueries = [createExtractionTable, createCoinsTable, createPlatformsTable, createPricePlatformsCoinsTable, createTweetsTable]
dropTablesQueries = [dropExtractionTable, dropCoinsTable, dropPlatformsTable, dropPricePlatformsCoinsTable, dropTweetsTable]
	
    



def execute_query(conn, query):     #execute une requete sur connection de DB
    try:
        c = conn.cursor()
        c.execute(query)
    except Error as e:
        print(e)

def create_tables(conn):
    """ 
    execute_query(conn,createExtractionTable)
    execute_query(conn,createCoinsTable)
    execute_query(conn,createPlatformsTable)
    execute_query(conn,createPricePlatformsCoinsTable)
    execute_query(conn,createTweetsTable)
    """
    for query in createTablesQueries:
        execute_query(conn, query)


def drop_tables(conn):
    for query in dropTablesQueries:
        execute_query(conn,query)

def create_connection(db_file):   
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None
 
def main():
    conn=create_connection("DBProject.sql")    #le nom du fichier de la DB en " "
    # Arguments handling
    if len(sys.argv)==1: # no argument => create all tables
        create_tables(conn)
    else: # at least 1 argument 
        if sys.argv[1]=="-d": # drop all tables
            drop_tables(conn)
        elif sys.argv[1]=="-r": # drop all table then create them
            drop_tables(conn)
            create_tables(conn)
        else:
            print("""Wrong argument; only accepted arguments are "-d", "-r" or no argument""")
    

if __name__=="__main__":
    main()