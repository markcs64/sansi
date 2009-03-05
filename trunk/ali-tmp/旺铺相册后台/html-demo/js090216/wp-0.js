/* bo 搬家 */

var $Y = YAHOO.util,
	$D = $Y.Dom,
	$E = $Y.Event,
	$  = $D.get,
	Ali = YAHOO.namespace("Ali");


function BTN902(o) {
	this.ob = typeof(o) == "string" ? YAHOO.util.Dom.get(o) : o;
	this.a = YAHOO.util.Dom.getFirstChild(this.ob);
	this.text = this.ob.innerHTML.replace(/<[^>]*?>/g, "");
	this.charLen = this.text.length;
	this.width = 0;
	this.disabled = false;
	this.callback = null;
	this.evtLsner = {};

	this.init();
}

BTN902.prototype.init = function () {
	var bL = document.createElement("b");
	bL.className = "btnL";
	var bR = document.createElement("b");
	bR.className = "btnR";
	this.width = this.charLen * 14 + 45;
	if (YAHOO.env.ua.ie == 6) this.width += 5;
	YAHOO.util.Dom.insertBefore(bL, this.a);
	YAHOO.util.Dom.insertBefore(bR, this.a);
	YAHOO.util.Dom.setStyle(this.ob, "width", this.width + "px");
	YAHOO.util.Event.addListener(this.ob, "mouseover", this.hover, this, true);
	YAHOO.util.Event.addListener(this.ob, "mouseout", this.unhover, this, true);
	YAHOO.util.Event.addListener(this.a, "focus", function () {
		this.blur();
	});
	this.a.onclick = function () {return false;};

	if (YAHOO.util.Dom.hasClass(this.ob, "bo_902btn_disabled"))
		this.disable(1);
};

BTN902.prototype.disable = function (flag) {
	//if (this.disabled == !flag) return;
	this.disabled = !!flag;
	if (this.disabled) {
		YAHOO.util.Dom.addClass(this.ob, "bo_902btn_disabled");
	} else {
		YAHOO.util.Dom.removeClass(this.ob, "bo_902btn_disabled");
	}
};

BTN902.prototype.hover = function () {
	if (this.disabled) return;
	YAHOO.util.Dom.addClass(this.ob, "bo_902btn_hover");
};

BTN902.prototype.unhover = function () {
	YAHOO.util.Dom.removeClass(this.ob, "bo_902btn_hover");
};

BTN902.prototype.on = function (evtName, f) {
	if (!this.evtLsner[evtName]) {
		this.evtLsner[evtName] = [];
		$E.on(this.ob, evtName, function () {
			if (this.disabled) return;
			for (var i = 0; i < this.evtLsner[evtName].length; i ++) {
				this.evtLsner[evtName][i]();
			}
		}, this, true);
	}
	this.evtLsner[evtName].push(f);
};

BTN902.btns = {};
function wp_902btn_init() {
	var btn902s = YAHOO.util.Dom.getElementsByClassName("bo_902btn");
	var nm;
	for (var i = 0; btn902s[i]; i ++) {
		nm = btn902s[i].id || "btn902_" + i;
		BTN902.btns[nm] = new BTN902(btn902s[i]);
	}
}
$E.onDOMReady(wp_902btn_init);

function PullDownMenu_oj(top, ul, ipt, val) {
	this.top = typeof(top) == "string" ? YAHOO.util.Dom.get(top) : top;
	this.ul = typeof(ul) == "string" ? YAHOO.util.Dom.get(ul) : ul;
	this.ipt = typeof(ipt) == "string" ? YAHOO.util.Dom.get(ipt) : ipt;
	this.li = this.ul.getElementsByTagName("li");
	this.val = val;

	this.tmOut = 0;

	this.init();
}

PullDownMenu_oj.prototype.init = function () {
	var _this = this;
	YAHOO.util.Event.on(this.top, "mouseover", this.pullDown, this, true);
	YAHOO.util.Event.on(this.top, "mouseout", this.toPullUp, this, true);
	YAHOO.util.Event.on(this.ul, "mouseover", this.pullDown, this, true);
	YAHOO.util.Event.on(this.ul, "mouseout", this.toPullUp, this, true);
	for (var i = 0; this.li[i]; i ++) {
		YAHOO.util.Event.on(this.li[i], "mouseover", this._liHover);
		YAHOO.util.Event.on(this.li[i], "mouseout", this._liUnHover);
		YAHOO.util.Event.on(this.li[i], "click", function () {
			_this.select(_this, this);
		});
	}
};

PullDownMenu_oj.prototype.pullDown = function () {
	clearTimeout(this.tmOut);
	this.ul.style.display = "block";
};

PullDownMenu_oj.prototype.toPullUp = function () {
	var _this = this;
	this.tmOut = setTimeout(function () {
		_this.pullUp();
	}, 500);
};

PullDownMenu_oj.prototype.pullUp = function () {
	this.ul.style.display = "none";
};

PullDownMenu_oj.prototype._liHover = function () {
	YAHOO.util.Dom.addClass(this, "hover");
};

PullDownMenu_oj.prototype._liUnHover = function () {
	YAHOO.util.Dom.removeClass(this, "hover");
};

PullDownMenu_oj.prototype.select = function (self, target) {
	this.val = target.innerHTML;
	this.top.innerHTML = this.val;
	this.ipt.value = this.val;
	this.pullUp();
};

function MsgBox_oj() {
	this.html = "";
	this.btns = [];
	this.btnsWidth = 0;

	this.init();
}

MsgBox_oj.prototype.init = function () {
	var overlay = document.createElement("div");
	overlay.className = "msgbox_oj_overlay";
	this.overlay = overlay;
	document.getElementsByTagName("body")[0].appendChild(this.overlay);

	var wrapper = document.createElement("div");
	wrapper.className = "msgbox_oj";
	this.wrapper = wrapper;
	var innerWrapper = document.createElement("div");
	innerWrapper.className = "msgbox_oj_innerWrapper";
	this.wrapper.appendChild(innerWrapper);
	this.topBg = mkEl("div", {className: "msgbox_oj_topBg"});
	innerWrapper.appendChild(this.topBg);
	var wrapper2 = document.createElement("div");
	wrapper2.className = "msgbox_oj_inner";
	innerWrapper.appendChild(wrapper2);
	var box = document.createElement("div");
	box.className = "msgbox_oj_box";
	wrapper2.appendChild(box);
	this.wrapper2 = wrapper2;
	this.box = box;
	var close = document.createElement("div");
	close.className = "close";
	this.box.appendChild(close);
	$E.on(close, "click", this.hide, this, true);
	var h2 = document.createElement("h2");
	this.box.appendChild(h2);
	this.head = h2;
	var body = document.createElement("div");
	body.className = "msgbox_oj_body";
	this.box.appendChild(body);
	this.body = body;
	var foot = document.createElement("div");
	foot.className = "msgbox_oj_foot";
	this.box.appendChild(foot);
	this.foot = foot;
	var bottom = document.createElement("div");
	bottom.className = "msgbox_oj_bottom";
	innerWrapper.appendChild(bottom);
	document.getElementsByTagName("body")[0].appendChild(this.wrapper);
	YAHOO.util.Event.on(window, "scroll", this.center, this, true);
	YAHOO.util.Event.on(window, "resize", this.center, this, true);

	/*this.animShow = new YAHOO.util.Anim(this.wrapper, {
		opacity: {from:0, to: 1}
	});

	this.animHide = new YAHOO.util.Anim(this.wrapper, {
		opacity: {to: 0}
	});

	var _this = this;
	this.animHide.onComplete.subscribe(function () {
		YAHOO.util.Dom.setStyle(this.wrapper, "display", "none");
		YAHOO.util.Dom.setStyle(this.wrapper, "opacity", 1);
	});*/
};

MsgBox_oj.prototype.show = function (title, html, btnsAndCallback) {
	this.isShow = true;
	this.head.innerHTML = title || "温馨提示";
	if (typeof(html) == "string") {
		this.body.innerHTML = html|| "无提示信息";
	} else {
		this.body.innerHTML = "";
		this.body.appendChild(html);
	}
	if (!btnsAndCallback) btnsAndCallback = [{text: "确定"}];
	for (var i = 0; btnsAndCallback[i]; i ++) {
		this.mkBtn(btnsAndCallback[i]);
	}

	YAHOO.util.Dom.setStyle(this.foot, "padding-left", (378 - this.btnsWidth) / 2 + "px");
	YAHOO.util.Dom.setStyle(this.overlay, "width", YAHOO.util.Dom.getDocumentWidth() + "px");
	YAHOO.util.Dom.setStyle(this.overlay, "height", YAHOO.util.Dom.getDocumentHeight() + "px");
	YAHOO.util.Dom.setStyle(this.overlay, "top", 0);
	YAHOO.util.Dom.setStyle(this.overlay, "left", 0);
	YAHOO.util.Dom.setStyle(this.overlay, "opacity", 0);

	YAHOO.util.Dom.setStyle(this.overlay, "display", "block");
	YAHOO.util.Dom.setStyle(this.wrapper, "display", "block");
	this.chkBg();
	this.center();
	//this.animShow.animate();
};

MsgBox_oj.prototype.chkBg = function () {
	if (!this.isShow) return;
	var _this = this;
	$D.setStyle(this.topBg, "height", this.wrapper2.offsetHeight + "px");
	setTimeout(function () {
		_this.chkBg();
	}, 50);
};

MsgBox_oj.prototype.center = function () {
	YAHOO.util.Dom.setStyle(this.wrapper, "left", (YAHOO.util.Dom.getClientWidth() - 422) / 2 + "px");
	YAHOO.util.Dom.setStyle(this.wrapper, "top", YAHOO.util.Dom.getDocumentScrollTop() + (YAHOO.util.Dom.getClientHeight() - this.wrapper.offsetHeight) / 2 + "px");
};

MsgBox_oj.prototype.hide = function () {
	//this.animHide.animate();
	YAHOO.util.Dom.setStyle(this.wrapper, "display", "none");
	YAHOO.util.Dom.setStyle(this.overlay, "display", "none");
	this.btns = [];
	this.btnsWidth = 0;
	this.foot.innerHTML = "";
	this.isShow = false;
};

MsgBox_oj.prototype.mkBtn = function (btnObj) {
	var btn = document.createElement("div");
	if (!btnObj.disabled) {
		btn.className = "bo_902btn";
	} else {
		btn.className = "bo_902btn bo_902btn_disabled";
	}
	var a = document.createElement("a");
	a.appendChild(document.createTextNode(btnObj.text || "按钮"));
	btn.appendChild(a);
	var oBtn = new BTN902(btn);
	YAHOO.util.Event.on(btn, "click", function () {
		oBtn.callback = btnObj.callback;
		var _callback_result = true;
		if (!oBtn.disabled && oBtn.callback && typeof(oBtn.callback) == "function") {
			_callback_result = oBtn.callback();
		}
		if (!oBtn.disabled && _callback_result != "__blocked__")
			this.hide();
	}, this, true);
	this.btns.push(oBtn);
	this.foot.appendChild(oBtn.ob);
	this.btnsWidth += oBtn.width;
};

function mkEl(tagName, p) {
	var o = document.createElement(tagName);
	if (p) {
		for (var k in p) {
			if (k != "class")
				o[k] = p[k];
			else
				o.className = p[k];
		}
	}
	return o;
}

function g_imgMaxSize(img, maxWidth, maxHeight) {
	if (!img) return;
	var w = parseInt(img.width),
		h = parseInt(img.height);
	
	if (w == h) {
		w = maxWidth;
		h = maxHeight;
	} else if (w > h) {
		h = Math.floor(h * maxWidth / w);
		w = maxWidth;
	} else {
		w = Math.floor(w * maxHeight / h);
		h = maxHeight;
	}
	$D.setStyle(img, "width", w + "px");
	$D.setStyle(img, "height", h + "px");
	return [w, h];
}

(function () {
	var oj = function (p) {
		return new oj.cls(p);
	};
	
	oj.$ = function (p) { return document.getElementById(p); };
	
	oj.cls = function (p) {
		this.items = [];
		if (typeof(p) == "string") {
			this.items.push(oj.$(p));
		} else if (typeof(p) == "object" && typeof(p.length) == "number") {
			for (var i = 0, l = p.length; i < l; i ++)
				this.items.push(p[i]);
		} else if (typeof(p) == "object") {
			for (var k in p)
				this.items.push(p[k]);
		} else {
			this.items.push(p);
		}
	};
	
	oj.cls.prototype = {
		each: function (f) {
			var args = [];
			for (var i = 1, l = arguments.length; i < l; i ++) {
				args.push(arguments[i]);
			}
			for (i = 0, l = this.items.length; i < l; i ++) {
				f.apply(this.items[i], args);
			}
			return this;
		}
	}
	
	$J = oj;
})();
