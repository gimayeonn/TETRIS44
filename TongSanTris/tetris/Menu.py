import pygame
from variable import Var
import pygame_menu
from Tetris import *
from Database_users import *
import time


class Menu:

    def __init__(self):
        pygame.init()
        Var.infoObject = pygame.display.Info()
        self.tetris=Tetris()
        self.database = Database()
        self.w=Var.menu_display_w
        self.h=Var.menu_display_h
        self.Mode = Var.initial_mode
        self.id=Var.initial_id
        self.score=Var.initial_score
        self.page=Var.initial_page
        self.surface=pygame.display.set_mode((self.w,self.h),RESIZABLE)
        self.mytheme=Var.mytheme
        self.mytheme2=Var.mytheme_help
        self.menu = pygame_menu.Menu(self.h,self.w, '', theme=self.mytheme)
        self.font_main=Var.font_main   # 메인 폰트 사이즈
        self.font_sub=Var.font_sub     # 서브 폰트 사이즈
        self.widget_margin_login=Var.widget_margin_login       #로그인 위젯 사이 간격
        self.widget_margin_main=Var.widget_margin_main         #메인 위젯 사이 간격
        self.widget_margin_showpage=Var.widget_margin_showpage #show 페이지 위젯 사이 간격
        self.widget_margin_rank=Var.widget_margin_rank         #rank 페이지 위젯 사이 간격
        self.margin_main=Var.margin_main                       #메인 페이지 x,y 위젯 시작 위치
        self.margin_show=Var.margin_show                       #show 페이지 x,y 위젯 시작 위치
        self.margin_help=Var.margin_help                       #help 페이지 back 위치
        self.margin_rank=Var.margin_rank                       #rank 페이지 x,y 위젯 시작 위치
        self.id


#add_button 이거는 선택하는 버튼 만들기
#clear()는 초기화하기
#add_vertical_margin 위에서 부터 간격 설정하기
#add_label 은 텍스트만 있는 것 만들기
#add_text_input 은 텍스트 입력 받아 함수 실행 가능한 것
#자세한 것은 깃허브 pygame_menu에 자세하게 나와있습니다. 참고하세요

    def run(self):   # 실행하는 함수
        print('test2')
        self.page=Var.initial_page   #시작하면 기본 모드로 모드가 설정
        self.menu.clear()
        self.mytheme.widget_margin=self.widget_margin_login
        self.menu.add_vertical_margin(self.margin_main)
        self.menu.add_button('  Sign Up  ', self.signup_page, font_size=self.font_sub)
        self.menu.add_button('  Log In  ', self.login_page, font_size=self.font_sub)
        self.menu.add_button('        Quit         ', pygame_menu.events.EXIT, font_size=self.font_sub)

    def first_page(self):
        self.surface = pygame.display.set_mode((self.w, self.h), RESIZABLE)
        self.menu = pygame_menu.Menu(self.h, self.w, '', theme=self.mytheme)
        self.page = 'page0'
        self.mytheme.widget_margin = self.widget_margin_login
        Var.click.play()
        self.page = Var.initial_page
        self.menu.clear()
        self.menu.add_vertical_margin(self.margin_main)
        self.menu.add_button('  Sign Up  ', self.signup_page, font_size=self.font_sub)
        self.menu.add_button('  Log In  ', self.login_page, font_size=self.font_sub)
        self.menu.add_button('        Quit         ', pygame_menu.events.EXIT, font_size=self.font_sub)

    def login_page(self): ##로그인 페이지
        self.surface = pygame.display.set_mode((self.w, self.h), RESIZABLE)
        self.menu = pygame_menu.Menu(self.h, self.w, '', theme=self.mytheme)
        self.page='page1'
        self.mytheme.widget_margin=self.widget_margin_login
        Var.click.play()
        self.menu.clear()
        self.menu.add_vertical_margin(self.margin_main)
        self.menu.add_text_input('ID : ', maxchar=100, onreturn=self.get_text, font_size=self.font_sub)
        self.menu.add_text_input('PASSWORD : ', maxchar=100, onreturn=self.get_text2,password=True, password_char='*', font_size=self.font_sub)
        self.menu.add_button('  Log In   ', self.login,font_size=self.font_sub)
        self.menu.add_button('  back  ', self.first_page, font_size=self.font_sub)
        self.menu.add_button('        Quit         ', pygame_menu.events.EXIT,font_size=self.font_sub)



    def login(self):
        if self.id:
            if self.password and self.database.compare_data(self.id, self.password):
                # 현재 선택 캐릭터가 없다면 캐릭터 선택 (char변수 할당) (아직 미구현)
                char = self.database.load_char_data(self.id)
                if char is None:
                    print("select char")
                    self.menu.clear()
                    #self.menu = pygame_menu.Menu(self.h, self.w, '', theme=self.mytheme)
                    path = "assets/images/"
                    self.menu.add_button('1) Elephant', self.set_char1,font_size=self.font_sub)
                    self.menu.add_image(Var.char1_lst[0][0])
                    self.menu.add_button('2) Chicken', self.set_char2,font_size=self.font_sub)
                    self.menu.add_image(Var.char2_lst[0][0])
                    self.menu.add_button('3) Butterfly', self.set_char3, font_size=self.font_sub)
                    self.menu.add_image(Var.char3_lst[0][0])
                    self.menu.add_button('  back  ', self.login_page, font_size=self.font_sub)
                else:
                    self.show_list()

                # 계정의 exp,char 값 가져오기
                Var.exp=self.database.load_exp_data(self.id) #로그인 성공하면 경험치 데이터베이스에서 받아오기
                Var.char=self.database.load_char_data(self.id)
                if char==1:
                    Var.lst = Var.char1_lst
                elif char==2:
                    Var.lst = Var.char2_lst
                elif char==3:
                    Var.lst = Var.char3_lst
                Var.user_id = self.id

            else:
                self.login_page()
        else:
            self.login_page()

    def set_char1(self):
        Var.char = 1
        self.database.update_char_data(Var.char,Var.user_id)
        Var.lst = Var.char1_lst
        Var.user_id = self.id
        self.show_list()

    def set_char2(self):
        Var.char = 2
        self.database.update_char_data(Var.char,Var.user_id)
        Var.lst = Var.char2_lst
        Var.user_id = self.id
        self.show_list()

    def set_char3(self):
        Var.char = 3
        self.database.update_char_data(Var.char,Var.user_id)
        Var.lst = Var.char3_lst
        Var.user_id = self.id
        self.show_list()

    #아이디 입력값
    def get_text(self,value):
        self.id = value

    #비밀번호 입력값
    def get_text2(self,value):
        self.password=value

    def save_id(self,value): #아이디 데이터베이스에 저장
        self.id=value
        self.database.add_id_data(self.id)

    def save_password(self,value): #비밀번호 데이터베이스에 저장
        self.password=value
        self.database.add_password_data(self.password,self.id)


    def signup_page(self):  ##첫 페이지 회원가입 페이지
        self.surface = pygame.display.set_mode((self.w, self.h), RESIZABLE)
        self.menu = pygame_menu.Menu(self.h, self.w, '', theme=self.mytheme)
        self.page='page2'
        self.mytheme.widget_margin=self.widget_margin_login
        Var.click.play()
        self.menu.clear()
        self.menu.add_vertical_margin(self.margin_main)
        self.menu.add_text_input('ID : ', maxchar=100, onreturn=self.save_id,font_size=self.font_sub)
        self.menu.add_text_input('PASSWORD : ', maxchar=100, onreturn=self.save_password,password=True, password_char='*', font_size=self.font_sub)
        self.menu.add_button('  Sign Up  ', self.login_page, font_size=self.font_sub)
        self.menu.add_button('  back  ', self.first_page, font_size=self.font_sub)
        self.menu.add_button('        Quit         ', pygame_menu.events.EXIT,font_size=self.font_sub)


    def show_list(self):  ## 뒤로 갈때 보여줄 목록들
        self.surface = pygame.display.set_mode((self.w, self.h), RESIZABLE)
        self.menu = pygame_menu.Menu(self.h, self.w, '', theme=self.mytheme)
        self.page='page3'
        self.mytheme.widget_margin=self.widget_margin_main
        Var.click.play()
        self.menu.clear()
        self.menu.add_vertical_margin(self.margin_main)
        self.menu.add_button('   Select mode   ', self.show_game,font_size=self.font_sub)
        self.menu.add_button('    Show Rank    ', self.show_rank,font_size=self.font_sub)
        self.menu.add_button('    My Info.    ', self.show_info,font_size=self.font_sub)
        self.menu.add_button('  Help  ', self.help, font_size=self.font_sub)
        self.menu.add_button('   Select theme   ',self.change_theme,font_size=self.font_sub)
        self.menu.add_button('   Select BGM   ',self.change_base_bgm,font_size=self.font_sub)
        self.menu.add_button(' Log Out ', self.login_page, font_size=self.font_sub)
        self.menu.add_button('        Quit         ', pygame_menu.events.EXIT,font_size=self.font_sub)


    def show_game(self):  ## 게임 목록 들어가면 나오는 목록들
        self.page='page4'
        Var.click.play()
        self.menu.clear()
        self.mytheme.widget_margin=self.widget_margin_showpage
        self.menu.add_vertical_margin(self.margin_main)
        self.menu.add_label("    --Start game--    ",selectable=False,font_size=self.font_main)
        self.menu.add_vertical_margin(self.margin_show)
        self.menu.add_button('      Single mode      ', self.select_single,font_size=self.font_sub)
        self.menu.add_button('       MiNi mode       ', self.start_the_Mini,font_size=self.font_sub)
        self.menu.add_button('       Big mode       ', self.start_the_Big,font_size=self.font_sub)
        self.menu.add_button('    Twohands mode   ', self.start_the_Twohands,font_size=self.font_sub)
        self.menu.add_button('    vs Computer   ', self.start_the_Ai,font_size=self.font_sub)
        self.menu.add_button('           back            ', self.show_list,font_size=self.font_sub)

    def select_single(self):
        self.page='page12'
        Var.click.play()
        self.menu.clear()
        self.mytheme.widget_margin=self.widget_margin_showpage
        self.menu.add_vertical_margin(self.margin_main)
        self.menu.add_label("    --Select--    ",selectable=False,font_size=self.font_main)
        self.menu.add_vertical_margin(self.margin_show)
        self.menu.add_button('      Easy mode      ', self.start_the_game,font_size=self.font_sub)
        self.menu.add_button('      Hard mode      ', self.start_the_hard,font_size=self.font_sub)
        self.menu.add_button('           back            ', self.show_game,font_size=self.font_sub)

    def show_rank(self):  ## 랭크 들어가면 나오는 목록들기
        self.page='page5'
        Var.click.play()
        self.menu.clear()
        self.mytheme.widget_margin=self.widget_margin_showpage
        self.menu.add_vertical_margin(self.margin_main)
        self.menu.add_label("     --Show Rank--     ", max_char=0, selectable=False,font_size=self.font_main)
        self.menu.add_vertical_margin(self.margin_show)
        self.menu.add_button('      Single Easy mode      ', self.Single_the_rank,font_size=self.font_sub)
        self.menu.add_button('      Single Hard mode      ', self.Single_hard_rank, font_size=self.font_sub)
        self.menu.add_button('    Twohands mode   ', self.Twohands_the_rank,font_size=self.font_sub)
        self.menu.add_button('       MiNi mode       ', self.Mini_the_rank,font_size=self.font_sub)
        self.menu.add_button('       Big mode       ', self.Big_the_rank,font_size=self.font_sub)
        self.menu.add_button('           back            ', self.show_list,font_size=self.font_sub)

    # exp,char 변수 보여주기 
    def show_info(self):
        self.menu.clear()
        self.menu.add_label("ID : " , font_size=self.font_sub)
        self.menu.add_label(Var.user_id , font_size=self.font_sub)
        self.menu.add_label("EXP : " , font_size=self.font_sub)
        self.menu.add_label(Var.exp , font_size=self.font_sub)
        self.menu.add_label("CHAR : " , font_size=self.font_sub) 
        self.menu.add_image(Var.lst[Var.char_level - 1][0])

        self.menu.add_button(' back ', self.show_list,font_size=self.font_sub)

    def stop(self):
        Var.click.play()
        self.menu.disable()

    def load_data(self, game_mode): #랭크 점수 데이터 불러오기
        # self.database.__init__()
        # 이렇게 하면 랭크업데이트 되는데 DB에 연결이 너무 많아져서 테스트때는 주석처리하고 제출할 때 주석 풀고 제출
        #불러 오기
        curs = self.database.score_db.cursor(pymysql.cursors.DictCursor)
        if game_mode == 'easy':
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
        return data

    def Single_the_rank(self): #기본 이지 모드 랭크 보는 화면
        self.page='page7'
        Var.click.play()
        self.menu.clear()
        self.mytheme.widget_margin=self.widget_margin_rank
        self.menu.add_vertical_margin(self.margin_main)
        self.menu.add_label("--Single Easy Rank--", selectable=False, font_size=self.font_main)
        self.menu.add_vertical_margin(self.margin_rank)
        self.menu.add_button("       ID       Score", self.Mini_the_rank,font_size=self.font_sub)
        original_data = self.load_data("easy") # 오리지날 모드 데이터 받아오기
        for i in range(Var.rank_max) : #최대 몇명까지 보여줄건지 설정
            original_name=original_data[i]['ID']
            original_score = '{0:>05s}'.format(str(original_data[i]['score']))
            r= "#{} : ".format(i+1) + original_name+"    "+ original_score
            self.menu.add_button(r, self.pass_,font_size=self.font_sub)
        self.menu.add_button('back', self.show_rank,font_size=self.font_sub)


    def Single_hard_rank(self): #기본 하드 모드 랭크 보는 화면
        self.page='page13'
        Var.click.play()
        self.menu.clear()
        self.mytheme.widget_margin=self.widget_margin_rank
        self.menu.add_vertical_margin(self.margin_main)
        self.menu.add_label("--Single Hard Rank--", selectable=False, font_size=self.font_main)
        self.menu.add_vertical_margin(self.margin_rank)
        self.menu.add_button("       ID       Score", self.Mini_the_rank,font_size=self.font_sub)
        hard_data = self.load_data("hard")
        for i in range(Var.rank_max) :
            original_name=hard_data[i]['ID']
            original_score = '{0:>05s}'.format(str(hard_data[i]['score']))
            r= "#{} : ".format(i+1) + original_name+"    "+ original_score
            self.menu.add_button(r, self.pass_,font_size=self.font_sub)
        self.menu.add_button('back', self.show_rank,font_size=self.font_sub)


    def Twohands_the_rank(self):
        self.page='page8'
        Var.click.play()
        self.menu.clear()
        self.mytheme.widget_margin=self.widget_margin_rank
        self.menu.add_vertical_margin(self.margin_main)
        twohadns_data = self.load_data("two")
        self.menu.add_label("--Two Rank--",  selectable=False, font_size=self.font_main)
        self.menu.add_vertical_margin(self.margin_rank)
        self.menu.add_button("       ID       Score", self.pass_,font_size=self.font_sub)
        for i in range(Var.rank_max):
            original_name = twohadns_data[i]['ID']
            original_score = '{0:>05s}'.format(str(twohadns_data[i]['score']))
            r = "#{} : ".format(i+1) + original_name + "    " + original_score
            self.menu.add_button(r, self.pass_, font_size=self.font_sub)
        self.menu.add_button('back', self.show_rank,font_size=self.font_sub)

    def Mini_the_rank(self):
        self.page='page9'
        Var.click.play()
        self.menu.clear()
        self.mytheme.widget_margin=self.widget_margin_rank
        mini_data = self.load_data("mini")
        self.menu.add_vertical_margin(self.margin_main)
        self.menu.add_label("--Mini Rank--", selectable=False, font_size=self.font_main)
        self.menu.add_vertical_margin(self.margin_rank)
        self.menu.add_button("       ID       Score", self.pass_,font_size=self.font_sub)
        for i in range(Var.rank_max):
            original_name = mini_data[i]['ID']
            original_score = '{0:>05s}'.format(str(mini_data[i]['score']))
            r = "#{} : ".format(i+1) + original_name + "    " + original_score
            self.menu.add_button(r, self.pass_, font_size=self.font_sub)
        self.menu.add_button('back', self.show_rank,font_size=self.font_sub)

    def Big_the_rank(self):
        self.page='page10'
        Var.click.play()
        self.menu.clear()
        self.mytheme.widget_margin=self.widget_margin_rank
        big_data = self.load_data("big")
        self.menu.add_vertical_margin(self.margin_main)
        self.menu.add_label("--Big Rank--", selectable=False, font_size=self.font_main)
        self.menu.add_vertical_margin(self.margin_rank)
        self.menu.add_button("       ID       Score", self.pass_,font_size=self.font_sub)
        for i in range(Var.rank_max):
            original_name = big_data[i]['ID']
            original_score = '{0:>05s}'.format(str(big_data[i]['score']))
            r = "#{} : ".format(i+1) + original_name + "    " + original_score
            self.menu.add_button(r, self.pass_, font_size=self.font_sub)
        self.menu.add_button('back', self.show_rank,font_size=self.font_sub)



    def help(self): # help 페이지
        self.page='page11'
        self.surface = pygame.display.set_mode(Var.help_screen)
        self.menu = pygame_menu.Menu(Var.help_h, Var.help_w, '', theme=self.mytheme2)
        self.menu.add_vertical_margin(self.margin_help)
        self.menu.add_button(' back ', self.show_list,font_size=self.font_sub)

    def start_the_game(self): # 클릭시 게임 실행 끝나면 기록 화면 보여주기
        Var.click.play()
        self.Mode = 'basic'
        self.tetris.mode = 'basic'
        self.tetris.run()
        self.menu.clear()
        self.show_game()
        #self.show_score(self.Mode,self.tetris.Score)

    def start_the_hard(self): # 클릭시 게임 실행 끝나면 기록 화면 보여주기
        Var.click.play()
        self.Mode = 'hard'
        self.tetris.mode = 'hard'
        self.tetris.run()
        self.menu.clear()
        self.show_game()
        #self.show_score(self.Mode,self.tetris.Score)

    def start_the_Mini(self):
        Var.click.play()
        self.Mode = 'mini'
        self.tetris.mode='mini'
        self.tetris.run()
        self.menu.clear()
        self.show_game()
        #self.show_score(self.Mode,self.tetris.Score)

    def start_the_Big(self):
        Var.click.play()
        self.Mode = 'big'
        self.tetris.mode='big'
        self.tetris.run()
        self.menu.clear()
        self.show_game()
        #self.show_score(self.Mode,self.tetris.Score)

    def start_the_Twohands(self):
        Var.click.play()
        self.Mode = 'two'
        self.tetris.mode='two'
        self.tetris.run()
        self.menu.clear()
        self.show_game()
        #self.show_score(self.Mode,self.tetris.Score)

    def start_the_Ai(self):
        Var.click.play()
        self.Mode = 'ai'
        self.tetris.mode='ai'
        self.tetris.run()
        self.show_game()


    def pass_(self):
        pass

    # 테마 선택 코드
    def change_theme(self):
        #self.page='page8'
        self.menu.clear()
        #menu = Var.menu_image
        #path = menu.get_path()
        self.menu.add_button('Yami theme',self.theme_base,font_size=self.font_sub)
        self.menu.add_button('Black theme',self.theme_black,font_size=self.font_sub)
        self.menu.add_button('back',self.show_list,font_size=self.font_sub)



    def theme_base(self):
        Var.menu_image = pygame_menu.baseimage.BaseImage(
            image_path='assets/images/야미야미 테마.png',
            drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL	)
        Var.mytheme.background_color = Var.menu_image
        Var.mytheme.widget_font_color=Var.MAIN_VIOLET
        Var.mytheme.widget_font = pygame_menu.font.FONT_NEVIS
        Var.mytheme_help.background_color = pygame_menu.baseimage.BaseImage(
            image_path='assets/images/위젯3.png',
            drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)


    def theme_black(self):
        Var.menu_image = pygame_menu.baseimage.BaseImage(
            image_path='assets/images/main2.png',
            drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL	)
        Var.mytheme.background_color = Var.menu_image
        Var.mytheme.widget_font_color=Var.DARK_GRAY
        Var.mytheme.widget_font = pygame_menu.font.FONT_MUNRO
        Var.mytheme_help.background_color = pygame_menu.baseimage.BaseImage(
            image_path='assets/images/Keyset2.png',
            drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
        #Var.mytheme=pygame_menu.themes.THEME_BLUE.copy
        Var.theme_num=2


    # bgm 선택 코드
    def change_base_bgm(self):
        self.menu.clear()
        self.menu.add_button('BGM 1',self.bgm1,font_size=self.font_sub)
        self.menu.add_button('BGM 2',self.bgm2,font_size=self.font_sub)
        self.menu.add_button('back',self.show_list,font_size=self.font_sub)

    def bgm1(self):
        Var.base_bgm = pygame.mixer.Sound('assets/sounds/base_sound.wav')
        Var.base_bgm.set_volume(0.1)
        Var.select_bgm2 = 0
        Var.select_bgm1 = 1

    def bgm2(self):
        Var.base_bgm2 = pygame.mixer.Sound('assets/sounds/base_sound_2.wav')
        Var.base_bgm2.set_volume(0.1)
        Var.select_bgm1 = 0
        Var.select_bgm2 = 1
