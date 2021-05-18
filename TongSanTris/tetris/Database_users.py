import pymysql
import bcrypt


class Database:
    def __init__(self):
        self.score_db = pymysql.connect(
            user='chin9510',
            password='tongsantris2021',
            host='tongsantris-db.cm8wqdx1uq7w.ap-northeast-2.rds.amazonaws.com',
            db='tongsantris',
            charset='utf8'
        )

    def compare_data(self, id_text, pw_text):
        # 불러 오기
        input_password=pw_text.encode('utf-8')
        curs = self.score_db.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT * FROM users WHERE user_id=%s"
        curs.execute(sql,id_text)
        data = curs.fetchone()  # 리스트 안에 딕셔너리가 있는 형태
        curs.close()
        # print(input_password)
        # print(data['user_password'].encode('utf-8'))
        # check_password=bcrypt.checkpw(input_password,data['user_password'].encode('utf-8'))
        # print(check_password)
        # return check_password
        return True


    def add_id_data(self,user_id):
        #추가하기
        curs = self.score_db.cursor()
        # 데이터베이스에 같은 id가 이미 존재하면 에러 메세지 띄우는 코드 필요.
        sql = "INSERT INTO users (user_id) VALUES (%s)"
        curs.execute(sql, user_id)
        self.score_db.commit()  #서버로 추가 사항 보내기
        curs.close()


    def add_password_data(self,user_password,user_id):
        #추가하기
        new_salt=bcrypt.gensalt()
        new_password=user_password.encode('utf-8')
        hashed_password=bcrypt.hashpw(new_password,new_salt)
        decode_hash_pw=hashed_password.decode('utf-8')
        curs = self.score_db.cursor()
        sql = "UPDATE users SET user_password= %s WHERE user_id=%s"
        curs.execute(sql,(decode_hash_pw,user_id))
        self.score_db.commit()  #서버로 추가 사항 보내기
        curs.close()
        test_pw=user_password
        print(test_pw.encode('utf-8'))
        print(decode_hash_pw)
        print(bcrypt.checkpw(test_pw.encode('utf-8'),decode_hash_pw.encode('utf-8')))
