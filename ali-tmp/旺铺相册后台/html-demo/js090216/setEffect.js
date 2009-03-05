/* setEffect.js */

var $Tab = {
	init: function () {
		$D.getElementsBy(function () {
			return true;
		}, "li", $D.getElementsByClassName("tabHead")[0], function (o) {
			$Tab.tabItems.push(o);
			var t = mkEl("b", {className: "tabHL"});
			$D.insertBefore(t, o.firstChild);
			t = mkEl("b", {className: "tabHR"});
			$D.insertBefore(t, o.firstChild);
			$E.on(o, "click", $Tab.select);
			if ($D.hasClass(o, "inuse")) {
				o.innerHTML += "<span>(ÒÑÑ¡ÖÐ)</span>";
			}
		});
		$D.getElementsBy(function () { return true; }, "li",
			$D.getElementsByClassName("tabBody")[0], function (o) {
				$Tab.tabBodys.push(o);
			});
		$J($("effectList").getElementsByTagName("a")).each(function () {
			this.onclick = function () {this.blur();return false;}
		});
	},
	curIdx: 0,
	tabItems: [],
	tabBodys: [],
	select: function () {
		$J($Tab.tabItems).each(function () {
			$D.removeClass(this, "selected");
		});
		$D.addClass(this, "selected");
		for (var i = 0; i < $Tab.tabItems.length; i ++) {
			if ($Tab.tabItems[i] == this) $Tab.curIdx = i;
		}
		$J($Tab.tabBodys).each(function () {
			$D.removeClass(this, "selected");
		});
		$D.addClass($Tab.tabBodys[$Tab.curIdx], "selected");
	}
};

function initStars() {
	$J($D.getElementsByClassName("effect-stars")).each(function () {
		var v = parseInt(this.innerHTML) || 0,
			html = "";
		for (var i = 1; i <= 5; i ++) {
			html += "<img src=\"img090216/"
				+ (v >= i ? "6003016" : "6003116")
				+ ".gif\" />";
		}
		this.innerHTML = html;
	});
}
