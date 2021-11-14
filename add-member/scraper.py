from telethon.tl.types import UserStatusRecently
import time

class Scraper:
    scrape_only_recently_active = True
    @staticmethod
    def scrape_members(client, target_group, already_added = False):
        all_participants = client.get_participants(target_group, aggressive=True)
        scraped_members = []
        
        time.sleep(1)
        for user in all_participants:
            # if user.status ==  UserStatusRecently():
                if user.username:
                    username= user.username
                else:
                    username= ""
                if user.first_name:
                    first_name= user.first_name
                else:
                    first_name= ""
                if user.last_name:
                    last_name= user.last_name
                else:
                    last_name= ""
                name= (first_name + ' ' + last_name).strip()
                print("check settings:", Scraper.scrape_only_recently_active)
                if not already_added:
                    print("bfore scrape active")
                    if Scraper.scrape_only_recently_active:
                        print("scrape active")
                        if user.status != UserStatusRecently():
                            continue
                scraped_members.append({"username":username,"id":user.id,"access_hash":user.access_hash,"name":name,"target_group_title":target_group.title,"target_group_id":target_group.id})     
        return scraped_members