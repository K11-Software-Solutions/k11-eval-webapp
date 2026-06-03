from flask import Blueprint, request, render_template
bp = Blueprint('search', __name__)
@bp.route('/search')
def search(): return render_template('search.html', q=request.args.get('q'))
