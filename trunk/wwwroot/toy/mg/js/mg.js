/*
Sansi Maze
- A maze game based on JavaScript.

Copyright (c) 2008 oldJ, Sansi.Org
Author: oldj.wu@gmail.com
License: LGPL

LastUpdate: 2008-8-16

You can get the last version by SVN:
svn checkout http://sansi.googlecode.com/svn/trunk/ sansi-read-only
*/

// 迷宫类
function MG(ob, w, h) {
	this.ob = document.getElementById(ob);
	this.w = w || 20;
	this.h = h || 20;
	this.gridSize = 20;		// 迷宫格子宽度，暂时没有用
	this.gridStr = "";		// 迷宫的字符串形式，暂时没有用
	this.grids = [];		// 迷宫每个格子的状态，数值为[0, 15]
	this.gridOb = [];		// 迷宫各格子对应的DOM元素
	this.isMoved = false;		// 用户是否按下过方向键
	this.markHistory = false;	// 是否将走过的格子用红色标出
	this.markHistory2 = false;	// 是否标出最短路径，暂时没有用
}

MG.prototype = {
	set: function (sets) {
		// 设置迷宫的宽度与高度
		if (sets.width) this.w = sets.width;
		if (sets.height) this.h = sets.height;
		return this;
	},
	create: function () {
		// 秘生成迷宫
		this.init();
		return this._walk(Math.floor(Math.random() * this.grids.length));
	},
	_walk: function (startPos) {
		// 从startPos开始，遍历地图
		this._walkHistory = [];
		this._walkHistory2 = [];
		var curPos = startPos;
		while (this._getNext0() != -1) {
			// 当还有格子未到达过
			curPos = this._step(curPos);
			if (typeof(curPos) != "number") break;
		}
		return this;
	},
	_getTargetSteps: function (curPos) {
		// 得到当前格子上、下、左、右四个相邻格子中未到达过且可在下一次遍历到达的格子，
		// 可到达写入相应格子的位置，不可到达写入-1
		// 结果以数组形式返回。
		var p = 0,
			a = [];

		// 判断当前格子上方的格子是否可在下一次遍历到达
		p = curPos - this.w;
		if (p > 0 && this.grids[p] == 0 && !this._isRepeating(p))
			a.push(p);
		else
			a.push(-1);

		// 判断当前格子右方的格子是否可在下一次遍历到达
		p = curPos + 1;
		if (p % this.w != 0 && this.grids[p] == 0 && !this._isRepeating(p))
			a.push(p);
		else
			a.push(-1);

		// 判断当前格子下方的格子是否可在下一次遍历到达
		p = curPos + this.w;
		if (p < this.grids.length && this.grids[p] == 0 && !this._isRepeating(p))
			a.push(p);
		else
			a.push(-1);

		// 判断当前格子左方的格子是否可在下一次遍历到达
		p = curPos - 1;
		if (curPos % this.w != 0 && this.grids[p] == 0 && !this._isRepeating(p))
			a.push(p);
		else
			a.push(-1);

		return a;
	},
	_noStep: function () {
		// 判断当前格子是否有可到达的邻格
		for (var i = 0; i < this._targetSteps.length; i ++)
			if (this._targetSteps[i] != -1)
				return false;
		return true;
	},
	_step: function (curPos) {
		// 从当前格子随机行走一步
		this._targetSteps = this._getTargetSteps(curPos);
		if (this._noStep()) {
			// 如果当前格子的所有邻居都无法到达，
			// 返回历史记录中的上一级
			var tmp = this._walkHistory.pop();
			if (typeof(tmp) != "number") return false;
			this._walkHistory2.push(tmp);
			return this._step(tmp);
		}

		var r = Math.floor(Math.random() * 4),
			nextPos;

		while (this._targetSteps[r] == -1) {
			r = Math.floor(Math.random() * 4);
		}
		// 从当前格子可到达的领居中随机选取一个
		nextPos = this._targetSteps[r];

		var isCross = false;
		// 判断当前格子是否与已走过的路线交叉
		if (this.grids[nextPos] != 0)
			isCross = true;

		if (r == 0) {
			// 如果是向上走
			// 当前格子的顶边标记为可通过（标记为1）
			// 下一格子的底边标记为可通过（标记为1）
			this.grids[curPos] ^= 1;
			this.grids[nextPos] ^= 4;
		} else if (r == 1) {
			// 如果是向右走
			// 当前格子的右边标记为可通过（标记为1）
			// 下一格子的左边标记为可通过（标记为1）
			this.grids[curPos] ^= 2;
			this.grids[nextPos] ^= 8;
		} else if (r == 2) {
			// 如果是向下走
			// 当前格子的底边标记为可通过（标记为1）
			// 下一格子的顶边标记为可通过（标记为1）
			this.grids[curPos] ^= 4;
			this.grids[nextPos] ^= 1;
		} else if (r == 3) {
			// 如果是向左走
			// 当前格子的左边标记为可通过（标记为1）
			// 下一格子的右边标记为可通过（标记为1）
			this.grids[curPos] ^= 8;
			this.grids[nextPos] ^= 2;
		}
		// 将当前位置记入历史记录
		this._walkHistory.push(curPos);

		return isCross ? false : nextPos;
	},
	_isRepeating: function (p) {
		// 判断当前格子是否已走过
		for (var i = 0; i < this._walkHistory.length; i ++) {
			if (this._walkHistory[i] == p) return true;
		}
		for (i = 0; i < this._walkHistory2.length; i ++) {
			if (this._walkHistory2[i] == p) return true;
		}
		return false;
	},
	_getNext0: function () {
		// 得到地图上下一个未到达的格子
		for (var i = 0, l = this.grids.length; i <= l; i ++) {
			if (this.grids[i] == 0)
				return i;
		}
		return -1;
	},
	init: function () {
		// 初始化迷宫地图
		this.grids = [];
		this.gridOb = [];
		this.gridStr = "";
		for (var y = 0; y < this.h; y ++)
			for (var x = 0; x < this.w; x ++) {
				//this.grids.push(Math.floor(Math.random() * 16).toString(16));
				this.grids.push(0);
			}
		//this.gridStr = this.grids.join("");
		return this;
	},
	clear: function () {
		// 清除迷宫上的DOM元素
		while (this.ob.childNodes[0])
			this.ob.removeChild(this.ob.childNodes[0]);
		return this;
	},
	show: function () {
		// 将迷宫从数据转化为DOM元素并显示在页面上
		this.clear();
		var tmpOb, v;
		this.ob.style.width = this.gridSize * this.w + 2 + "px";
		this.ob.style.height= this.gridSize * this.h + 2 + "px";
		for (var y = 0; y < this.h; y ++) {
			for (var x = 0; x < this.w; x ++) {
				tmpOb = document.createElement("div");
				tmpOb.setAttribute("class", "grid");
				tmpOb.setAttribute("className", "grid");
				tmpOb.style.width = this.gridSize + "px";
				tmpOb.style.height = this.gridSize + "px";
				tmpOb.style.left = this.gridSize * x + "px";
				tmpOb.style.top = this.gridSize * y + "px";
				//v = parseInt(this.gridStr.substr(y * this.w + x, 1) || "0", 16);
				v = this.grids[y * this.w + x];
				MG.border(tmpOb, v);
				//tmpOb.appendChild(document.createTextNode(v));
				this.gridOb.push(tmpOb);
				this.ob.appendChild(tmpOb);
			}
		}
		tmpOb.setAttribute("class", "grid mg_finish");
		tmpOb.setAttribute("className", "grid mg_finish");
		this.me = new MG_Me(this);
		return this;
	}
};

MG.border = function (ob, v) {
	// MG对象的方法，
	// 根据格子的值显示格子四条边是否可通过
	if (v == 0) {
		ob.style.backgroundColor = "#666";
		return;
	}
	if (v & 1)
		ob.style.borderTop = "solid 1px #f5f5f5";
	if (v & 2)
		ob.style.borderRight = "solid 1px #f5f5f5";
	if (v & 4)
		ob.style.borderBottom = "solid 1px #f5f5f5";
	if (v & 8)
		ob.style.borderLeft = "solid 1px #f5f5f5";
};

// 走迷宫的小人的类
function MG_Me(mg) {
	this.mg = mg || null;
	this.pos = 0;
	this.history = [0];
	this.history2 = [0];
	this.isMoving = false;
	this.lastMove = new Date();
	this.finished = false;
	this.emotions = {
		normal: "img/me.gif",
		happy: "img/me_happy.gif",
		unhappy: "img/me_unhappy.gif",
		surprised: "img/me_surprised.gif",
		tongue: "img/me_tongue.gif"
	};

	if (this.mg) this.init();
}

MG_Me.prototype = {
	init: function () {
		var tmpOb = document.createElement("div"),
			tmpImg = document.createElement("img"),
			tmpInfo = document.createElement("div"),
			tmpSpan = document.createElement("p"),
			_this = this;
		tmpInfo.setAttribute("class", "inform");
		tmpInfo.setAttribute("className", "inform");
		this.informBox = tmpInfo;
		this.informSpan = tmpSpan;
		tmpInfo.appendChild(tmpSpan);
		tmpOb.appendChild(tmpInfo);
		tmpImg.setAttribute("src", "img/me.gif");
		this.meImg = tmpImg;
		tmpOb.setAttribute("class", "me");
		tmpOb.setAttribute("className", "me");
		tmpOb.appendChild(tmpImg);
		tmpOb.style.width = this.mg.gridSize + "px";
		tmpOb.style.height = this.mg.gridSize + "px";
		this.ob = tmpOb;
		this.mg.ob.appendChild(this.ob);

		$.hotkeys.add("up", function () {
			_this.move(0);
		});
		$.hotkeys.add("right", function () {
			_this.move(1);
		});
		$.hotkeys.add("down", function () {
			_this.move(2);
		});
		$.hotkeys.add("left", function () {
			_this.move(3);
		});
		setTimeout(function () {
			if (_this.mg.isMoved) return;
			_this.inform(SANSI_TOY_MSG.keyboardHint);
		}, 3000);

		this.itvl = setInterval(function () {
			if (!_this.mg.isMoved) return;
			var now = new Date();
			if (now - _this.lastMove > 10000) {
				_this.inform(SANSI_TOY_MSG.hello);
				_this.setEmotion("surprised");
			}
		}, 3000);

		this.setMark(1, this.mg.markHistory);
		//this.setMark(2, this.mg.markHistory2);
	},
	move: function (d) {
		if (this.isMoving || this.finished) return;
		this.mg.isMoved = true;
		var v = this.mg.grids[this.pos];
		if (v & Math.pow(2, d)) {
			if (d == 0)
				this.moveTo(this.pos - this.mg.w);
			if (d == 1)
				this.moveTo(this.pos + 1);
			if (d == 2)
				this.moveTo(this.pos + this.mg.w);
			if (d == 3)
				this.moveTo(this.pos - 1);
		}
		this.lastMove = new Date();
	},
	moveTo: function (p) {
		this.isMoving = true;
		this.inform();
		this.setEmotion("normal");
		this.history.unshift(p);
		if (this.mg.markHistory)
			this.mg.gridOb[this.history[0]].style.backgroundColor = "#fcc";
		/*if (this.history2[0] == p) {
			this.history2.shift();
		} else {
			if (this.mg.markHistory2)
				this.mg.gridOb[this.history2[0]].style.backgroundColor = "#f99";
			this.history2.unshift(p);
		}*/
		var x = p % this.mg.w,
			y = Math.floor(p / this.mg.w),
			top = y * this.mg.gridSize + "px",
			left = x * this.mg.gridSize + "px",
			_this = this;

		$(this.ob).animate({
				top: top,
				left: left
			}, 100, "", function () {
				_this.pos = p;
				_this.isMoving = false;
				var v = _this.mg.grids[p];
				if (p == _this.mg.grids.length - 1) {
					_this.inform(SANSI_TOY_MSG.win);
					_this.finished = true;
					_this.setEmotion("happy");
					clearInterval(_this.itvl);
				} else if (p != 0 && (v == 1 || v == 2 || v == 4 || v == 8)) {
					_this.inform(SANSI_TOY_MSG.blindAlley);
					_this.setEmotion("unhappy");
				} else if (p == 0) {
					_this.inform(SANSI_TOY_MSG.backToTheStart);
					_this.setEmotion("surprised");
				}
			});
	},
	inform: function (s) {
		if (s) {
			$(this.informSpan).html(s);
			$(this.informBox).fadeIn(500);
		} else {
			$(this.informBox).fadeOut(500);
		}
	},
	setEmotion: function (em) {
		if (this._emotionStr == em) return;
		if (this.emotions[em]) {
			this.meImg.setAttribute("src", this.emotions[em]);
			this._emotionStr = em;
		}
	},
	setMark: function (h, v) {
		if (h == 1) {
			this.mg.markHistory = v;
			for (var i = 0; i < this.history.length; i ++) {
				this.mg.gridOb[this.history[i]].style.backgroundColor = v ? "#fcc" : "#f5f5f5";
			}
		} else if (h == 2) {
			this.mg.markHistory2 = v;
			for (var i = 0; i < this.history2.length; i ++) {
				this.mg.gridOb[this.history2[i]].style.backgroundColor = v ? "#f99" : "#f5f5f5";
			}
		}
	}
};

