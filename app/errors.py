from flask import render_template
def not_found(e): return render_template('404.html'), 404
