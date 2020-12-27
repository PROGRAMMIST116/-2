text = 'мой папа из самых честных правил, Когда не в шутку занемог, он уважать себя заставил "n" лучше выдумать не мог'
print(' '.join([ word for word in text.split() if not word.startswith('м') ]))