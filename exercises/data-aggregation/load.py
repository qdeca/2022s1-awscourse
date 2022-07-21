import psycopg2


def main():
    connection = psycopg2.connect(user='postgres', password='postgres',
                                  host='default-db.cfcjvgyonsqr.eu-west-3.rds.amazonaws.com', port=5432)
    cursor = connection.cursor()
    with open("init_museum_table.sql", "r") as sql_file :
        cursor.execute(sql_file.read())
    #client.get_object(Bucket='top-data-eu-west-3', Key='french_museum_attendance.csv')



if __name__ == '__main__':
    main()
