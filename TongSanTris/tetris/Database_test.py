import pymysql


class Database:
    def __init__(self):
        self.score_db = pymysql.connect(
            user='chin9510',
            password='tongsantris2021',
            host='tongsantris-db.cm8wqdx1uq7w.ap-northeast-2.rds.amazonaws.com',
            db='tongsantris',
            charset='utf8'
        )


    def load_id_data(self):
        #불러 오기
        curs = self.score_db.cursor(pymysql.cursors.DictCursor)
        sql = "select user_id from users"
        curs.execute(sql)
        data = curs.fetchall() #리스트 안에 딕셔너리가 있는 형태
        curs.close()
        return data

    def load_password_data(self):
        #불러 오기
        curs = self.score_db.cursor(pymysql.cursors.DictCursor)
        sql = "select user_password from users"
        curs.execute(sql)
        data = curs.fetchall() #리스트 안에 딕셔너리가 있는 형태
        curs.close()
        return data

    def add_id_data(self,user_id):
        #추가하기
        curs = self.score_db.cursor()
        # 데이터베이스에 같은 id가 이미 존재하면 에러 메세지 띄우는 코드 필요.
        sql = "INSERT INTO users (user_id) VALUES (%s)"
        curs.execute(sql, user_id)
        self.score_db.commit()  #서버로 추가 사항 보내기
        curs.close()


    def add_password_data(self,user_password):
        #추가하기
        curs = self.score_db.cursor()
        sql = "UPDATE users SET user_password= %s WHERE user_id='aaa'" # 일단 aaa라고 해놨는데 user_id를 받아올 수 있으면 user_id로 바꾸면 가능할듯함.
        curs.execute(sql,user_password)
        self.score_db.commit()  #서버로 추가 사항 보내기
        curs.close()
