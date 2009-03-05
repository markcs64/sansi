/* alioj */

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
	
	oj.cookie = function (k, v, expDT) {
		if (arguments.length == 1) {	//get
			v = document.cookie.match("(?:^|;)\\s*" + k + "=([^;]*)");
			return v ? unescape(v[1]) : "";
		} else {	//set
		}
	};
	
	$J = oj;
})();