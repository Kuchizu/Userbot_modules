from telethon import events
from .. import loader, utils
import os
import requests
from PIL import Image,ImageFont,ImageDraw 
import re
import io
from textwrap import wrap

def register(cb):
	cb(JacquesemMod())
	
class JacquesemMod(loader.Module):
	"""Хуй кучизу"""
	strings = {
		'name': 'Лолизатор',
		'usage': 'ТАК СЛОЖНО НАПИСАТЬ <code>.help Лолизатор</code> , ДОЛБАЕБ?',
	}
	def __init__(self):
		self.name = self.strings['name']
		self._me = None
		self._ratelimit = []
	async def client_ready(self, client, db):
		self._db = db
		self._client = client
		self.me = await client.get_me()
		
	async def lzcmd(self, message):
		""".lz <реплай на сообщение/свой текст>\nАвтор - @kuchizu :3"""
		
		ufr = requests.get("https://github.com/LaciaMemeFrame/FTG-Modules/blob/master/open-sans.ttf?raw=true")
		f = ufr.content
		
		reply = await message.get_reply_message()
		args = utils.get_args_raw(message)
		if not args:
			if not reply:
				await utils.answer(message, self.strings('usage', message))
				return
			else:
				txt = reply.raw_text
		else:
			txt = utils.get_args_raw(message)
		await message.edit("<b>Лолизируем...</b>")
		pic = requests.get("https://i.ibb.co/Z6Lzw1j/shit.png")
		pic.raw.decode_content = True
		img = Image.open(io.BytesIO(pic.content)).convert("RGB")
 
		W, H = img.size
		#txt = txt.replace("\n", "𓃐")
		text = "\n".join(wrap(txt, 20))
		t = text + "\n"
		#t = t.replace("𓃐","\n")
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype(io.BytesIO(f), 35, encoding='UTF-8')
		w, h = draw.multiline_textsize(t, font=font)
		imtext = Image.new("RGBA", (w+50, h+50), (0, 0,0,0))
		draw = ImageDraw.Draw(imtext)
		draw.multiline_text((40, 40),t,(225,225,225),font=font, align='left')
		imtext.thumbnail((450, 330))
		w, h = 450, 330
		img.paste(imtext, (2,100), imtext)
		out = io.BytesIO()
		out.name = "@kuchizu.jpg"
		img.save(out)
		out.seek(0)
		await message.client.send_file(message.to_id, out, reply_to=reply)
		await message.delete()
