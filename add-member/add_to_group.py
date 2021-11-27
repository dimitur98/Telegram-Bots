#!/bin/env python3
import asyncio
from logging import currentframe
from telethon import client
from telethon.sync import *
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import  PeerFloodError, UserBannedInChannelError, UserChannelsTooMuchError, UserKickedError, UserNotMutualContactError, UserPrivacyRestrictedError, UsernameNotOccupiedError, UsersTooMuchError
from telethon.tl.functions.channels import InviteToChannelRequest
from scraper import *
import csv
import traceback



SUCCESSFULL_ADDED = "Added."
ALREADY_ADDED = "User is already added."
FLOOD_ERROR = "Too many request, should wait some time."
USER_ACCOUNT_RESTRICTIONS = "The user's privacy settings don't allow to be added."
OTHER_ERROR = "Error has occured."
NO_USERNAME = "User has no username."
CONNECT_ERROR = "Error with connection. Try again after a while or try with other account."
MAX_USERS_EXCEED_ERROR = "The maximum number of users has been exceeded."
USER_BANNED_IN_CHANNEL_ERROR = "You're banned from sending messages in supergroups/channels."
TOO_MANY_CHATS_ERROR = "The user is in too many channels/supergroups."
KICKED_USER_ERROR = "The user was kicked from this supergroup/channel."
NOT_MUTAL_ERROR = "The user is not a mutual contact."
NOT_USED_USERNAME_ERROR = "The username is not in use by anyone else yet." 
ACCOUNT_NOT_PARTICIPATE_IN_GROUP = "Account not participate in the group."

scraper = Scraper()
class Add_To_Group:
    client_list = {}
    accounts = {}
    main_client = None
    current_client = None
    last_added_client = None
    current_phone = None
    current_phone_hash = None
    mode = 1
    already_added_users = []
    skip_added_users = True
    get_megagroups_only = True

    def change_client(self,client = None,deleteClient = False):
        if client == None:
            client = self.current_client
        if self.accounts == {}:
            return

        clients = list(self.accounts.keys())
        clientIndex = clients.index(client) + 1

        if deleteClient:
            current_client_index = self.clients.index(client)
            clients.pop(current_client_index)

        if clientIndex > len(clients)-1:
            clientIndex = 0
        self.current_client = clients[clientIndex]
        return clients[clientIndex]
    async def load_groups(self,client = None, index = None):
        last_date = None
        chunk_size = 200
        groups = []
        
        if client == None:
            client = self.current_client
        
        result = await client(GetDialogsRequest(
            offset_date=last_date,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=chunk_size,
            hash = 0
        ))
        for group in result.chats:
            try:
                groups.append(group)
            except:
                continue
        
        if index == None:
            return groups
        else:
            return groups[index]

    def load_group_names(self,groups):
        i=0
        group_names = {}

        for group in groups:
            try:
                if self.get_megagroups_only:
                        if group.megagroup == False:
                            continue

                group_names[i] = group.title
                i+=1
            except:
                continue

        return group_names
    def get_clients(self, index = None):
        if(self.accounts == {}):
            return

        key_list = list(self.accounts.keys())

        if index == None:
            return key_list
        else:
            return key_list[index]
    def set_main_client(self, phone = None, client = None):
        if phone == None and client == None:
            self.main_client = None
            return
        if phone != None:
            clients = list(self.client_list.keys())
            phones = list(self.client_list.values())
            index = phones.index(phone)
            self.main_client = clients[index]
        elif client != None:
            self.main_client = client
    def is_client_main(self, client):
        if client == self.main_client:
            return True
        else:
            return False
    def get_account_groups(self,current_client = False,main_client = False,client = None, client_index = None, group_index = None):
        if(self.accounts == {}):
            return

        key_list = list(self.accounts.keys())
        value_list = list(self.accounts.values())
        output = value_list
        
        if current_client:
            position = key_list.index(self.current_client)
            output = value_list[position]
        elif main_client:
            position = key_list.index(self.main_client)
            output = value_list[position]
        elif client != None:
            position = key_list.index(client)
            output = value_list[position]
        elif client_index != None:
            output = value_list[client_index]
        
        if self.get_megagroups_only:
            megagroups = []
            for group in output:
                try:
                    if group.megagroup == True:
                        megagroups.append(group)
                except:
                    continue
            output = megagroups
        if group_index != None:
            output = output[group_index]
        return output
    def client_group_select(self,group_name,groups):
        if groups == []:
            return

        group_names = self.load_group_names(groups)
        key_list = list(group_names.keys())
        val_list = list(group_names.values())

        if group_name not in val_list:
            return None

        position = val_list.index(group_name)
        g_index = key_list[position]

        target_group=self.get_account_groups(current_client=True,group_index = g_index)
        return InputPeerChannel(target_group.id,target_group.access_hash)
    async def get_new_instance_of_group(self, group_name):
        last_date = None
        chunk_size = 200
        result = await self.current_client(GetDialogsRequest(
        offset_date=last_date,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=chunk_size,
        hash = 0
        ))
        groups = []
        for chat in result.chats:
            try:
                if chat.megagroup== True:
                    groups.append(chat)
            except:
                continue
        i=0
        group_names = {}
        g_index = 0

        for group in groups:
            group_names[i] = group.title
            i+=1

        key_list = list(group_names.keys())
        val_list = list(group_names.values())
        position = val_list.index(group_name)
        g_index = key_list[position]

        target_group=groups[int(g_index)]
        return InputPeerChannel(target_group.id,target_group.access_hash)
    async def client_initializer(self,api_id, api_hash, phone):
        try:
            client = TelegramClient(phone, api_id, api_hash)

            if self.current_client == None:
                self.current_client = client
            if self.main_client == None:
                self.main_client = client

            self.last_added_client = client
            self.current_phone = phone
       
            await client.connect()
        except:
            print("connect error")
            return CONNECT_ERROR
        if not await client.is_user_authorized():
            self.current_phone_hash = await client.send_code_request(phone)
            return False
        return client

    def read_file(self,input_file):
        members_list = []
        with open(input_file, encoding='UTF-8') as f:
            rows = csv.reader(f,delimiter=",",lineterminator="\n")
            next(rows, None)
            for row in rows:
                user = {}
                user["username"] = row[0]
                user["id"] = int(row[1])
                user["access_hash"] = int(row[2])
                user["name"] = row[3]
                members_list.append(user) 
            return members_list
    def get_already_added_users(self, group):
         loop = asyncio.get_event_loop()
         asyncio.set_event_loop(loop)    
         self.already_added_users =loop.run_until_complete(scraper.scrape_members(self.main_client, group, already_added=True))

    async def add_members(self,user, group_name):
        client = self.current_client
        groups = self.get_account_groups(current_client=True)
        target_group_entity = self.client_group_select(group_name, groups)

        if target_group_entity == None:
            return ACCOUNT_NOT_PARTICIPATE_IN_GROUP

        already_added = False
        user_to_add = None

        try:
            if self.skip_added_users:
                for added_user in self.already_added_users:
                    if user["name"] == added_user["name"]:
                        already_added = True
                        break

                if already_added:
                    return ALREADY_ADDED

            if self.mode == 1:
                if user["username"] == "":
                    return NO_USERNAME
                user_to_add = await client.get_input_entity(user["username"])
            elif self.mode == 2:
                user_to_add = InputPeerUser(user["id"],user["access_hash"])

            await client(InviteToChannelRequest(target_group_entity,[user_to_add]))
            return SUCCESSFULL_ADDED
        except PeerFloodError as e:
            return FLOOD_ERROR
        except UserPrivacyRestrictedError:
            return USER_ACCOUNT_RESTRICTIONS
        except UsersTooMuchError:
            return MAX_USERS_EXCEED_ERROR
        except UserBannedInChannelError:
            return USER_BANNED_IN_CHANNEL_ERROR
        except UserChannelsTooMuchError:
            return TOO_MANY_CHATS_ERROR
        except UserKickedError:
            return KICKED_USER_ERROR
        except UserNotMutualContactError:
            return NOT_MUTAL_ERROR
        except UsernameNotOccupiedError:
            return NOT_USED_USERNAME_ERROR
        except:
            return OTHER_ERROR

       

