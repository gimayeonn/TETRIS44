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

    def id_not_exists(self,input_id): # 아이디가 데이터베이스에 존재하는지 확인
        curs = self.score_db.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT * FROM users WHERE user_id=%s"
        curs.execute(sql, input_id)
        data = curs.fetchone()
        curs.close()
        if data:
            return False
        else:
            return True


    def compare_data(self, id_text, pw_text): # 데이터베이스의 아이디와 비밀번호 비교교
       # 불러 오기
        input_password=pw_text.encode('utf-8')
        curs = self.score_db.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT * FROM users WHERE user_id=%s"
        curs.execute(sql,id_text)
        data = curs.fetchone()
        curs.close()
        check_password=bcrypt.checkpw(input_password,data['user_password'].encode('utf-8'))
        return check_password


    def add_id_data(self,user_id): # 아이디 추가
        #추가하기
        curs = self.score_db.cursor()
        sql = "INSERT INTO users (user_id) VALUES (%s)"
        curs.execute(sql, user_id)
        self.score_db.commit()  #서버로 추가 사항 보내기
        curs.close()


    def add_password_data(self,user_password,user_id): # 비밀번호 추가
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

    def load_exp_data(self,user_id):  # 경험치 데이터 불러오기
        curs = self.score_db.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT * FROM users WHERE user_id=%s"
        curs.execute(sql, user_id)
        data = curs.fetchone()  # 리스트 안에 딕셔너리가 있는 형태
        curs.close()
        return data['user_exp']

    def update_exp_data(self,user_exp,user_id): # 경험치 데이터베이스에 업데이트
        curs = self.score_db.cursor()
        sql = "UPDATE users SET user_exp= %s WHERE user_id=%s"
        curs.execute(sql, (user_exp, user_id))
        self.score_db.commit()
        curs.close()

    def update_char_data(self,user_char,user_id): # 캐릭터 추가
        curs = self.score_db.cursor()
        sql = "UPDATE users SET user_character= %s WHERE user_id=%s"
        print("user_char>>>>>>>>> : ",user_char)
        curs.execute(sql, (user_char, user_id))
        self.score_db.commit()
        curs.close()


    def load_char_data(self,user_id): #캐릭터정보 불러오기
        curs = self.score_db.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT * FROM users WHERE user_id=%s"
        curs.execute(sql, user_id)
        data = curs.fetchone()  # 리스트 안에 딕셔너리가 있는 형태
        curs.close()
        print("ID : ",data['user_id'])
        print("EXP : ",data['user_exp'])
        print("CHAR : ",data['user_character'])
        return data['user_character']

    def add_data(self,game_mode,  ID, score):
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
