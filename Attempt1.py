#from bokeh.layouts import row
from bokeh.plotting import figure
from bokeh.io import export_png

from bokeh.palettes import brewer
from bokeh.models import ColumnDataSource, LinearColorMapper


def reverse(n):
    rev=0
    while(n>0):
        d=n%10
        rev=rev*10+d
        n=n//10
    return rev


t = []
x = []
y = []
z = []
c = []
limit = 1
i = 89

a = i
b = reverse(a)
t.append(a)
j = 0;
n = a
while n > 0:
    d = n % 10
    y.append(0)
    x.append(-j)
    c.append(d)
    n = n // 10
    j = j + 1;

while limit < 25:
    # x = [q+(j/2) for q in x]
    k = 1
    while abs(a - b) > 0:
        a = a + b
        t.append(a)
        b = reverse(a)

        # plotting essentials
        n = a
        j = 0
        z = []
        while n > 0:
            d = n % 10
            y.append(-k)
            z.append(-j)
            c.append(d)
            n = n // 10
            j = j + 1

        # z = [q+(j/2) for q in z]
        x = x + z
        k = k + 1
        limit = limit + 1


mapper = LinearColorMapper(palette=brewer['Spectral'][10], low=0, high=9)

source = ColumnDataSource(data=dict(x=x, y=y, c=c))

plt = figure(title="Sequence of reverse then add", match_aspect = True, aspect_scale =1)
#plt.rect(x='x', y='y', width=1, height=1, source=source, fill_color={'field': 'c', 'transform': mapper}, line_color=None)
plt.circle(x='x', y='y',size = 10, source=source, fill_color={'field': 'c', 'transform': mapper}, line_color=None)
plt.background_fill_color = "#000000"
plt.axis.visible = False
plt.xgrid.visible = False
plt.ygrid.visible = False
#show(plt)

export_png(plt, filename="attempt1.png")