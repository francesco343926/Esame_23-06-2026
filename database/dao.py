from database.DB_connect import DBConnect
from model.user import User

class Dao:
    #def __init__(self):
        #pass

    @staticmethod
    def read_all_users():
        print("Executing read from database using SQL query")

        results = []
        cnx = DBConnect.get_connection()

        if cnx is None:
            print("Connection failed")
            return None

        cursor = cnx.cursor(dictionary=True)

        query = """ SELECT * FROM Users """

        cursor.execute(query)

        for row in cursor:
            user = User(
                row["user_id"],
                row["votes_funny"],
                row["votes_useful"],
                row["votes_cool"],
                row["name"],
                row["average_stars"],
                row["review_count"]
            )

            results.append(user)

        cursor.close()
        cnx.close()

        return results

    @staticmethod
    def getnodes(nbus):  # [obj]
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ select u.user_id, u.name, count(r.business_id) as totbus
from reviews r, users u
where r.user_id = u.user_id 
group by u.user_id  
having totbus > %s - 1"""
        cursor.execute(query, (nbus,))

        for row in cursor:
            u = User(id=row['user_id'],
                       name=row['name'],
                       totbus=row['totbus'])
            result.append(u)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getarchi(nodi, mappa, nbus):  # {(obj1, obj2)--> peso}
        conn = DBConnect.get_connection()
        result = dict()
        cursor = conn.cursor(dictionary=True)
        query = """ select r1.user_id as u1, r2.user_id as u2, count(*) totbuscomuni
from reviews r1, reviews r2
where r1.user_id in (select distinct tab.user_id
from (select u.user_id, u.name, count(r.business_id) as totbus
from reviews r, users u
where r.user_id = u.user_id 
group by u.user_id  
having totbus > %s - 1) tab)
	and r2.user_id in (select distinct tab.user_id
from (select u.user_id, u.name, count(r.business_id) as totbus
from reviews r, users u
where r.user_id = u.user_id 
group by u.user_id  
having totbus > %s - 1) tab)
	and r1.user_id < r2.user_id
	and r1.business_id = r2.business_id
group by r1.user_id, r2.user_id
                """
        cursor.execute(query, (nbus, nbus))

        for row in cursor:
            u1 = mappa[row['u1']]
            u2 = mappa[row['u2']]
            peso = row['totbuscomuni']
            result[(u1, u2)] = peso

        cursor.close()
        conn.close()
        return result
