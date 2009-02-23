// cls_gotoPage.js

function WP_GotoPage(ob, curPage, pageCount, callback) {
	this.ob = (typeof(ob) == "string") ? $(ob) : ob;
	this.curPage = curPage || 1;
	this.pageCount = pageCount || 1;
	this.obs = {};
	this.callback = callback;

	this.tm = 0;

	WP_GotoPage.items.push(this);
	this.init();
}

WP_GotoPage.prototype = {
	init: function () {
		var _this = this;
		var tmp = mkEl("div", {className: "wp-gotopage-pre"});
		tmp.appendChild(document.createTextNode("上一页"));
		if (this.curPage == 1) $D.addClass(tmp, "disabled");
		$E.on(tmp, "click", this.gotoPrePage, this, true);
		this.obs.lnkPrePage = tmp;
		this.ob.appendChild(tmp);
		tmp = mkEl("div", {className: "wp-gotopage-some"});
		var tmp2 = mkEl("div", {className: "wp-gotopage-cur"});
		this.obs.somePage = tmp;
		this.obs.curPage = tmp2;
		tmp2.appendChild(document.createTextNode(this.curPage + "/" + this.pageCount));
		$E.on(tmp2, "mouseover", this.showPages, this, true);
		$E.on(tmp2, "mouseout", this.hidePages, this, true);
		tmp.appendChild(tmp2);
		tmp2 = mkEl("ul", {className: "wp-gotopage-pages"});
		$E.on(tmp2, "mouseout", this.hidePages, this, true);
		this.obs.pages = tmp2;
		var li;
		for (var i = 1; i <= this.pageCount; i ++) {
			li = document.createElement("li");
			if (this.curPage == i)
				li.className = "selected";
			li.appendChild(document.createTextNode(i));
			$E.on(li, "mouseout", function () {
				_this.pageUnhover(this);
			});
			$E.on(li, "mouseover", function () {
				_this.pageHover(this);
			});
			$E.on(li, "click", function () {
				_this.pageSelect(this);
			});
			tmp2.appendChild(li);
		}
		tmp.appendChild(tmp2);
		this.ob.appendChild(tmp);
		tmp = mkEl("div", {className: "wp-gotopage-next"});
		this.obs.lnkNextPage = tmp;
		tmp.appendChild(document.createTextNode("下一页"));
		if (this.curPage == this.pageCount) $D.addClass(tmp, "disabled");
		$E.on(tmp, "click", this.gotoNextPage, this, true);
		this.ob.appendChild(tmp);
	},
	chkState: function () {
		if (this.curPage > 1)
			$D.removeClass(this.obs.lnkPrePage, "disabled");
		else
			$D.addClass(this.obs.lnkPrePage, "disabled");
		if (this.curPage < this.pageCount)
			$D.removeClass(this.obs.lnkNextPage, "disabled");
		else
			$D.addClass(this.obs.lnkNextPage, "disabled");
		this.obs.curPage.innerHTML = this.curPage + "/" + this.pageCount;
		var lis = this.obs.pages.getElementsByTagName("li");
		for (var i = 0; lis[i]; i ++) {
			if (this.curPage != i + 1)
				$D.removeClass(lis[i], "selected");
			else
				$D.addClass(lis[i], "selected");
		}
	},
	gotoPage: function (p) {
		this.curPage = p;
		WP_GotoPage.curPage = p;
		if (this.callback)
			this.callback(p);
		//this.chkState();
		WP_GotoPage.update();
	},
	gotoPrePage: function () {
		this.gotoPage(--this.curPage);
	},
	pageSelect: function (li) {
		var p = parseInt(li.innerHTML) || 1;
		this.gotoPage(p);
	},
	gotoNextPage: function () {
		this.gotoPage(++this.curPage);
	},
	hidePages: function () {
		var _this = this;
		clearTimeout(this.tm);
		this.tm = setTimeout(function () {
			$D.removeClass(_this.obs.somePage, "hover");
		}, 500);
	},
	showPages: function () {
		clearTimeout(this.tm);
		$D.addClass(this.obs.somePage, "hover");
		$D.setStyle(this.obs.pages, "width", this.obs.somePage.offsetWidth - 12 + "px");
	},
	pageUnhover: function (li) {
		$D.removeClass(li, "hover");
	},
	pageHover: function (li) {
		clearTimeout(this.tm);
		$D.addClass(li, "hover");
	}
};

WP_GotoPage.items = [];
WP_GotoPage.curPage = 1;
WP_GotoPage.update = function () {
	for (var i = 0; WP_GotoPage.items[i]; i ++) {
		WP_GotoPage.items[i].curPage = WP_GotoPage.curPage;
		WP_GotoPage.items[i].chkState();
	}
};
