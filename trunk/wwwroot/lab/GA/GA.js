/* GA.js
 *
 */

(function () {
	GA = function (params) {
		if (!params) params = {};
		this.xRate = params.xRate || 0.9;
		this.mutationRate = params.mutationRate || 0.005;
		this.mutationCount = 0;
		this.generation = 0;
		this.oldLives = [];
		this.lives = [];
		this.lifeCount = params.lifeCount || 50;
		this.geneLength = params.geneLength || 100;

		this.init();
	};

	GA.prototype = {
		init: function () {
			for (var i = 0; i < this.lifeCount; i ++) {
				this.lives.push(new GA.Life(this));
			}
		},
		_bear: function (p1, p2) {
			var r = Math.random(), gene, c;
			if (r < this.xRate) {
				r = Math.floor(Math.random() * this.geneLength);
				gene = p1.gene.substr(0, r) + p2.gene.substr(r);
			} else {
				gene = p1.gene;
			}
			r = Math.random();
			if (r < this.mutationRate) {
				r = Math.floor(Math.random() * this.geneLength);
				c = gene.indexOf(r) == "1" ? "0" : "1";
				gene = gene.substr(0, r - 1) + c + gene.substr(r);
				this.mutationCount ++;
			}
			return new GA.Life(this, gene);
		},
		_getOne: function () {
			var r = Math.random() * this.bounds;
			for (var i = 0; i < this.lifeCount; i ++) {
				r -= this.lives[i].score;
				if (r <= 0) return this.lives[i];
			}
		},
		_getBounds: function () {
			this.bounds = 0;
			for (var i = 0; i < this.lifeCount; i ++)
				this.bounds += this.lives[i].score;
		},
		_newChild: function () {
			return this._bear(this._getOne(), this._getOne());
		},
		next: function () {
			var newLives = [], i;
			this._getBounds();
			while (newLives.length < this.lifeCount) {
				newLives.push(this._newChild());
			}
			this.lives = newLives;
			this.generation ++;
		}
	};

	GA.Life = function (park, gene) {
		this.park = park;
		this.score = 1;
		if (typeof(gene) == "string" && gene.length == this.park.geneLength)
			this.gene = gene;
		else
			this.rndGene();
	};

	GA.Life.prototype = {
		init: function () {
		},
		rndGene: function () {
			var l = this.park.geneLength;
			this.gene = "";
			while (l) {
				this.gene += Math.random() > 0.5 ? "1" : "0";
				l --;
			}
			return this;
		},
		setScore: function (v) {
			this.score = v;
		},
		addScore: function (v) {
			this.score += v;
		}
	}
})();
