from flask import Blueprint, make_response
bp = Blueprint('sitemap', __name__)
@bp.route('/sitemap.xml')
def sitemap(): return make_response('<?xml version="1.0"?><urlset></urlset>', 200)
