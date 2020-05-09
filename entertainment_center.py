import media_
import fresh_tomatoes


toy_story = media_.Movie("Toy Story (Movie)",
                        "一位男孩與他的玩具們的故事",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=y6s5VXTMv8s")
                         
#print(toy_story.storyline)
avatar = media_.Movie("Avatar (Movie)",
                     "未來世界中，人類為取得另一星球資源，開啟阿凡達計畫",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()

monsters = media_.Movie("Monsters Inc. (Movie)",
                       "兩個怪物的工作就是晚上通過一扇又一扇有特殊功能的門，從怪物的世界進入人類世界中幼童的房間去嚇他們",
                       "http://upload.wikimedia.org/wikipedia/en/6/63/Monsters_Inc.JPG",
                       "https://www.youtube.com/watch?v=FLWO5uyFpNo")
                       
#print(monsters.storyline)
Shrek = media_.Movie("Shrek (Movie)",
                    "在他的沼澤里充滿了魔法生物之後，食人魔同意為小主宰解救公主。為了奪回他的土地",
                   "http://upload.wikimedia.org/wikipedia/en/3/39/Shrek.jpg",
                    "https://www.youtube.com/watch?v=jYejzdBwvY4")
#print(Shrek.storyline)
Sherlock = media_.TvShow("Sherlock (TvShow)",
                        "本劇改編自阿瑟·柯南·道爾爵士家喻戶曉的推理小說，一位脾氣古怪的大偵探在現代倫敦的街頭悄悄巡行，四處搜尋線索。",
                        "https://www.dramaqueen.com.tw/images/video_poster/2016/201612071624439083eeaa03c9a340ff4f6bbd33ca6ea3a5.jpg",
                        "https://www.youtube.com/watch?v=0Dr99aKk8pA",
                        "https://www.netflix.com/tw/title/70202589")

                        
                        



movies = [toy_story,avatar,monsters,Shrek,Sherlock]
fresh_tomatoes.open_movies_page(movies)
#print(media_.Movie.__doc__)



