import asyncio
from db import *
from telethon.errors.rpcerrorlist import ChannelPrivateError, ChatAdminRequiredError
from telethon.tl.types import  UserStatusRecently
import time
CHANNEL_PRIVATE_ERROR = "This channel is private and you lack permission to access it or you are banned."
ADMIN_REQUIRED_ERROR = "This channel is private and you lack permission to access it or you are banned."
TIMEOUT_ERROR = "A timeout occurred while fetching data from the worker."
ERROR = "Error has occured."

db = Db()
class Scraper:
    async def scrape_members(self, client, target_group, already_added = False):
        settings = db.get_all_settings()[0]

        try:
            all_participants = await client.get_participants(target_group, aggressive=True)
            scraped_members = []

            await asyncio.sleep(1)
            for user in all_participants:
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

                    if not already_added:
                        if settings["scrape_active_users"]:
                            if user.status != UserStatusRecently():
                                continue
                    
                    scraped_members.append({"username":username,"id":user.id,"access_hash":user.access_hash,"name":name,"target_group_title":target_group.title,"target_group_id":target_group.id})     
            return scraped_members
        except ChannelPrivateError:
            return CHANNEL_PRIVATE_ERROR
        except ChatAdminRequiredError:
            return ADMIN_REQUIRED_ERROR
        except TimeoutError:
            return TIMEOUT_ERROR
        except:
            return ERROR