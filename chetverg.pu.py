import fitz

print(fitz.__doc__)
doc = fitz.open('sus.pdf')
print(doc)
print(f'Количество страниц - {doc.page_count}')
print(doc.metadata)

#text = doc.pages()
#for t in text:
#    print(t)

page = doc.load_page(1)
doc_text = page.get_text('text')
print(doc_text)

if 'Хорь и Калиныч' in doc_text:
    print('есть')
else:
    print('нет')

areas = page.search_for('Хорь и Калиныч')
print(areas)
page.add_highlight_annot(areas)
doc.save('highlight.pdf')

for current_page in range(len(doc)):
    page = doc.load_page(current_page)
    text = page.get_text('text')
    print(text)
