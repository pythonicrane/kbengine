# -*- coding: utf-8 -*-
import KBEngine
import kbesystem
from KBEDebug import *

def onInit(isReload):
	"""
	KBEngine method.
	当引擎启动后初始化完所有的脚本后这个接口被调用
	@param isReload: 是否是被重写加载脚本后触发的
	@type isReload: bool
	"""
	DEBUG_MSG('onInit::isReload = %s' % isReload)

def onStart():
	"""
	KBEngine method.
	在onInitialize调用之后， 准备开始游戏时引擎调用这个接口.
	"""
	pass
	
def onFinish():
	"""
	KBEngine method.
	客户端将要关闭时， 引擎调用这个接口
	可以在此做一些游戏资源清理工作
	"""
	pass

def onTargetChanged(entityID):
	"""
	KBEngine method.
	客户端选择了某个目标
	"""
	# DEBUG_MSG('onTargetChanged:: entityID = %i' % entityID)
	kbesystem.targetMgr.setTargetID(entityID)
	
def kbengine_onEvent(eventID, args):
	"""
	KBEngine method.
	app发出的事件
	@param args: 自行约定
	"""
	DEBUG_MSG('kbengine_onEvent:: eventID = %s, args=%s' % (str(eventID), str(args)))
	
	if eventID == "reset":
		kbesystem.eventMgr.fire("reset", 0)
	elif eventID == "relive":
		if KBEngine.player() != None:
			KBEngine.player().relive()