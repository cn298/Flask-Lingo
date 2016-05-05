import sqlite3

with sqlite3.connect("blog_posts.db") as connection:

	c = connection.cursor()
	c.execute('DROP TABLE words')
	c.execute('CREATE TABLE words(word TEXT, translation TEXT, language TEXT)')

	c.execute('INSERT INTO words VALUES("Bonjour", "Hello", "French")')
	c.execute('INSERT INTO words VALUES("Jambon", "Ham", "French")')
	c.execute('INSERT INTO words VALUES("Fromage", "Cheese", "French")')

print("Created Database!")