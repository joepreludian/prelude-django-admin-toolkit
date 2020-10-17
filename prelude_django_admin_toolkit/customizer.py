

class PreludeAdminCustomizer(object):

    def __init__(self, site_header=None):
        self.site_header = site_header

    def populate_menu(self, name, items=None):
        pass

    def add_page(self, url, name, handler):
        pass

    def set_index_page(self, handler):
        pass
