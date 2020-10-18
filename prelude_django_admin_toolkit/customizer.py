

class PreludeAdminCustomizer(object):
    
    def __init__(self, site_header=None):
        self.site_header = site_header
        self.main_menu = []

    def register_menu(self, name, icon=None, to=None, items=None):
        menu_item = {
            'name': name,
            'icon': icon,
            'to': to,
            'items': None
        }
       
        if items is not None: 
            # normalizing menu_items
            normalized_items = [
                {
                    'name': x.get('name', None),
                    'icon': x.get('icon', None),
                    'to': x.get('to', None)
                } for x in items
            ]
            
            menu_item.update({'items': normalized_items})
        
        self.main_menu.append(menu_item)

    def get_context_vars(self):
        return {
            'custom_menu': self.main_menu
        }

    def add_page(self, url, name, handler):
        pass

    def set_index_page(self, handler):
        pass
