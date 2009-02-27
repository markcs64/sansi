/*
Copyright (c) 2009, Qiuhua. All rights reserved.
Portions Copyright (c) 2009, Alibaba, Inc. All rights reserved.
Code licensed under the BSD License:
http://www.bubbling-library.com/eng/licence
version: 0.1
*/
									  
function log(something){	try { console.log(something); } catch(e) {}; };
function info(something){   try { console.info(something);} catch(e) {}; };


	/**
	* @singleton WizardManager - Use this object to management your wizards...
	* Apply dynamic functionality to a wizard widget
	* @constructor
	*/
    AliUploader = function(id, att) {	
		
		function event_handler(target, evt) {
			var uploader = document.getElementById(target).owner;
			info(evt.type);
			try { uploader[evt.type](evt); } catch(e) {};
		};
		
		function  initlize(_this) {
			
			var flashvars = {};
			var params = {};
			var attributes = {};
			
			var dom, insertDom;
			dom = document.getElementById(id);
			dom.innerHTML = "";
			insertDom = document.createElement("div")
			id = insertDom.id = _this.container_id+"_swf";
			insertDom.obj = _this;
			dom.appendChild(insertDom);
			
			if(!_this.buttonSkin) {
				//使用外部的图片做按钮skin
				dom.style.position = "relative";
				insertDom.style.position = "absolute";
				insertDom.style.left = "0";
				insertDom.style.top = "0";
			}else{
				//透明方式，按钮的文字中HTML内，flash透明
				flashvars.buttonSkin = _this.buttonSkin;
			}
			
			// 如果没有指定flash的大小，算出flash的尺寸，默认是父对象的100%大小
			var w = _this.width;
			var h = _this.height;
			if(w<=0)
				w = insertDom.width = dom.offsetWidth;
			if(h<=0)
				h = insertDom.height = dom.offsetHeight;
			
			attributes.name = attributes.id = id;
			attributes.width = w;
			attributes.height = h;
			attributes.data = _this.swfURL;
			params.wmode = "transparent";
			flashvars.eventHandler = event_handler;
			flashvars.elementID = id;
			
			
			var str_fv = "";			
			for (var i in flashvars) {
				if (flashvars[i] != Object.prototype[i]) { // Filter out prototype additions from other potential libraries
					str_fv += "&" + i + "=" + flashvars[i];
				}
			}
			params.flashvars = str_fv;
			
			//insert flash
			var swf = swfobject.createSWF( attributes, params, _this.container_id );
			swf.owner = _this;
			_this.swf = swf;
		}
		
		this.container_id = id;
		for(var each in att){
			this[each] = att[each];
		}
		
		initlize(this);
	};
	
	AliUploader.prototype = (function(){
		// events:
		
		function onFlashReady(_this){
			_this.setAllowMultipleFiles(_this.allowMulti);
		};
				
		
		return {
		
		// 一些参数的默认值
		fileList:	[],			// 保存文件列表的变量
		simLimit:	3,			// 同时上传的文件数目
		url:		null,		// 上传到远程的地址
		method:		"POST",		// 数据发送方式
		allowMulti:	true,		// 允许多选
		swfURL:		"assets/aliuploader.swf",	//flash所在的目录
		buttonSkin:	null,		// 按钮皮肤
		width:		-1,			// 宽度， -1表示与父对象一致
		height:		-1,			// 高度， -1表示与父对象一致
		vars:		{},			// 传输到服务器的额外变量
		fieldName:	"FileData",	// 传输到服务器时，文件内容在form中的字段名称
		fileLimit:	0,			// 单个文件的大小限制（KB）
		totalLimit:	0,			// 上传的大小总和限制（KB）
		
		
		/*
		*
		* API 列表
		* -------------------------
		
		// setAllowLogging ( true | false )
		// 设置是不是由flash发送测试
		
		// setAllowMultipleFiles ( true |false )
		// 设置是否允许多选 	
		
		// removeFile (fileID:String = null) 
		// 在上传队列中删除一个文件
		
		// clearFileList (): Boolean
		// 清空上传队列
		
		// upload(fileID:String, url:String, method:String = "GET", vars:Object = null, fieldName:String = "Filedata")
		// 上传单个文件，可以设定各个上传参数
		
		// uploadAll()
		// 上传全部文件
		
		// cancel (fileID:String = null) 		
		// 取消指定的上传文件
		
		// setSimUploadLimit(simUpload:int = [2,5])		
		// 设置同时进行上传的文件数
		
		// setFileFilters(fileFilters:Array)
		// 设置选择文件的过滤器
		
		// enable()
		// 启用Flash选择文件UI
		
		// disable()
		// 禁用Flash选择文件UI
		*/
		
		setAllowLogging: function(b){ try { this.swf.setAllowLogging(b); } catch(e) {} },		
		
		setAllowMultipleFiles: function(b){ try { this.swf.setAllowMultipleFiles(b);} catch(e) {} },
		
		removeFile: function(fileID){ try { this.swf.removeFile(fileID); } catch(e) {} },
		
		clearFileList: function(){ try { this.swf.clearFileList(); } catch(e) {} },
		
		upload: function(fileID){ try { this.swf.upload(fileID, this.url, this.method, this.vars, this.fileName); } catch(e) {} },
		
		uploadAll: function(){ try { this.swf.uploadAll(this.url, this.method, this.vars, this.fieldName); } catch(e) {} },
		
		
		cancel: function(fileID) { try { this.swf.cancel(fileID); } catch(e) {} },
		
		
		setSimUploadLimit: function(n) { try { this.swf.setSimUploadLimit(n); } catch(e) {} },
		
		setFileFilters: function(arr)  { try { this.swf.setFileFilters(arr); } catch(e) {} },
		
		enable: function() { try { this.swf.enable();} catch(e) {} },
		
		disable: function() { try { this.swf.disable(); } catch(e) {} },
		
		
		
		/*
		*
		*  Events 
		* -------------------------			
		// swfReady					flash主引擎加载完毕
		// buttonReady				按钮模式下，按钮载入完成
		// mouseDown				[透明模式] 鼠标按下动作
		// mouseUp					[透明模式] 鼠标松开
		// rollOver					[透明模式] 鼠标移到flash上	
		// rollOut					[透明模式] 鼠标移出flash
		// click					[透明模式] 鼠标点击
		// fileSelect				选择了一个或多个文件
		// fileRefused				用户选择的一个或多个文件拒绝被加入上传队列
		// uploadStart				（某文件）上传开始
		// uploadProgress			上传进度
		// uploadComplete			（某文件）上传完成
		// uploadCompleteData		（某文件）上传完成后收到服务器返回消息
		// uploadError				（某文件）上传不成功
		// uploadCancel				（某文件）上传被取消
		// finish					上传全部完成
		
		*/
		
		swfReady: function($){			
			if(typeof($)=="function") this.swfReady_handler = $;
			else {
				onFlashReady(this);
				try { this.swfReady_handler($); } catch(e) {};
			}
			return this;
		},
		
		
		buttonReady: function($){		
			if(typeof($)=="function") this.btnReady_handler = $;
			else {
				try { this.btnReady_handler($); } catch(e) {};
			}
			return this;
		},
		
		
		mouseDown: function($){	
			if(typeof($)=="function") this.msdown_handler = $;
			else {
				try { this.msdown_handler($); } catch(e) {};
			}
			return this;},
			
		
		mouseUp: function($){
			if(typeof($)=="function") this.msup_handler = $;
			else {
				try { this.msup_handler($); } catch(e) {};
			}
			return this;},
			
		
		rollOver: function($){
			if(typeof($)=="function") this.rollover_handler = $;
			else {
				try { this.rollover_handler($); } catch(e) {};
			}
			return this;},
		
		rollOut: function($){
			if(typeof($)=="function") this.rollout_handler = $;
			else {	try { this.rollout_handler($); } catch(e) {}; }
			return this;
		},
		
		
		click: function($){
			if(typeof($)=="function") this.click_handler = $;
			else {	try { this.click_handler($); } catch(e) {}; }
			return this;
		},
		
		
		uploadStart: function($){
			if(typeof($)=="function") this.uploadStart_handler = $;
			else {	try { this.uploadStart_handler($); } catch(e) {}; }
			return this;
		},
		
		
		uploadProgress: function($){
			if(typeof($)=="function") this.uploadProgress_handler = $;
			else {	try { this.uploadProgress_handler($); } catch(e) {}; }
			return this;
		},
		
		
		uploadComplete: function($){
			if(typeof($)=="function") this.uploadComplete_handler = $;
			else {	try { this.uploadComplete_handler($); } catch(e) {}; }
			return this;
		},
		
		uploadCompleteData: function($) {
			if(typeof($)=="function") this.uploadCompleteData_handler = $;
			else {	try { this.uploadCompleteData_handler($); } catch(e) {}; }
			return this;
		},
		
		uploadError: function($){
			if(typeof($)=="function") this.uploadError_handler = $;
			else {	try { this.uploadError_handler($); } catch(e) {}; }
			return this;
		},
		
		uploadCancel: function($){
			if(typeof($)=="function") this.uploadCancel_handler = $;
			else {	try { this.uploadCancel_handler($); } catch(e) {}; }
			return this;
		},
		
		fileSelect: function($){		
			if(typeof($)=="function") this.fileSelect_handler = $;
			else {
				try { this.fileSelect_handler($); } catch(e) {};
			}
			return this;
		},
		
		finish: function($){
			if(typeof($)=="function") this.rollout_handler = $;
			else {	try { this.rollout_handler($); } catch(e) {}; }
			return this;
		}
		
		
	};
	
	})();
