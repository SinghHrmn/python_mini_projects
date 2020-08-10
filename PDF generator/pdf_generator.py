from reportlab.pdfgen import canvas

filename = 'mydoc.pdf'
documentTitle = 'Document title!'
title = 'My title is a good one'
subtitle = 'Not a very google answer a is the of the'

textlines = ['a boy','is in love with the end thing']



pdf = canvas.Canvas(filename)
pdf.save()


