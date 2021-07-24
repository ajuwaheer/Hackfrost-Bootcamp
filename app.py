from datetime import date
import sqlite3
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

con = sqlite3.connect('database.db')
cur = con.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS blogs (title TEXT, content TEXT, image TEXT, authorName TEXT, authorImage TEXT, dateCreated TEXT)
""")
cur.close()
con.commit()

# blogs = [{
#     "id": 1,
#     "image": "https://images.unsplash.com/photo-1569173112611-52a7cd38bea9?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=634&q=80",
#     "title": "This is a very long title text for blog 1, trying to make it long",
#     "content": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Error laudantium, molestiae numquam quae omnis explicabo ut? Officiis quos accusantium harum. Hello from the other side. This is justa random text, just don't care about this. Look away.",
#     "authorImage": "https://images.unsplash.com/photo-1569173112611-52a7cd38bea9?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=634&q=80",
#     "authorName": "Me",
#     "dateCreated": "21-04-21"
# },
# {"id": 2,
#     "image": "https://images.unsplash.com/photo-1569173112611-52a7cd38bea9?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=634&q=80",
#     "title": "This is a test 2",
#     "content": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Error laudantium, molestiae numquam quae omnis explicabo ut? Officiis quos accusantium harum.",
#     "authorImage": "https://images.unsplash.com/photo-1569173112611-52a7cd38bea9?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=634&q=80",
#     "authorName": "Me",
#     "dateCreated": "21-04-21"
# },
# {"id": 3,
#     "image": "https://images.unsplash.com/photo-1569173112611-52a7cd38bea9?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=634&q=80",
#     "title": "This is a test 3",
#     "content": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Error laudantium, molestiae numquam quae omnis explicabo ut? Officiis quos accusantium harum.",
#     "authorImage": "https://images.unsplash.com/photo-1569173112611-52a7cd38bea9?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=634&q=80",
#     "authorName": "Me",
#     "dateCreated": "21-04-21"
# }]

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', type="home")

@app.route('/blog')
def blog():
    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute('SELECT rowid,* FROM blogs')
    blogs = cur.fetchall()
    cur.close()
    con.commit()

    return render_template('blog.html', type="blog", blogs=blogs)

@app.route('/blog/<int:blog_id>')
def singleblog(blog_id):
    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute(f'SELECT rowid,* FROM blogs WHERE rowid == {blog_id}')
    blog = cur.fetchone()
    cur.close()
    con.commit()

    return render_template('singleblog.html', type="singleblog", blog_id=blog_id, blog=blog)

@app.route('/about')
def about():
    return render_template('about.html', type="about")

@app.route('/contact')
def contact():
    return render_template('contact.html', type="contact", form_id="xayadazg")

@app.route('/createblog', methods = ['POST', 'GET'])
def createblog():
    message = ''

    if request.method == 'POST':
        print('Adding Blog')
        try:
            title = request.form['title']
            content = request.form['content']
            imageLink = request.form['imageLink']
            authorName = request.form['authorName']
            authorImageLink = request.form['authorImageLink']
            dateCreated = date.today()

            con = sqlite3.connect('database.db')
            cur = con.cursor()
            cur.execute("INSERT INTO blogs (title, content, image, authorName, authorImage, dateCreated) VALUES (?,?,?,?,?,?)", (title, content, imageLink, authorName, authorImageLink, dateCreated))
            cur.close()
            con.commit()

            message = 'Blog added successfully.'
            
        except:
            print('Error occured while trying to add blog.')
            message = 'An error occured while trying to add the blog.'

    return render_template('createblog.html', type="createblog", message=message)

if __name__=='__main__':
    app.run(debug=True)