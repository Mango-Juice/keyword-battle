
from flask import Flask, render_template, request, redirect
import google_keyword
import num_to_text

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('hello.html')


@app.route('/result')
def child():
    key1 = request.args.get('keyword1')
    key2 = request.args.get('keyword2')

    if key1 and key2:
        num1 = google_keyword.get_keyword_number(key1)
        num2 = google_keyword.get_keyword_number(key2)
        title = "무승부"
        desc1 = f"{key1}: {num_to_text.ntt(num1)}회"
        desc2 = f"{key2}: {num_to_text.ntt(num2)}회"

        if num1 > num2:
            title = f"{key1} 승리!"
        elif num2 > num1:
            title = f"{key2} 승리!"

        return render_template('result.html', title=title, desc1=desc1, desc2=desc2)

    else:
        return redirect('/')


if __name__ == '__main__':
    app.run()
