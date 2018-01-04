from ROOT import TCanvas, TGraph, TMultiGraph
from array import array
from math import radians, tan

c1 = TCanvas('c1', 'Wire plane', 10000, 10000)
c1.SetFillColor(0)

n = 10000
x, y = array( 'd' ), array( 'd' )

mg = TMultiGraph()

for i in range(334):
	for j in range(n - 30*i):
		x.append(j)
		y.append(j + 30*i)
	gr = TGraph(n - 30*i, x, y)
	gr.SetLineWidth(1)
	mg.Add(gr)
	x, y = array("d"), array("d")

for i in range(334):
	for j in range(30 * i, n):
		x.append(j)
		y.append(j - 30*i)
	gr = TGraph((n - (30 * i)), x, y)
	gr.SetLineWidth(1)
	mg.Add(gr)
	x, y = array("d"), array("d")

mg.Draw("A")

raw_input()
