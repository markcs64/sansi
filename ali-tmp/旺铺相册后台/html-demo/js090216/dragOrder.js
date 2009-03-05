/* dragOrder.js */

var $DD = {
	container: null,
	items: [],
	order0: [],
	saveBtns: [],
	init: function (arr) {
		$DD.container = $("orderItems");
		for (var i = 0, l = arr.length; i < l; i ++) {
			new $DD.item(arr[i]);
		}
		$DD.show();
		$DD.app.init();
		$J($DD.container.getElementsByTagName("img")).each(function () {
			g_imgMaxSize(this, 64, 64);
			$D.setStyle(this, "margin", (64 - this.offsetHeight) / 2 + "px 0");
		});

		$D.getElementsByClassName("resetOrder", "a", "main_right_body", function (o) {
			o.onclick = function () {
				$DD.resetOrder();
				return false;
			};
		});
		$J(BTN902.btns).each(function () {
			if (this.text == "±£´æË³Ðò") {
				$DD.saveBtns.push(this);
				this.disable(1);
			}
			this.on("click", $DD.saveOrder);
		});
	},
	show: function () {
		for (var i = 0, l = $DD.items.length; i < l; i ++) {
			$DD.container.appendChild($DD.items[i].ob);
		}
	},
	saveOrder: function () {
		var od = [],
		obs = $D.getElementsByClassName("itemWrapper", "div", $("orderItems"), function (o) {
			od.push(o.id.substring(8));
		});
		alert("±£´æË³Ðò\n\n" + od.join(", "));
	},
	resetOrder: function () {
		var ul = $("orderItems");
		for (var i = 0, l = $DD.order0.length; i < l; i ++) {
			ul.appendChild($DD.order0[i]);
		}
		$J($DD.saveBtns).each(function () { this.disable(1); });
	},
	item: function (ob) {
		this.id = ob.id;
		this.ob = mkEl("li", {className: "item"});
		this.ob.innerHTML = "<div id=\"dd-item-" + this.id + "\" class=\"itemWrapper\"><img src=\""
			+ (ob.cover || ob.src || "img090216/no_photo.gif") + "\" />"
			+ (ob.title ? "<div class=\"title\">" + ob.title + "</div>" : "")
			+ "</div>";

		$DD.items.push(this);
		$DD.order0.push(this.ob);

		//this.dd = new $Y.DD(this.ob);
		/*this.dd = new $Y.DDProxy(this.ob, "default", {
			dragElId: "dd-proxy",
			centerFrame: false
			});*/
	},
	app: {
		init: function () {
			new $Y.DDTarget("orderItems");
			var lis = $("orderItems").getElementsByTagName("li"),
				l = lis.length;
			for (var i = 0; i < l; i ++) {
				new $DD.list(lis[i]);
			}
		}
	},
	list: function (id, sGroup, config) {
		$DD.list.superclass.constructor.call(this, id, sGroup, config);
		var el = this.getDragEl();
		//$D.setStyle(el, "opacity", 0.8);
		if ($("photoArea-head"))
			$D.addClass(el, "photo");

		this.goingUp = true;
		this.lastY = 0;
	}
};

YAHOO.extend($DD.list, $Y.DDProxy, {
	startDrag: function (x, y) {
		var dragEl = this.getDragEl();
		var clickEl = this.getEl();
		$D.addClass(dragEl, "item");
		//$D.setStyle(clickEl, "visibility", "hidden");
		dragEl.innerHTML = "<div class=\"wrapper\"><div id=\"dragHand\"></div>" + clickEl.innerHTML + "</div>";
		$D.getElementsByClassName("itemWrapper", "div", dragEl, function (o) {
			$D.setStyle(o, "opacity", 0.8);
		});
		//$D.setStyle(dragEl, "color", $D.getStyle(clickEl, "color"));
		//$D.setStyle(dragEl, "backgroundColor", $D.getStyle(clickEl, "backgroundColor"));
		//$D.setStyle(dragEl, "border", "2px solid gray");
		$D.setStyle(clickEl, "border", "1px solid #A0B6E8");
	},
	endDrag: function (e) {
		var srcEl = this.getEl();
		var proxy = this.getDragEl();

		this.vars.onEl.parentNode.insertBefore(srcEl, this.vars.onEl);
		//$D.setStyle(this.vars.onEl, "margin-left", "0");
		$D.removeClass(this.vars.onEl, "target");
		$D.setStyle(proxy, "visibility", "");
		var a = new $Y.Motion(
			proxy, {
				points: {
					to: $D.getXY(srcEl)
				}
			},
			0.2,
			$Y.Easing.easeOut
		);
		var proxyId = proxy.id;
		var thisId = this.id;
		a.onComplete.subscribe(function () {
			$D.setStyle(proxyId, "visibility", "hidden");
			$D.setStyle(thisId, "visibility", "");
		});
		a.animate();
		$J($DD.saveBtns).each(function () { this.disable(0); });
		$D.setStyle(srcEl, "border", "1px solid #fff");
	},
	onDragDrop: function (e, id) {
		if ($Y.DragDropMgr.interactionInfo.drop.length === 1) {
			var pt = $Y.DragDropMgr.interactionInfo.point;
			var region = $Y.DragDropMgr.interactionInfo.sourceRegion;
			if (!region.intersect(pt)) {
				var destEl = $(id);
				var destDD = $Y.DragDropMgr.getDDById(id);
				destEl.appendChild(this.getEl());
				destDD.isEmpty = false;
				$Y.DragDropMgr.refreshCache();
			}
		}
	},
	onDrag: function (e) {
		var y = $E.getPageY(e);
		if (y < this.lastY) {
			this.goinUp = true;
		} else if (y > this.lastY) {
			this.goinUp = false;
		}
		this.lastY = y;
	},
	onDragOver: function (e, id) {
		var srcEl = this.getEl();
		var destEl = $(id);
		var a;
		if (destEl.tagName.toLowerCase() == "li" && 
				destEl.className == "item" && 
				this.vars.onEl != destEl) {
			//$D.setStyle(this.vars.onEl, "margin-left", "0");
			$D.removeClass(this.vars.onEl, "target");
			/*a = new $Y.Anim(this.vars.onEl, {
				marginLeft: {to: 0}
			}, 0.2);
			a.animate();*/
			this.vars.onEl = destEl;
		}
		if (destEl.nodeName.toLowerCase() == "li") {
			var orig_p = srcEl.parentNode;
			var p = destEl.parentNode;
			if (this.goingUp) {
				//p.insertBefore(srcEl, destEl);
				//$D.setStyle(destEl, "margin-left", "10px");
				$D.addClass(this.vars.onEl, "target");
				/*a = new $Y.Anim(destEl, {
					marginLeft: {to: 10}
				}, 0.1);*/
			} else {
				p.insertBefore(srcEl, destEl.nextSibling);
			}
			$Y.DragDropMgr.refreshCache();
		}
		//a.animate();
	},
	vars: {
		onEl: null
	}
});

//$E.onDOMReady($DD.app.init, $DD.app, true);
