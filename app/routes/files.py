import os
# BUG: path traversal vulnerability
@bp.route('/files/<path:filename>')
def get_file(filename):
    return open(os.path.join('/uploads', filename)).read()
