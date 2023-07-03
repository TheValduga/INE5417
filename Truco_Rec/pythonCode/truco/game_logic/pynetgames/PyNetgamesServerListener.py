#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
import PynetgamesServerProxy
import MatchStartedMessage
import MoveMessage

class PyNetgamesServerListener(object):
	__metaclass__ = ABCMeta
	@abstractmethod
	def receive_connection_succes(self):
		"""@ReturnType void"""
		pass

	@abstractmethod
	def receive_match(self, aMatch):
		"""@ParamType aMatch MatchStartedMessage
		@ReturnType void"""
		pass

	@abstractmethod
	def receive_move(self, aReceive_move):
		"""@ParamType aReceive_move MoveMessage
		@ReturnType void"""
		pass

	@abstractmethod
	def receive_error(self, aError):
		"""@ParamType aError Exception
		@ReturnType void"""
		pass

	@abstractmethod
	def receive_disconnect(self):
		"""@ReturnType void"""
		pass

	@classmethod
	def receive_match_requested_success(self):
		"""@ReturnType void"""
		pass

	@classmethod
	def receive_move_sent_success(self):
		"""@ReturnType void"""
		pass

	@classmethod
	def __init__(self):
		self._unnamed_PynetgamesServerProxy_ = None
		"""@AttributeType PynetgamesServerProxy
		# @AssociationType PynetgamesServerProxy"""
		self._unnamed_MatchStartedMessage_ = None
		"""@AttributeType MatchStartedMessage
		# @AssociationType MatchStartedMessage"""
		self._unnamed_MoveMessage_ = None
		"""@AttributeType MoveMessage
		# @AssociationType MoveMessage"""

