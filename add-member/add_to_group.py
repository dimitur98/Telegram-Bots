#!/bin/env python3
import asyncio
from logging import currentframe
from telethon.client import account, telegramclient
from telethon.sync import *
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import FloodWaitError, PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
from scraper import *
import csv
import traceback



SUCCESSFULL_ADDED = "Added"
ALREADY_ADDED = "User is already added"
FLOOD_ERROR = "Too many request, should wait some time"
USER_ACCOUNT_RESTRICTIONS = "The user's privacy settings don't allow to be added"
OTHER_ERROR = "Error has occured"
NO_USERNAME = "User has no username"

class Add_To_Group:
    client_list = {}
    accounts = {}
    current_client = None
    current_phone = None
    current_phone_hash = None
    mode = 1
    already_added_users = []
    skip_added_users = True

    def change_client(self,client = None,deleteClient = False):
        if client == None:
            client = self.current_client

        clients = self.get_clients()
        clientIndex = clients.index(client) + 1

        if deleteClient:
            current_client_index = self.clients.index(client)
            clients.pop(current_client_index)

        if clientIndex > len(clients)-1:
            clientIndex = 0
        self.current_client = clients[clientIndex]
        return clients[clientIndex]
    def load_groups(self,client = None, index = None):
        last_date = None
        chunk_size = 200
        groups = []
        
        if client == None:
            client = self.current_client
        
        result = client(GetDialogsRequest(
            offset_date=last_date,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=chunk_size,
            hash = 0
        ))
        for group in result.chats:
            try:
                 if group.megagroup== True:
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
            group_names[i] = group.title
            i+=1
        return group_names
    def get_clients(self, index = None):
        if(self.accounts == {}):
            return

        key_list = list(self.accounts.keys())

        if index == None:
            return key_list
        else:
            return key_list[index]

    def get_account_groups(self,current_client = False,client = None, client_index = None, group_index = None):
        if(self.accounts == {}):
            return

        key_list = list(self.accounts.keys())
        value_list = list(self.accounts.values())
        output = value_list
        
        if current_client:
            position = key_list.index(self.current_client)
            output = value_list[position]
        elif client != None:
            position = key_list.index(client)
            output = value_list[position]
        elif client_index != None:
            output = value_list[client_index]
        
        if group_index != None:
            output = output[group_index]

        return output
    def client_group_select(self,group_name,groups):
        if groups == []:
            return

        group_names = self.load_group_names(groups)
        key_list = list(group_names.keys())
        val_list = list(group_names.values())
        position = val_list.index(group_name)
        g_index = key_list[position]

        target_group=self.get_account_groups(current_client=True,group_index = g_index)
        # target_group = self.get_account_groups(client = list(self.accounts.keys())[0],group_index=g_index)
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
    def client_initializer(self,api_id, api_hash, phone):
        try:
            client = TelegramClient(phone, api_id, api_hash)
            self.current_client = client
            self.current_phone = phone
        except KeyError:
            #todo
            print("key error")
            return
        client.connect()
        if not client.is_user_authorized():
            self.current_phone_hash = client.send_code_request(phone)
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
        self.already_added_users = Scraper.scrape_members(self.current_client, group, already_added=True)

    async def add_members(self,user, group_name):
        client = self.current_client
        groups = self.get_account_groups(current_client=True)
        target_group_entity = self.client_group_select(group_name, groups)
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
                user_to_add = InputPeerUser(int(user['id']), int(user['access_hash']))
                
            print(1)
            await client(InviteToChannelRequest(target_group_entity,[user_to_add]))
            return SUCCESSFULL_ADDED
        except PeerFloodError as e:
            print("flood")
            # await asyncio.sleep(10)
            return FLOOD_ERROR
        except UserPrivacyRestrictedError:
            print("restr")
            # await asyncio.sleep(10)
            return USER_ACCOUNT_RESTRICTIONS
        except:
            # await asyncio.sleep(10)
            print("asd",traceback.print_exc())
            return OTHER_ERROR

       

