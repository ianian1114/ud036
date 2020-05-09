import Video_media
import webbrowser
class Movie(Video_media.Video):
    """ This class provides a way to store movie realted information"""

    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        Video_media.Video.__init__(self,movie_title,movie_storyline,poster_image,trailer_youtube)
        self.TvShow_netflix =""
class TvShow(Video_media.Video):
    
    def __init__(self,TvShow_title,TvShow_storyline,TvShow_image,TvShow_trailer_youtube,TvShow_netflix):
        Video_media.Video.__init__(self,TvShow_title,TvShow_storyline,TvShow_image,TvShow_trailer_youtube)
        self.TvShow_netflix =TvShow_netflix
    
        

        

