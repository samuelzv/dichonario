from django.utils.translation import gettext

def get_i18n_quotes_list(): 
    return {
        'new_quote': gettext('New quote'),
       'next_page': gettext('Go to next page'),
       'previous_page': gettext('Go to previous page'),
       'search': gettext('Search'),
       'page': gettext('Page'),
       'from': gettext('from'),
       'edit': gettext('Edit'),
       'delete': gettext('Delete'),
    }