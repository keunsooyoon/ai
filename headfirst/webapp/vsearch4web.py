from flask import Flask, render_template, request   # 서버 동작에 필요한 flask 모듈 읽어오기
from vsearch import search4letters
app = Flask(__name__)     # Flask 객체 생성하여 app 변수명으로 할당
                          # 객체 생성시 생성자에 __name__파이썬 인터프리터가
                          # 제공하는 값, 현재 활성 모듈의 이름을 가진다. 
# 데코레이터 decorator 장식자 


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = '찾은 결과 입니다.'
    results = str(search4letters(phrase, letters))
    return render_template('results.html',
                            the_phrase = phrase,
                            the_letters= letters,
                            the_title=title,
                            the_results=results,)
@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', 
            the_title='글자 찾기 사이트 방문을 환영합니다. By 홍길동')

if __name__ == '__main__':
    app.run(debug=True)

# 로컬에서 테스트와 개발을 할때는 
# app.run(debug=True) 실행이 되어야하지만
# 웹상에서 배포할때는 실행이되면 안된다. 
# if __name__ == '__main__':
# 웹상에서는 실행을 막게 된다. 
# 계속 지금처럼 로컬에서 웹앱을 개발할수 있도록 한다. 