/* ’’∆¨ */

function WP_Photo(p) {
	this.id = p.id || "";
	this.title = p.title || "";
	this.src = p.src || "";
	this.datetime = p.datetime || new Date();
	this.desc = p.desc || "";

	WP_Photo.items.push(this);
}

WP_Photo.prototype = {
	
};

WP_Photo.items = [];


function WP_Photo_Li(ob) {
	this.ob = ob;
	this.img = ob.getElementsByTagName("img")[0];
	this.infoBar = $D.getElementsByClassName("info", "div", ob)[0];
	this.chkbox = this.ob.getElementsByTagName("input")[0];
	this._tm = 0;
	g_imgMaxSize(this.img, 64, 64);
	$E.on(this.ob, "mouseover", this.showAct, this, true);
	$E.on(this.ob, "mouseout", this.hideAct, this, true);
	$E.on(this.chkbox, "click", this.chkSelect, this, true);
}

WP_Photo_Li.prototype = {
	showAct: function () {
		clearTimeout(this._tm);
		var anim = new $Y.Anim(this.infoBar, {
			height: {to: 20}
		}, 0.2);
		anim.animate();
	},
	hideAct: function () {
		var _this;
		var anim = new $Y.Anim(this.infoBar, {
			height: {to: 0}
		}, 0.2);
		//anim.animate();
		clearTimeout(this._tm);
		this._tm = setTimeout(function () {
			anim.animate();
		}, 200);
	},
	chkSelect: function () {
		if (!this.chkbox.checked) {
			$D.getElementsByClassName("actSelectAll", "input", "photoArea", function (o) {
				o.checked = false;
			});
		}
	}
};
