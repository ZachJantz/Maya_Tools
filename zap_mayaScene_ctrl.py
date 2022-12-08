
import dropbox
from dropbox.exceptions import AuthError


DROPBOX_ACCESS_TOKEN = 'v37x9wo4jcur57w'
def dropbox_connect():
    """Create a connection to Dropbox."""

    try:
        dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)
    except AuthError as e:
        print('Error connecting to Dropbox with access token: ' + str(e))
    return dbx
