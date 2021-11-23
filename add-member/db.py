import sqlite3


class Db:
    DB_NAME = "telegram_bot_db"
    def __init__(self):
        self.main()

    def main(self):
       self.create_table_accounts()
       self.create_table_settings()

    def get_db_connection(self):
        con = sqlite3.connect(self.DB_NAME,detect_types= sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        return con

    def create_table_settings(self):
        con = self.get_db_connection()

        sql = """ CREATE TABLE IF NOT EXISTS settings(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        only_megagroups BOOLEAN NOT NULL,
        skip_added_users BOOLEAN NOT NULL,
        automatic_settings_for_multy_accounts BOOLEAN NOT NULL,
        scrape_active_users BOOLEAN NOT NULL,
        users_add_interval INTEGER NOT NULL,
        users_batches_interval INTEGER NOT NULL,
        users_per_batch INTEGER NOT NULL
        )
        """
        con.execute(sql)
        con.close()

    def create_table_accounts(self):
        con = self.get_db_connection()

        sql = """ CREATE TABLE IF NOT EXISTS accounts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        phone TEXT NOT NULL,
        api_id INTEGER NOT NULL,
        api_hash TEXT NOT NULL
        )
        """
        con.execute(sql)
        con.close()

    def insert_settings(self,only_megagroups, skip_added_users, atomatic_settings_for_multiple_accounts,scrape_only_recently_active_users,users_add_interval,users_batches_interval,users_per_batch):
        con = self.get_db_connection().cursor()
        
        sql = """INSERT INTO settings
        VALUES(
            :only_megagroups,
            :skip_added_users,
            :atomatic_settings_for_multiple_accounts,
            :scrape_only_recently_active_users,
            :users_add_interval,
            :users_batches_interval,
            :users_per_batch
        )
        """
        query_params = {
            "only_megagroups": only_megagroups,
            "skip_added_users": skip_added_users,
            "atomatic_settings_for_multiple_accounts": atomatic_settings_for_multiple_accounts,
            "scrape_only_recently_active_users":scrape_only_recently_active_users,
            "users_add_interval": users_add_interval,
            "users_batches_interval":users_batches_interval,
            "users_per_batch": users_per_batch
        }

        con.execute(sql,query_params)
        id = con.lastrowid
        con.close()

        return id
    
    def insert_account(self,phone, api_id,api_hash):
        if self.if_account_exist(phone):
            return

        con = self.get_db_connection()
        
        sql = """INSERT INTO accounts
        (
            phone,
            api_id,
            api_hash
        )
        VALUES(
            :phone,
            :api_id,
            :api_hash
        )
        """
        query_params = {
            "phone": phone,
            "api_id": api_id,
            "api_hash":api_hash
        }

        con.execute(sql,query_params)
        con.commit()
        con.close()

    def update_settings(self,id,
                        only_megagroups = None,
                        skip_added_users = None,
                        automatic_settings_for_multiple_accounts = None,
                        scrape_only_recently_active_users = None,
                        users_add_interval = None,
                        users_batches_interval = None,
                        users_per_batch = None):
        con = self.get_db_connection()
        
        sql = """ UPDATE settings SET """
        query = []
        if only_megagroups != None:
            query.append("""only_megagroups = :only_megagroups""")
        if skip_added_users != None:
            query.append("""skip_added_users = :skip_added_users""")
        if automatic_settings_for_multiple_accounts != None:
            query.append("""automatic_settings_for_multiple_accounts = :atomatic_settings_for_multiple_accounts""")
        if scrape_only_recently_active_users != None:
            query.append("""scrape_only_recently_active_users = :scrape_only_recently_active_users""")
        if users_add_interval != None:
            query.append("""users_add_interval = :users_add_interval""")
        if users_batches_interval != None:
            query.append("""users_batches_interval = :users_batches_interval""")
        if users_per_batch != None:
            query.append("""users_per_batch = :users_per_batch""")
              
        sql = f"""UPDATE settings SET {",".join(query)} WHERE id = :id"""
        
        query_params = {
            "id": id,
            "only_megagroups": only_megagroups,
            "skip_added_users": skip_added_users,
            "atomatic_settings_for_multiple_accounts": automatic_settings_for_multiple_accounts,
            "scrape_only_recently_active_users":scrape_only_recently_active_users,
            "users_add_interval": users_add_interval,
            "users_batches_interval":users_batches_interval,
            "users_per_batch": users_per_batch
        }

        con.execute(sql,query_params)
        con.commit()
        con.close()

    def get_settings_by_id(self, id):
        con = self.get_db_connection().cursor()
        
        sql = """SELECT * FROM settings WHERE id = ?"""

        con.execute(sql,{"id": id})
        settings = []

        for item in Mapper(con):
            settings.append(item)
        con.close()

        return settings
    def get_all_settings(self):
        con = self.get_db_connection().cursor()

        sql = """SELECT * FROM settings"""

        con.execute(sql)

        settings = []
        for item in Mapper(con):
            settings.append(item)

        return settings

    def get_all_accounts(self):
        con = self.get_db_connection().cursor()

        sql = """SELECT * FROM accounts""" 

        con.execute(sql)

        result = []
        for item in Mapper(con):
            result.append(item)

        con.close()
        return result
    def get_account_by_phone(self, phone):
        con = self.get_db_connection().cursor()

        sql = """SELECT * FROM accounts WHERE phone = :phone"""
        con.execute(sql, {"phone":phone})
        account = []
        for item in Mapper(con):
            account.append(item)
        con.close()

        return account
    def delete_account(self, id):
        con = self.get_db_connection()

        sql = """DELETE FROM accounts WHERE id = ?"""
        con.execute(sql,(id,))
        con.commit()
        con.close()
    def if_account_exist(self, phone):
        con = self.get_db_connection().cursor()
        sql = """SELECT * FROM accounts WHERE phone = :phone"""

        con.execute(sql, {"phone":phone})
        account = con.fetchone()
        con.close()

        if account == None:
            return False
        else:
            return True

class Mapper():
    def __init__(self, cursor):
        self._cursor = cursor
    
    def __iter__(self):
        return self

    def __next__(self):
        row = self._cursor.__next__()
        return { description[0]: row[col] for col, description in enumerate(self._cursor.description) }

        






