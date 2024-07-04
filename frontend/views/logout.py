from flask import redirect
from flask import session
from flask import url_for
from frontend.views import bp


@bp.route('/logout', methods=['GET', 'POST'])
def logout():
    """Logout a User"""
    session.pop('user_logged_in', None)
    return redirect(url_for('bp.home')), 302
