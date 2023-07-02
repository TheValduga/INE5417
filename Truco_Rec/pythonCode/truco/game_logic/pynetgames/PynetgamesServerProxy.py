#!/usr/bin/python
# -*- coding: UTF-8 -*-
import PyNetgamesServerListener

class PynetgamesServerProxy(object):
	def add_listener(self, aListener):
		"""@ParamType aListener tkinter_client.PynetgamesServerListener
		@ReturnType void"""
		pass

	def send_connect(self, aAddres = localhost:8765):
		"""@ParamType aAddres string
		@ReturnType void"""
		pass

	def send_match(self, aAmount_of_players):
		"""@ParamType aAmount_of_players int
		@ReturnType void"""
		pass

	def send_move(self, aMatch_id, aPayload):
		"""@ParamType aMatch_id UUID
		@ParamType aPayload Dict [str, Any]
		@ReturnType void"""
		pass

	def send_disconnect(self):
		pass

	def __init__(self):
		self._unnamed_PyNetgamesServerListener_ = []
		"""@AttributeType PyNetgamesServerListener*
		# @AssociationType PyNetgamesServerListener[]
		# @AssociationMultiplicity *
		# @AssociationKind Aggregation"""

