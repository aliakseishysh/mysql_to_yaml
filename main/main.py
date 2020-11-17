from database.connection import Connection, Cursor
from database.select import select_all
from database.use import database_use
from database.describe import describe_table
import os
from utils.files import save_to_yaml
import yaml


# Get Database And Table Names
DB_NAME = os.environ.get('DB_NAME')
TB_NAME = os.environ.get('TB_NAME')


def main():
    with Connection().connection:
        with Cursor().cursor as cursor:
            # USE database
            result = database_use(DB_NAME)
            print(result)
            
            # Select All Elements From Table
            result = select_all(TB_NAME)
            rows = cursor.fetchall()
            print(result)

            # Get Table Description
            table_desc = []
            for i in range(len(cursor.description)):
                desc = cursor.description[i]
                table_desc.append(desc[0])

            
            # Create Dicts
            dicts = []

            for row in rows:
                dicts.append({table_desc[i]: row[i] for i in range(len(table_desc))})

            # Save Dicts To Yaml
            
            yaml_dump = yaml.dump(dicts)
            result = save_to_yaml(TB_NAME + '.yaml', yaml_dump)
            print(result)

            
            
            