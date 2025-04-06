#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 09:38:19 2025

@author: alon
"""
class PostOffice:
    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}
        
    def send_message(self, sender, recipient, message_body, urgent=False):
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
            'read': False,  # שדה חדש שמסמן אם ההודעה נקראה
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username, num_messages=None):
        """
        מקבלת שם משתמש ומספר הודעות לקריאה.
        מחזירה את ההודעות הראשונות בתיבת הדואר הנכנס של המשתמש ומסמנת אותן כנקראו.
        אם לא הועבר מספר הודעות, מחזירה את כל ההודעות בתיבה.
        """
        inbox = self.boxes[username]
        
        # אם לא צוין מספר ההודעות, נקרא את כל ההודעות
        messages_to_read = inbox[:num_messages] if num_messages is not None else inbox
        
        # סימון ההודעות כנקראו
        for message in messages_to_read:
            message['read'] = True
        
        # מחזירים את ההודעות שנקראו
        return messages_to_read

    def search_inbox(self, username, search_str):
        """
        מחפשת בתיבת הדואר הנכנס של המשתמש את כל ההודעות שמכילות את המחרוזת שנמסרה
        (בכותרת או בגוף ההודעה).
        """
        inbox = self.boxes[username]
        
        # מחפשים את המחרוזת בגוף ההודעה או בכותרת (לפי הצורך)
        return [message for message in inbox if search_str in message['body']]

def main():
# דוגמת שימוש
    post_office = PostOffice(['john', 'sarah', 'emma'])
    
    # שליחת הודעות
    post_office.send_message('john', 'sarah', 'Hello Sarah, are you available for a meeting tomorrow?')
    post_office.send_message('emma', 'john', 'Reminder: Don\'t forget to submit the report by Friday.', urgent=True)
    post_office.send_message('sarah', 'emma', 'Re: Meeting - Let\'s catch up next week!')
    
    # קריאת הודעות
    print(post_office.read_inbox('john'))  # מחזיר את כל ההודעות בתיבת הדואר של ג'ון
    
    # חיפוש הודעות
    print(post_office.search_inbox('sarah', 'meeting'))  # מחפש הודעות בתיבת הדואר של סארה שמכילות את המילה "meeting"

if(__name__=="__main__"):
    main()