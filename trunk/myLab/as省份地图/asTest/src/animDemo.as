// 动画演示
package {
	import flash.display.Bitmap;
	import flash.display.DisplayObject;
	import flash.display.Sprite;
	import flash.display.Stage;
	import flash.utils.clearTimeout;
	import flash.utils.setTimeout;
	
	public class animDemo {
		public var couldShow:Boolean = true;
		public var cursor:Sprite = new Sprite();
		public var step:int = 5;	//每次移动的距离
		public var tmShow:int;
		private var stage:Stage;
		private var su:Object;
		private var cursorMoving:Boolean = false;
		private var showList:Array = [];//["zj", "gd", "bj"];
		//private var showIdx:int = 0;
		
		public function animDemo(su:Object, cursor:Bitmap) {
			this.cursor.addChild(cursor);
			this.cursor.visible = false;
			this.cursor.x = 300;
			this.cursor.y = 50;
			
			su.stage.addChild(this.cursor);
			this.stage = su.stage;
			this.su = su;
			
			for (var k:String in this.su.prov) {
				this.showList.push(k);
			}
		}
		
		public function show():void {
			if (!this.couldShow) return;
			/*if (this.cursorMoving) {
				setTimeout(this.show, 50);
				return;
			}*/
			
			this.cursor.visible = true;
			//this.cursor.
			
			//this.moveTo(480, 320, 0);
			var r:int = Math.floor(Math.random() * this.showList.length);
			this.moveTo(this.su.prov[this.showList[r]]);
			
			//this.showIdx ++;
			//if (this.showIdx >= this.showList.length) this.showIdx = 0;
			
			setTimeout(this.show, 6000);
		}
		
		public function hide():void {
			this.cursor.visible = false;
		}
		
		private function moveTo(prov:DisplayObject):void {
			//将鼠标移到某个省
			var x:Number = prov.x + prov.width / 2;
			var y:Number = prov.y + prov.height / 2;
			
			//将鼠标移到位置 x, y
			var x0:Number = this.cursor.x;
			var y0:Number = this.cursor.y;
			var xm:Number = x - x0;
			var ym:Number = y - y0;
			
			var d:Number = Math.sqrt(xm * xm + ym * ym);	//距离
			var steps:Number = d / this.step;
			
			var xs:Number = xm / steps;
			var ys:Number = ym / steps;
			
			var ob:Sprite = this.cursor;
			var tmOut:uint;
			var _this:Object = this;
			
			var move:Function = function (x:int, y:int, xs:Number, ys:Number):void {
				//trace(xs, ys);
				var absX:Number = Math.abs(ob.x - x);
				var absY:Number = Math.abs(ob.y - y);
				_this.cursorMoving = true;
				
				if (absX < 1 && absY < 1) {
					clearTimeout(tmOut);
					_this.hover(prov);
					_this.cursorMoving = false;
					return;
				}
				//trace(ob.x, ob.y);

				if (absX < Math.abs(xs))
					xs = x - ob.x;
				if (absY < Math.abs(ys))
					ys = y - ob.y;
				
				ob.x += xs;
				ob.y += ys;
			};
			
			var f:Function = function():void {
				tmOut = setTimeout(f, 30);
				move(x, y, xs, ys);
				if (!_this.couldShow) {
					clearTimeout(tmOut);
				}
			}
			
			f();
		}
		
		private function hover(prov:DisplayObject):void {
			//var p:Point = new Point(this.cursor.x, this.cursor.y);
			//var obs:Array = this.stage.getObjectsUnderPoint(p);
			//var prov:DisplayObject = obs[0];
			//var sp:Sprite = this.stage.getChildAt(1) as Sprite;
			//var prov:DisplayObject = sp.getChildAt(idx);
			//trace(obs, prov, sp.getChildAt(3));
			//for (var i:int = 0; i < sp.numChildren; i ++) {
			//	trace(i, sp.getChildAt(i));
			//}
			//trace(sp.numChildren);
			/*var filter:GlowFilter = new GlowFilter();
			filter.color = 0x333333;
			filter.strength = 2;
			prov.filters = [filter];*/
			
			this.su.hover2(prov);
		}
	}
}