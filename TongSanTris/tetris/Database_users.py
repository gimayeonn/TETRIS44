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
        check_password=bcrypt.checkpw(input_password,data['user_password'].encode('utf-8'))
        return check_password


    def add_id_data(self,user_id):
        #추가하기
        curs = self.score_db.cursor()
        # 데이터베이스에 같은 id가 이미 존재하면 에러 메세지 띄우는 코드 필요.
        sql = "INSERT INTO users (user_id) VALUES (%s)"
        curs.execute(sql, user_id)
        self.score_db.commit()  #서버로 추가 사항 보내기
        curs.close()


    def add_password_data(self,user_password,user_id):
        #회원가입시 초기 경험치값은 0으로 설정
        #추가하기
        initial_exp=0
        new_salt=bcrypt.gensalt()
        new_password=user_password.encode('utf-8')
        hashed_password=bcrypt.hashpw(new_password,new_salt)
        decode_hash_pw=hashed_password.decode('utf-8')
        curs = self.score_db.cursor()
        sql = "UPDATE users SET user_password= %s WHERE user_id=%s"
        curs.execute(sql,(decode_hash_pw,user_id))
        self.score_db.commit()  #서버로 추가 사항 보내기
        curs = self.score_db.cursor()
        sql = "UPDATE users SET user_exp= %s WHERE user_id=%s"
        curs.execute(sql, (initial_exp, user_id))
        self.score_db.commit()
        curs.close()

    def load_exp_data(self,user_id):
        curs = self.score_db.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT * FROM users WHERE user_id=%s"
        curs.execute(sql, user_id)
        data = curs.fetchone()  # 리스트 안에 딕셔너리가 있는 형태
        curs.close()
        return data['user_exp']

    def update_exp_data(self,user_exp,user_id):
        
        curs = self.score_db.cursor()
        sql = "UPDATE users SET user_exp= %s WHERE user_id=%s"
        curs.execute(sql, (user_exp, user_id))
        self.score_db.commit()
        curs.close()

    def update_char_data(self,user_char,user_id):
        curs = self.score_db.cursor()
        sql = "UPDATE users SET user_character= %s WHERE user_id=%s"
        print("user_char>>>>>>>>> : ",user_char)
        curs.execute(sql, (user_char, user_id))
        self.score_db.commit()
        curs.close()


    def load_char_data(self,user_id):
        curs = self.score_db.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT * FROM users WHERE user_id=%s"
        curs.execute(sql, user_id)
        data = curs.fetchone()  # 리스트 안에 딕셔너리가 있는 형태
        curs.close()
        print("ID : ",data['user_id'])
        print("EXP : ",data['user_exp'])
        print("CHAR : ",data['user_character'])
        return data['user_character']


    def load_data(self, game_mode): #랭크 점수 데이터 불러오기
        #불러 오기
        curs = self.score_db.cursor(pymysql.cursors.DictCursor)
        if game_mode == 'basic':
            sql = "SELECT * FROM original_score ORDER BY score DESC "
        elif game_mode == 'hard':
            sql = "SELECT * FROM hard_score ORDER BY score DESC "
        elif game_mode == 'two':
            sql = "SELECT * FROM twohands_score ORDER BY score DESC"
        elif game_mode == 'mini':
            sql = "SELECT * FROM mini_score ORDER BY score DESC"
        elif game_mode == 'big':
            sql = "SELECT * FROM big_score ORDER BY score DESC"
        curs.execute(sql)
        data = curs.fetchall() #리스트 안에 딕셔너리가 있는 형태
        curs.close()
        print(data)
        return data

    def add_data(self,game_mode,  ID, score): #랭크 점수 기록
        #추가하기
        curs = self.score_db.cursor()
        if game_mode == 'basic':
            sql = "INSERT INTO original_score (ID, score) VALUES (%s, %s)"
        elif game_mode == 'hard':
            sql = "INSERT INTO hard_score (ID, score) VALUES (%s, %s)"
        elif game_mode == 'two':
            sql = "INSERT INTO twohands_score (ID, score) VALUES (%s, %s)"
        elif game_mode == 'mini':
            sql = "INSERT INTO mini_score (ID, score) VALUES (%s, %s)"
        elif game_mode == 'big':
            sql = "INSERT INTO big_score (ID, score) VALUES (%s, %s)"
        elif game_mode == 'ai':
            sql = "INSERT INTO ai_score (ID, score) VALUES (%s, %s)"
        curs.execute(sql, (ID, score))
        self.score_db.commit()  #서버로 추가 사항 보내기
        curs.close()
