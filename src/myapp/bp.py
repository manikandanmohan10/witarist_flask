from flask.blueprints import Blueprint
from .views import TestView

class TestBlueprint(Blueprint):
    def __init__(self):
        super(TestBlueprint, self).__init__('test', __name__, url_prefix='/test')
        self.add_url_rule('/', view_func=TestView.as_view('test'))