/* 相册后台 */


function formatDT(dt) {
	//把时间格式化为 "2009-2-18" 这样的格式
	//返回字符串
	
	return dt.getFullYear() + "-" + (dt.getMonth() + 1) + "-" + dt.getDay();
}

function WP_Album (ob, i) {
	if (!ob) ob = {};
	this.i = typeof(i) == "number" ? i : -1;
	this.id = ob.id || "";
	this.ob = null;
	this.title = ob.title || "";
	this.count = parseInt(ob.count) || 0;
	this.lock = ob.lock || 0;
	this.datetime = ob.datetime || new Date();
	this.datetime2 = formatDT(this.datetime);
	this.cover = ob.cover || "";
	this.state = "";

	this.init();
};

WP_Album.prototype = {
	init: function () {
		this.ob = mkEl("div", {className: "album"});
		this._ob_state = mkEl("div", {className: "wrapper normal"});
		this.ob.appendChild(this._ob_state);
		var tmp = mkEl("div", {className: "hook"});
		this._ob_state.appendChild(tmp);
		this._ob_cover = mkEl("div", {className: "cover"});
		this._ob_state.appendChild(this._ob_cover);
		this._ob_cover_img = mkEl("img", {src: this.cover});
		tmp = mkEl("div", {className: "cover-img"});
		tmp.appendChild(this._ob_cover_img);
		if (this.cover == "") $D.addClass(tmp, "no-photo");
		this._ob_cover.appendChild(tmp);
		tmp = mkEl("div", {className: "info"});
		this._ob_title = mkEl("span", {className: "title"});
		var _title = this.title;
		if (_title.length > 7) _title = _title.substring(0, 7) + "..";
		this._ob_title.appendChild(document.createTextNode(_title));
		this._ob_count = mkEl("span", {className: "count"});
		this._ob_count.appendChild(document.createTextNode("(" + this.count + ")"));
		tmp.appendChild(this._ob_title);
		tmp.appendChild(this._ob_count);
		this._ob_state.appendChild(tmp);
		tmp = mkEl("div", {className: "info"});
		this._ob_datetime = mkEl("span", {className: "datetime"});
		this._ob_datetime.appendChild(document.createTextNode(this.datetime2));
		tmp.appendChild(this._ob_datetime);
		if (this.lock) {
			this._ob_lock = mkEl("span", {className: "lock"});
			this._ob_lock.appendChild(document.createTextNode("密码访问"));
			tmp.appendChild(this._ob_lock);
		}
		this._ob_state.appendChild(tmp);

		$E.on(this.ob, "mouseover", this._bind(this.hover));
		$E.on(this.ob, "mouseout", this._bind(this.unhover));
		$E.on(this.ob, "click", this._bind(this.select));
		$E.on(this._ob_cover_img, "load", this._bind(this.resizeCover));
	},
	_bind: function (f) {
		var _this = this, args = [];
		for (var i = 1; i < arguments.length; i ++) {
			args.push(arguments[i]);
		}
		return function () {
			f.apply(_this, args);
		};
	},
	resizeCover: function () {
		var w = this._ob_cover_img.width,
			h = this._ob_cover_img.height;

		if (w >= h) {
			h = Math.floor(h * 100 / w);
			$D.setStyle(this._ob_cover_img, "width", "100px");
			$D.setStyle(this._ob_cover_img, "height", h + "px");
			$D.setStyle(this._ob_cover_img, "margin-top", Math.floor(62.5 - h / 2) + "px");
		} else {
			$D.setStyle(this._ob_cover_img, "width", Math.floor(w * 100 / h) + "px");
			$D.setStyle(this._ob_cover_img, "height", "100px");
			$D.setStyle(this._ob_cover_img, "margin-top", "12px");
		}
	},
	hover: function () {
		if (this.state == "selected") return;
		this._chgState("hover");
	},
	unhover: function () {
		if (this.state == "selected") return;
		this._chgState("normal");
	},
	select: function () {
		WP_Album.select(this);
		this._chgState("selected");
	},
	unselect: function () {
		this._chgState("normal");
	},
	del: function () {

	},
	_chgState: function (flag) {
		this.state = flag;
		this._ob_state.className = "wrapper " + flag;
	}
};

WP_Album._msgbox = null;
WP_Album.msgBox = function (title, params, html) {
	//相册对话框
	var btns = [
		{
			text: "创建",
			disabled: true,
			callback: function () {
				var title = $("frm_albumTitle").value,
					pswd = $("frm_albumPswd").value,
					pswd2 = $("frm_albumPswd2").value;

				if ($("frm_albumLocked").checked) {
					if (pswd != pswd2) {
						alert("两次输入的密码不一致！");
						return "__blocked__";
					}
				}

				alert(1);
			}
		},
		{
			text: "取消"
		}
	];
	if (params.action != "create") {
		btns[0].text = "确定";
		btns[0].disabled = false;
	}

	WP_Album._msgbox.show(title, html, btns);
};

WP_Album.curSelect = null;		//当前选中相册
WP_Album.items = [];

WP_Album.init = function (a) {
	if (!a) return;
	for (var i = 0; i < a.length; i ++) {
		WP_Album.items.push(new WP_Album(a[i], i));
	}
};

WP_Album.show = function (p_ob) {
	//显示相册
	var p = typeof(p_ob) == "string" ? $(p_ob) : p_ob;
	for (var i = 0; WP_Album.items[i]; i ++) {
		p.appendChild(WP_Album.items[i].ob);
	}
};

WP_Album.each = function (f) {
	var args = [];
	for (var i = 1; i < arguments.length; i ++) {
		args.push(arguments[i]);
	}
	for (i = 0; WP_Album.items[i]; i ++) {
		f.apply(WP_Album.items[i], args);
	}
};

WP_Album.on = function (action, f) {
	if (!WP_Album["on" + action] || WP_Album["on" + action].constructor != Array) {
		WP_Album["on" + action] = [];
	}
	WP_Album["on" + action].push(f);
};

WP_Album.onselect = [];
WP_Album.select = function (album) {
	WP_Album.each(function () {
		this.unselect();
	});
	WP_Album.curSelect = album;

	for (var i = 0; WP_Album.onselect[i]; i ++)
		WP_Album.onselect[i]();
};

$E.onDOMReady(function () {
	WP_Album._msgbox = new MsgBox_oj();
});
