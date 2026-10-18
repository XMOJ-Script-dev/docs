# 生成 features/rating.md 中的图表：python3 scripts/rating_charts.py
# 公式必须和 features/rating.md 保持一致，改动评分算法时请同步这里并重新生成。
import math, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "features", "charts")
os.makedirs(OUT, exist_ok=True)

# ---------- the formula, exactly as documented ----------
def g(a): return a if a <= 8 else 8 + 8 * math.log(1 + (a - 8) / 8)
def acc(P):
    if P < 0.15: return 0.0
    if P < 0.4: return (P - 0.15) / 0.25
    if P < 0.55: return 1.0
    return max(0.3, 1 - 2 * (P - 0.55))
def rating(S, X, D, B=1.0):
    if S == 0: return 0
    vol = 1 - math.exp(-S * B / 350)
    P = (S + 10) / (S + X + 40)
    K = S / (S + 80)
    per = 1 - math.exp(-D / 250)
    return 3000 * (0.57 * vol + 0.33 * acc(P) * K + 0.10 * per) ** 0.9

# ---------- theming ----------
# Each colour is var(--vp-…, var(--local)). Inlined into the page the --vp vars win and
# follow the site's light/dark toggle; opened on its own the --vp vars are undefined, so
# the local vars from <style> apply and follow the OS colour scheme.
FG   = "var(--vp-c-text-1, var(--x-fg))"
FG2  = "var(--vp-c-text-2, var(--x-fg2))"
GRID = "var(--vp-c-divider, var(--x-grid))"
AXIS = "var(--vp-c-text-3, var(--x-axis))"
BR   = "var(--vp-c-brand-1, var(--x-brand))"
SOFT = "var(--vp-c-brand-soft, var(--x-soft))"
BG   = "var(--vp-c-bg, var(--x-bg))"
FONT = "var(--vp-font-family-base, Georgia, 'Songti SC', 'Noto Serif CJK SC', serif)"
# scoped to .rating-chart so the inlined <style> doesn't leak onto other SVGs on the page
STYLE = """<style>
.rating-chart{--x-fg:#000;--x-fg2:#737373;--x-grid:#e5e5e5;--x-axis:#a3a3a3;--x-brand:#000;--x-soft:#f5f5f5;--x-bg:#fff}
@media (prefers-color-scheme:dark){.rating-chart{--x-fg:#e5e5e5;--x-fg2:#a3a3a3;--x-grid:#2a2a2a;--x-axis:#737373;--x-brand:#e5e5e5;--x-soft:#222;--x-bg:#1a1a1a}}
</style>"""

W, H = 600, 360

def esc(s): return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

class Chart:
    def __init__(self, name, label, xr, yr, xt, yt, xlab, ylab, ml=56, mr=24, mt=24, mb=52, ytick_fmt=None, xtick_fmt=None):
        self.name, self.label = name, label
        self.clip = f"{name}-plot"  # ids must be unique: all charts share one page
        self.x0, self.x1 = ml, W - mr
        self.y0, self.y1 = H - mb, mt
        self.xr, self.yr = xr, yr
        self.parts = []
        self.xt, self.yt = xt, yt
        self.xlab, self.ylab = xlab, ylab
        self.yfmt = ytick_fmt or (lambda v: f"{v:g}")
        self.xfmt = xtick_fmt or (lambda v: f"{v:g}")
    def X(self, v): return self.x0 + (v - self.xr[0]) / (self.xr[1] - self.xr[0]) * (self.x1 - self.x0)
    def Y(self, v): return self.y0 - (v - self.yr[0]) / (self.yr[1] - self.yr[0]) * (self.y0 - self.y1)
    def add(self, s): self.parts.append(s)
    def text(self, x, y, s, fill=FG2, size=13, anchor="start", weight=400, extra=""):
        self.add(f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" style="fill:{fill};font-size:{size}px;font-weight:{weight}"{extra}>{esc(s)}</text>')
    def frame(self):
        out = []
        for v in self.yt:
            y = self.Y(v)
            out.append(f'<line x1="{self.x0}" x2="{self.x1}" y1="{y:.1f}" y2="{y:.1f}" style="stroke:{GRID};stroke-width:1"/>')
            out.append(f'<text x="{self.x0-8}" y="{y+4.5:.1f}" text-anchor="end" style="fill:{FG2};font-size:12px">{esc(self.yfmt(v))}</text>')
        for v in self.xt:
            x = self.X(v)
            out.append(f'<line x1="{x:.1f}" x2="{x:.1f}" y1="{self.y0}" y2="{self.y0+5}" style="stroke:{AXIS};stroke-width:1"/>')
            out.append(f'<text x="{x:.1f}" y="{self.y0+19}" text-anchor="middle" style="fill:{FG2};font-size:12px">{esc(self.xfmt(v))}</text>')
        out.append(f'<line x1="{self.x0}" x2="{self.x1}" y1="{self.y0}" y2="{self.y0}" style="stroke:{AXIS};stroke-width:1"/>')
        out.append(f'<text x="{(self.x0+self.x1)/2:.1f}" y="{H-10}" text-anchor="middle" style="fill:{FG2};font-size:13px">{esc(self.xlab)}</text>')
        out.append(f'<text x="8" y="{self.y1-12}" text-anchor="start" style="fill:{FG2};font-size:13px">{esc(self.ylab)}</text>')
        return out
    def path(self, f, a, b, n=400, stroke=BR, width=2.5, dash=None, clip=True):
        pts = []
        for i in range(n + 1):
            v = a + (b - a) * i / n
            pts.append(f"{self.X(v):.2f},{self.Y(f(v)):.2f}")
        d = f' stroke-dasharray="{dash}"' if dash else ""
        cp = f' clip-path="url(#{self.clip})"' if clip else ""
        self.add(f'<polyline points="{" ".join(pts)}" fill="none" style="stroke:{stroke};stroke-width:{width};stroke-linejoin:round;stroke-linecap:round"{d}{cp}/>')
    def dot(self, xv, yv, r=4.5):
        self.add(f'<circle cx="{self.X(xv):.1f}" cy="{self.Y(yv):.1f}" r="{r}" style="fill:{BR};stroke:{BG};stroke-width:2"/>')
    def guide(self, xv, yv):
        x, y = self.X(xv), self.Y(yv)
        self.add(f'<path d="M{x:.1f},{self.y0} V{y:.1f} H{self.x0}" fill="none" style="stroke:{FG2};stroke-width:1;opacity:.5" stroke-dasharray="3 3"/>')
    def save(self, before=()):
        body = [f'<rect width="{W}" height="{H}" style="fill:{BG}"/>']
        body.append(f'<clipPath id="{self.clip}"><rect x="{self.x0}" y="{self.y1}" width="{self.x1-self.x0}" height="{self.y0-self.y1}"/></clipPath>')
        body += list(before)
        body += self.frame()
        body += self.parts
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" class="rating-chart" viewBox="0 0 {W} {H}" role="img" aria-label="{esc(self.label)}" '
               f'style="max-width:100%;height:auto;font-family:{FONT}">'
               f'<title>{esc(self.label)}</title>{STYLE}' + "".join(body) + "</svg>\n")
        with open(f"{OUT}/{self.name}.svg", "w") as fh:
            fh.write(svg)

pct = lambda v: f"{v*100:.0f}%"

# ---------- 1. daily AC discount g(a) ----------
c = Chart("rating-daily-ac", "每天 AC 数与折算后计入的次数：超过 8 次后按对数增长",
          (0, 120), (0, 60), range(0, 121, 20), range(0, 61, 10),
          "当天的 AC 数 a", "折算后 g(a)")
c.add(f'<rect x="{c.X(0)}" y="{c.y1}" width="{c.X(8)-c.X(0):.1f}" height="{c.y0-c.y1}" style="fill:{SOFT}"/>')
c.text(c.X(8) + 6, c.y1 + 16, "≤ 8 次：原样计入", fill=FG2, size=12)
c.path(lambda a: a, 0, 120, n=2, stroke=FG2, width=1.5, dash="5 4")
c.text(c.X(44) - 6, c.Y(44) - 4, "不打折", fill=FG2, size=12, anchor="end")
c.path(g, 0, 120)
for a, dx, dy, anc in [(14, 10, 24, "start"), (120, -8, -14, "end")]:
    c.dot(a, g(a))
    c.text(c.X(a) + dx, c.Y(g(a)) + dy, f"AC {a} 次 → 约计 {g(a):.1f} 次", fill=FG, size=13, anchor=anc)
c.save()

# ---------- 2. volume ----------
c = Chart("rating-volume", "做题量随解决题数的变化：1 − e^(−S/350)",
          (0, 2000), (0, 1), range(0, 2001, 500), [0, .25, .5, .75, 1],
          "解决的题数 S（B = 1 时）", "做题量", ytick_fmt=pct)
f = lambda s: 1 - math.exp(-s / 350)
c.path(f, 0, 2000)
for s, dx, dy in [(350, 10, 18), (700, 10, 18), (1400, 0, 22)]:
    c.guide(s, f(s)); c.dot(s, f(s))
    c.text(c.X(s) + dx, c.Y(f(s)) + dy, f"{s} 题 → {f(s)*100:.0f}%", fill=FG, size=13)
c.save()

# ---------- 3. accuracy vs P ----------
c = Chart("rating-accuracy", "准确度随 P 的变化：P 在 40%–55% 时满分，过高反而减分",
          (0, 1), (0, 1), [0, .15, .4, .55, .9, 1], [0, .3, .5, 1],
          "评测过的提交中解决新题的比例 P", "准确度", ytick_fmt=pct, xtick_fmt=pct, mt=60)
c.add(f'<rect x="{c.X(.4):.1f}" y="{c.y1}" width="{c.X(.55)-c.X(.4):.1f}" height="{c.y0-c.y1}" style="fill:{SOFT}"/>')
c.path(acc, 0, 1, n=1000)
c.text((c.X(.4) + c.X(.55)) / 2, c.Y(1) + 20, "满分", fill=BR, size=13, anchor="middle", weight=600)
c.text(c.x1, c.Y(.3) + 20, "最低 30%", fill=FG, size=13, anchor="end")
c.text(c.X(.6), c.Y(.44), "几乎不失败，", fill=FG2, size=12)
c.text(c.X(.6), c.Y(.44) + 16, "更像复制的代码", fill=FG2, size=12)
# top axis: fails per solved problem when S is large (P ≈ 1 / (1 + f))
ty = c.y1
c.add(f'<line x1="{c.x0}" x2="{c.x1}" y1="{ty}" y2="{ty}" style="stroke:{AXIS};stroke-width:1"/>')
for fpp in [5, 3, 2, 1, .5, 0]:
    x = c.X(1 / (1 + fpp))
    c.add(f'<line x1="{x:.1f}" x2="{x:.1f}" y1="{ty-5}" y2="{ty}" style="stroke:{AXIS};stroke-width:1"/>')
    c.text(x, ty - 10, f"{fpp:g}", fill=FG2, size=12, anchor="middle")
c.text((c.x0 + c.x1) / 2, ty - 30, "≈ 平均每道已解决的题失败几次（题数很多时）", fill=FG2, size=12, anchor="middle")
c.save()

# ---------- 4. confidence K ----------
c = Chart("rating-confidence", "准确度的可信度 K = S / (S + 80)",
          (0, 1000), (0, 1), range(0, 1001, 200), [0, .25, .5, .75, 1],
          "解决的题数 S", "可信度 K", ytick_fmt=pct)
f = lambda s: s / (s + 80)
c.path(f, 0, 1000)
for s, dx, dy in [(80, 10, 18), (320, 6, 22), (720, 0, 22)]:
    c.guide(s, f(s)); c.dot(s, f(s))
    c.text(c.X(s) + dx, c.Y(f(s)) + dy, f"{s} 题 → {f(s)*100:.0f}%", fill=FG, size=13)
c.save()

# ---------- 5. persistence ----------
c = Chart("rating-persistence", "坚持度随有提交天数的变化：1 − e^(−D/250)",
          (0, 1000), (0, 1), range(0, 1001, 200), [0, .25, .5, .75, 1],
          "有提交的天数 D", "坚持度", ytick_fmt=pct)
f = lambda d: 1 - math.exp(-d / 250)
c.path(f, 0, 1000)
for d, dx, dy in [(100, 10, 18), (250, 10, 18), (500, 10, 20)]:
    c.guide(d, f(d)); c.dot(d, f(d))
    c.text(c.X(d) + dx, c.Y(f(d)) + dy, f"{d} 天 → {f(d)*100:.0f}%", fill=FG, size=13)
c.save()

# ---------- 6. overall ----------
BANDS = [  # (lo, hi, name, colour) — same colours as .rating.* in .vitepress/theme/style.css
    (2400, 3000, "红", "#dc2f5a"), (2000, 2400, "橙", "#e8590c"), (1600, 2000, "蓝", "#337cf2"),
    (1200, 1600, "绿", "#2b9f4f"), (800, 1200, "青", "#1798b0"), (0, 800, "灰", "#78828c")]
c = Chart("rating-overall", "评分随解决题数的变化，按每题平均失败次数分四条线，背景为用户名颜色",
          (0, 2000), (0, 3000), range(0, 2001, 500), [0, 800, 1200, 1600, 2000, 2400, 3000],
          "解决的题数 S", "评分", mr=132, ml=64)
bg = []
for lo, hi, name, col in BANDS:
    y_hi, y_lo = c.Y(hi), c.Y(lo)
    bg.append(f'<rect x="{c.x0}" y="{y_hi:.1f}" width="{c.x1-c.x0}" height="{y_lo-y_hi:.1f}" style="fill:{col};opacity:.13"/>')
    bg.append(f'<rect x="{c.x0-5}" y="{y_hi+1:.1f}" width="3" height="{y_lo-y_hi-2:.1f}" rx="1.5" style="fill:{col}"/>')
    bg.append(f'<text x="{c.x0-12}" y="{(y_hi+y_lo)/2+4.5:.1f}" text-anchor="end" style="fill:{col};font-size:12px;font-weight:600">{name}</text>')
# y tick labels sit on the band boundaries; nudge them so they don't collide with band names
c.yfmt = lambda v: ""
for v in [0, 800, 1200, 1600, 2000, 2400, 3000]:
    bg.append(f'<text x="{c.x0-26}" y="{c.Y(v)+4.5:.1f}" text-anchor="end" style="fill:{FG2};font-size:11px">{v}</text>')
LINES = [(1, "每题失败 1 次", None, 2.75), (3, "每题失败 3 次", "8 4", 2.25), (7, "每题失败 7 次", "2 4", 2.25), (0, "从不失败", "10 3 2 3", 2.25)]
ends = []
for fpp, lab, dash, w in LINES:
    fn = lambda s, fpp=fpp: rating(s, fpp * s, s / 3)
    c.path(fn, 1, 2000, n=600, stroke=FG, width=w, dash=dash)
    ends.append([c.Y(fn(2000)), lab, dash, w])
ends.sort()
for i in range(1, len(ends)):  # spread labels at least 17px apart
    ends[i][0] = max(ends[i][0], ends[i - 1][0] + 17)
for y, lab, dash, w in ends:
    d = f' stroke-dasharray="{dash}"' if dash else ""
    c.add(f'<line x1="{c.x1+8}" x2="{c.x1+30}" y1="{y:.1f}" y2="{y:.1f}" style="stroke:{FG};stroke-width:{w}"{d}/>')
    c.text(c.x1 + 36, y + 4.5, lab, fill=FG, size=12)
c.text(c.x1 - 8, c.y0 - 28, "假设每天 AC 不超过 8 次，", fill=FG2, size=11, anchor="end")
c.text(c.x1 - 8, c.y0 - 12, "平均每天解决 3 题（D = S/3）", fill=FG2, size=11, anchor="end")
c.save(before=bg)
