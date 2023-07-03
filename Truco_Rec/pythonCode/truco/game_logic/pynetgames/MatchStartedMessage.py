#!/usr/bin/python
# -*- coding: UTF-8 -*-
import PyNetgamesServerListener

class MatchStartedMessage(object):
	def to_dict(self):
		"""@ReturnType Dict*"""
		pass

	def type(self):
		"""@ReturnType WebhookPayloadType"""
		pass

	def __init__(self):
		self._match_id = None
		"""@AttributeType UUID"""
		self._position = None
		"""@AttributeType int"""
		self._unnamed_PyNetgamesServerListener_ = None
		"""@AttributeType PyNetgamesServerListener
		# @AssociationType PyNetgamesServerListener"""

