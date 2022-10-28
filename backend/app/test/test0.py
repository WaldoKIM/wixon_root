# 파이썬에서 함수 생성하기
# def 함수_이름() : 실행할 내용

def sirLancelotsFavouriteColour() :
    print("Blue!")
    return '<h1>제목입니다</h1> </br> <div>그냥 의미없는 <strong>파이썬을 이용한 HTML 요소 생성</strong> 테스트 문구</div> <br> <span>그렇다고 이렇게 일일이 HTML을 작성할 수는 없는 노릇인데, <em>어떻게 하면 좋을까요?</em> </span>'


#  <-실행시
# Blue! <-결과값

# 하나의 함수 내에서 두개 이상의 명령 입력시 ; 로 구분

def sirGalahadsFavouriteColour() : print("Blue!"); print("No, Yellow!")

def sirRobinTheNotQuiteSoBraveAsSirLancelot() : print("\nBrave Sir Robin", end="\n \n \n"); print("Bravely bold Sir Robin", end="~ "); print("Rode forth from Camelot.");print("Brave Sir Robin ran away. \n(No, I didn't!)\n"); print("He beat a very brave retreat", end=" -Bravest of the brave, Sir Robin!\n");print("(You're lying", end="!!!)\n\n")

# 마지막 함수에서 사용한 end="" 명령어는 왜인지는 몰라도 QGIS 파이썬 콘솔에서 적용이 안된다.
# end="" 는 문자열 끝에 어떤 행동을 할 지를 설정해 주는 기능이다. 디폴트는 \n, 즉 줄바꿈이다.
# end="" 로 설정하면 print 구문을 여러번 출력시켜도 줄바꿈 없이 한 줄로 붙어 나오게 된다.

def sirRobin() :  print("What is the capital of Assyria?"); print("I don't know that", end=""); print("...Ahhhhhhhh", end="!!! \n")



sirLancelotsFavouriteColour()
sirGalahadsFavouriteColour()
sirRobinTheNotQuiteSoBraveAsSirLancelot() 
sirRobin()
