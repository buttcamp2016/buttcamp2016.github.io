import os.path
import cherrypy


start ="""<!DOCTYPE html> 
		<html> 
		<head>
		<meta charset="UTF-8">
		<title>Buttcamp 2016</title>
		<link rel="stylesheet" type = "text/css" href="images/stylesheets.css">

		<script type='text/javascript'>
			$(function() {
    		var nav = $('#floatingnav');
    		var navHomeY = nav.offset().top;
    		var isFixed = false;
    		var $w = $(window);
    		$w.scroll(function() {
        		var scrollTop = $w.scrollTop();
        		var shouldBeFixed = scrollTop > navHomeY;
        		if (shouldBeFixed && !isFixed) {
            		nav.css({
                		position: 'fixed',
                		top: 0,
                		left: nav.offset().left,
                		width: nav.width()
            		});
            		isFixed = true;
        		}
        		else if (!shouldBeFixed && isFixed)
        		{
            		nav.css({
                		position: 'static'
            		});
            		isFixed = false;
        		}
    		});
		});
		</script>
	</head>

	<div id="floatingnav" align="center">
		<img src="images/buttcamplogo.png">
		<img src="images/buttcampwords.png">
		<img src="images/buttcamplogo.png">
	</div>

	<body>

		<div id = "main">\n"""



stop ="""
		</div>

		<footer>
		Note: All butt pictures are taken from consenting adults.
		</footer>
		
	</body>
</html>"""

fileurl = '<div class ="butts"> \n<img src="%s">\n</div>\n\n'


class Root:
    @cherrypy.expose
    def index(self):
        import glob
        filenames = glob.glob("images/*.jpg")
        images = ""
        for picture in filenames:
            images += fileurl%(picture)
        return start + images + stop


if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Set up site-wide config first so we get a log if errors occur.
    cherrypy.config.update({'server.socket_host': '0.0.0.0',
                            'server.socket_port': 80, })

    conf = {'/images': {'tools.staticdir.on': True,
                      'tools.staticdir.dir': os.path.join(current_dir, 'images')}
           }

    cherrypy.quickstart(Root(), '/', config=conf)
