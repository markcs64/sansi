/* dragOrder.js */

var $DD = {
	container: null,
	items: [],
	order0: [],
	init: function (arr) {
		$DD.container = $("orderItems");
		for (var i = 0, l = arr.length; i < l; i ++) {
			new $DD.item(arr[i]);
		}
		$DD.show();
		$DD.app.init();
	},
	show: function () {
		for (var i = 0, l = $DD.items.length; i < l; i ++) {
			$DD.container.appendChild($DD.items[i].ob);
		}
	},
	item: function (ob) {
		this.id = ob.id;
		this.ob = mkEl("li", {className: "item"});
		this.ob.innerHTML = "<div class=\"itemWrapper\"><img src=\""
			+ (ob.cover || ob.src) + "\" />"
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
		$D.setStyle(el, "opacity", 0.67);

		this.goingUp = false;
		this.lastY = 0;
	}
};

YAHOO.extend($DD.list, $Y.DDProxy, {
	startDrag: function (x, y) {
		var dragEl = this.getDragEl();
		var clickEl = this.getEl();
		$D.addClass(dragEl, "item");
		//$D.setStyle(clickEl, "visibility", "hidden");
		dragEl.innerHTML = clickEl.innerHTML;
		$D.setStyle(dragEl, "color", $D.getStyle(clickEl, "color"));
		$D.setStyle(dragEl, "backgroundColor", $D.getStyle(clickEl, "backgroundColor"));
		$D.setStyle(dragEl, "border", "2px solid gray");
	},
	endDrag: function (e) {
		var srcEl = this.getEl();
		var proxy = this.getDragEl();

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
		if (destEl.nodeName.toLowerCase() == "li") {
			var orig_p = srcEl.parentNode;
			var p = destEl.parentNode;
			if (this.goingUp) {
				p.insertBefore(srcEl, destEl);
			} else {
				p.insertBefore(srcEl, destEl.nextSibling);
			}
			$Y.DragDropMgr.refreshCache();
		}
	}
});

//$E.onDOMReady($DD.app.init, $DD.app, true);
