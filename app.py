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

    if not blog:
        return render_template('404.html', type="error404")


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

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html', type="error404")

if __name__=='__main__':
    app.run(debug=True)