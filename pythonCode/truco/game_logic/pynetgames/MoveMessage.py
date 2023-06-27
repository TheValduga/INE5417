#!/usr/bin/python
# -*- coding: UTF-8 -*-
import PyNetgamesServerListener

class MoveMessage(object):
	def to_dict(self):
		"""@ReturnType Dict[str, Any]"""
		pass

	def type(self):
		"""@ReturnType WebHook PayloadType"""
		pass

	def __init__(self):
		self._match_id = None
		"""@AttributeType UUID"""
		self._payload = None
		"""@AttributeType Dict[str, Any]"""
		self._unnamed_PyNetgamesServerListener_ = None
		"""@AttributeType PyNetgamesServerListener
		# @AssociationType PyNetgamesServerListener"""

