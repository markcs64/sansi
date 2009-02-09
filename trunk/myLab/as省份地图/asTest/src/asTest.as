package {
	import flash.display.Bitmap;
	import flash.display.BlendMode;
	import flash.display.DisplayObject;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.events.TextEvent;
	import flash.events.TimerEvent;
	import flash.external.ExternalInterface;
	import flash.filters.GlowFilter;
	import flash.net.URLRequest;
	import flash.net.navigateToURL;
	import flash.text.TextField;
	import flash.text.TextFieldAutoSize;
	import flash.text.TextFieldType;
	import flash.text.TextFormat;
	import flash.utils.Timer;
	import flash.utils.clearTimeout;
	import flash.utils.setTimeout;

	[SWF(frameRate="30", backgroundColor="0xffffff", width="600", height="480")]
	
	public class asTest extends Sprite
	{
		public var sprProv:Sprite = new Sprite();
		public var prov:Object;
		public var cnmap:CNMap = new CNMap();
		
		private var tmOut:int;
		private var tmOut_cit:int;
		private var sprCit:Sprite = new Sprite();
		private var cit:TextField = new TextField();
		private var isCitiesHovering:Boolean = false;
		private var mapParams:Object;
		private var curProv:DisplayObject;
		
		private var demo:animDemo;
		private var demoShow:Boolean = true;
		[Embed(source="../img/cursor.png")]
		private var cursor:Class;

		public function asTest()
		{
			super();
			getParams();
			locateProv();
			stage.addChild(sprProv);
			stage.addChild(sprCit);
			
			citiesMenu();
			anim();
		}
		
		private function anim():void {
			var pointer:Bitmap = new Bitmap();
			var asset:Bitmap = new cursor() as Bitmap;
			pointer.bitmapData = asset.bitmapData;
			
			//stage.addChild(pointer);
			
			demo = new animDemo(this, pointer);
			setTimeout(demo.show, 1000);
		}
		
		private function citiesMenu():void {
			cit.type = TextFieldType.DYNAMIC;
			cit.autoSize = TextFieldAutoSize.LEFT;
			cit.multiline = true;
			cit.background = true;
			cit.backgroundColor = 0xffffff;
			cit.borderColor = 0x666666;
			cit.border = true;
			cit.alpha = 0.85;
			cit.addEventListener(TextEvent.LINK, citySelected);
			cit.addEventListener(MouseEvent.MOUSE_OVER, hoverCities);
			cit.addEventListener(MouseEvent.MOUSE_OUT, unhoverCities);
			
			//cit.thickness = 3;
			sprCit.visible = false;
			sprCit.blendMode = BlendMode.LAYER;
			sprCit.addChild(cit);
			
			var filter:GlowFilter = new GlowFilter();
			filter.color = 0xff6600;
			filter.inner = true;
			filter.strength = 2;
			cit.filters = [filter];
			
			//setCitiesTextFormat();
			
			//cit.addEventListener(Event.ENTER_FRAME, cityHover);
		}
		
		private function setCitiesTextFormat():void {
			var tf:TextFormat = new TextFormat();
			tf.kerning = true;
			tf.leading = 5;
			tf.leftMargin = 6;
			tf.rightMargin = 6;
			tf.size = 14;
			cit.defaultTextFormat = tf;
			//cit.setTextFormat(tf);
		}
		
		private function cityHover(e:Event):void {
			var tf:TextField = TextField(e.target);
			var i:int = tf.getCharIndexAtPoint(tf.mouseX, tf.mouseY);
			trace(i);
			if (i == -1) return;
			var f:TextFormat = new TextFormat();
			f.color = 0xff0000;
			tf.setTextFormat(f, i, i + 1);
		}
		
		private function citySelected(e:TextEvent):void {
			var url:String = mapParams.replace(/\{1\}/, e.text);
			openUrl(url);
		}
		
		private function citySpace(cityName:String, maxLen:int):String {
			var s:String = cityName + "　　　　　　　　　";
			var l:int = maxLen;
			l += cityName.length - cityName.replace(/<.+?>/g, "").replace(/[\s'"]/g, "").length;
			s = s.substr(0, l);
			return s;
		}
		
		private function showCities(ob:DisplayObject):void {
			clearTimeout(tmOut_cit);
			setCitiesTextFormat();
			var x:int, y:int;
			var p:String = ob.toString().match(/\[object (\w+)\]/i)[1].toString().toLowerCase();
			var pName:String = this.cnmap.prov[p];
			var htmlText:String = "" +
				"<p><font size='5'>&nbsp;</font></p>" +
				"<p><font color='#333333'><font size='16'><b>" + pName + "</b></font>";

			var sCitys:String = this.cnmap.provCity[pName];
			var citys:Array = sCitys.split("|");
			var maxLen:int = this.cnmap.citiesMaxLen[pName];
			//trace(pName + "::" + maxLen);

			//if (sprCit.visible == false) {
				clearTimeout(tmOut);
				var i:int, l:int = citys.length;
				for (i = 0; i < l; i ++) {
					if (maxLen < 9 && i % 2 == 1)
						htmlText += "　";
					else
						htmlText += "<br>";
					htmlText += "<a href='event:" + citys[i].replace(/<.+?>/g, "").replace(/[\s'"]/g, "") +
						"'>" + citySpace(citys[i], maxLen) + "</a>";
				}
				htmlText += "</font></p><font size='5'>&nbsp;</font>";
				cit.htmlText = htmlText;
				x = ob.x + ob.width / 2;
				y = ob.y + ob.height / 2;
				if (x + cit.width + 20 > stage.width) {
					x -= cit.width;
				}
				if (y + cit.height + 20 > stage.height) {
					y -= cit.height;
				}
				if (y < 10) {
					y = 10;
				}
				sprCit.x = x;
				sprCit.y = y;
				sprCit.visible = true;
				sprCit.alpha = 0;
				fadeInOut(sprCit);
			//}
			//cit.addEventListener(Event.ENTER_FRAME, cityHover);
		}
		
		private function hideCities():void {
			clearTimeout(tmOut);
			if (isCitiesHovering == false) {
				sprCit.alpha = 1;
				fadeInOut(sprCit);
				//sprCit.visible = false;
			
				curProv.filters = [];
				var pn:String = curProv.toString().match(/\[object (\w+)\]/i)[1].toLowerCase();
				fadeTo(curProv, cnmap.hot[pn]);
			}
			//cit.dispatchEvent();
		}
		
		private function hoverCities(e:MouseEvent):void {
			isCitiesHovering = true;
		}
		
		private function unhoverCities(e:MouseEvent):void {
			isCitiesHovering = false;
			hideCities();
		}
		
		private function hover(e:MouseEvent):void {
			//clearTimeout(tmOut_cit);
			demo.couldShow = false;
			demo.hide();
			clearTimeout(tmOut);
			if (this.curProv) {
				this.curProv.filters = [];
				//var pn:String = curProv.toString().match(/\[object (\w+)\]/i)[1].toLowerCase();
				//fadeTo(curProv, cnmap.hot[pn]);
			}
			
			var ob:DisplayObject = DisplayObject(e.target);
			
			hover2(ob);
		}
		
		public function hover2(ob:DisplayObject):void {
			this.curProv = ob;
			var filter:GlowFilter = new GlowFilter();
			filter.color = 0x333333;
			filter.strength = 2;
			ob.filters = [filter];
			//fadeTo(ob, 10);
			ob.parent.setChildIndex(ob, ob.parent.numChildren - 1);
			
			tmOut_cit = setTimeout(function ():void {
				showCities(ob);
			}, 500);
		}
		
		private function unhover(e:MouseEvent):void {
			clearTimeout(tmOut_cit);
			var ob:DisplayObject = DisplayObject(e.target);
			tmOut = setTimeout(hideCities, 800);
		}
		
		private function fadeTo(ob:DisplayObject, v:int):void {
			var p:Number = 0.5 + v * 0.05;
			if (p > 1) p = 1;
			//trace(ob);
			ob.alpha = p;
		}
		
		private function fadeInOut(ob:DisplayObject):void {
			var tmr:Timer = new Timer(10);
			var a:Number = ob.alpha;
			var p:Number = a <= 0 ? 0.05 : -0.05;
			var t:Number = a <= 0 ? 1 : 0;
			var _f:Function = function (e:TimerEvent):void {
				ob.alpha += p;
				if (ob.alpha >= 1 || ob.alpha <= 0) {
					tmr.stop();
					if (ob.alpha <= 0)
						ob.visible = false;
				}
			};
			tmr.addEventListener(TimerEvent.TIMER, _f);
			tmr.start();
		}
		
		private function getParams():void {
			var k:String;
			try {
				var params:Object = ExternalInterface.call("mapParams");
				
				if (!params) {
					params = {};
				}
				mapParams = params.url || "http://www.google.cn/search?q={1}";
				if (params.hot) {
					for (k in params.hot) {
						cnmap.hot[k] = parseInt(params.hot[k]) || 0;
					}
				}
				
				if (params.cities) {
					for (k in params.cities) {
						cnmap.provCity[k] = params.cities[k];
					}
				}
			} catch (e:Error) {
			}
			
			var maxLen:int;
			var cities:Array;
			var i:int;
			for (k in cnmap.provCity) {
				maxLen = 0;
				cities = cnmap.provCity[k].split("|");
				for (i = 0; i < cities.length; i ++) {
					if (cities[i].length > maxLen)
						maxLen = cities[i].replace(/<.+?>/g, "").replace(/[\s'"]/g, "").length;
				}
				cnmap.citiesMaxLen[k] = maxLen;
			}
		}
		
		private function openUrl(url:String):void {
			navigateToURL(new URLRequest(url), "_blank");
		}
		
		private function locateProv():void {
			prov = {
				zj: new ZJ (),
				s1x: new S1X (),
				hlj: new HLJ (),
				tw: new TW (),
				gd: new GD (),
				fj: new FJ (),
				jx: new JX (),
				hun: new HUN (),
				gz: new GZ (),
				gx: new GX (),
				gs: new GS (),
				js: new JS (),
				sh: new SH (),
				hain: new HAIN (),
				hub: new HUB (),
				nx: new NX (),
				s3x: new S3X (),
				jl: new JL (),
				hen: new HEN (),
				cq: new CQ (),
				yn: new YN (),
				sc: new SC (),
				xz: new XZ (),
				qh: new QH (),
				xj: new XJ (),
				tj: new TJ (),
				nmg: new NMG (),
				bj: new BJ (),
				sd: new SD (),
				heb: new HEB (),
				ln: new LN (),
				ah: new AH ()
			};
			
			prov.zj.x = 467;
			prov.zj.y = 292.35;
			prov.s1x.x = 378.75;
			prov.s1x.y = 185.7;
			prov.hlj.x = 445;
			prov.hlj.y = 23.5;
			prov.tw.x = 496.5;
			prov.tw.y = 359.5;
			prov.gd.x = 379.35;
			prov.gd.y = 366.5;
			prov.fj.x = 447.9;
			prov.fj.y = 326.9;
			prov.jx.x = 419.85;
			prov.jx.y = 311;
			prov.hun.x = 369.35;
			prov.hun.y = 313;
			prov.gz.x = 313.95;
			prov.gz.y = 326.1;
			prov.gx.x = 323.25;
			prov.gx.y = 358.5;
			prov.gs.x = 213;
			prov.gs.y = 162.5;
			prov.js.x = 441.3;
			prov.js.y = 244.45;
			prov.sh.x = 496.5;
			prov.sh.y = 276.6;
			prov.hain.x = 370.3;
			prov.hain.y = 437;
			prov.hub.x = 363.8;
			prov.hub.y = 275.9;
			prov.nx.x = 324.65;
			prov.nx.y = 206.6;
			prov.s3x.x = 334.15;
			prov.s3x.y = 202.6;
			prov.jl.x = 467.3;
			prov.jl.y = 107.5;
			prov.hen.x = 381;
			prov.hen.y = 235.1;
			prov.cq.x = 325.65;
			prov.cq.y = 290.8;
			prov.yn.x = 245.2;
			prov.yn.y = 321.5;
			prov.sc.x = 247.8;
			prov.sc.y = 265.85;
			prov.xz.x = 58.8;
			prov.xz.y = 229.1;
			prov.qh.x = 173.95;
			prov.qh.y = 203.6;
			prov.xj.x = 33.8;
			prov.xj.y = 77.5;
			prov.tj.x = 436.95;
			prov.tj.y = 190.85;
			prov.nmg.x = 255.9;
			prov.nmg.y = 27;
			prov.bj.x = 422.75;
			prov.bj.y = 179.35;
			prov.sd.x = 425.8;
			prov.sd.y = 204.6;
			prov.heb.x = 406.85;
			prov.heb.y = 158.35;
			prov.ln.x = 453.1;
			prov.ln.y = 140.3;
			prov.ah.x = 427.85;
			prov.ah.y = 253.05;

			for (var p:String in prov) {
				sprProv.addChild(prov[p]);
				fadeTo(prov[p], cnmap.hot[p]);
				prov[p].addEventListener(MouseEvent.MOUSE_OVER, hover);
				prov[p].addEventListener(MouseEvent.MOUSE_OUT, unhover);
			}
			
			//var ppp:Point = new Point(300, 300);
			//trace(sprProv.getObjectsUnderPoint(ppp));
			
			sprProv.setChildIndex(prov.zj, 0);
		}
	}
}