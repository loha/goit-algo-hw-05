Result:

Text1 (existing substring):
Boyer-Moore: 0.17083396
KMP: 1.4568041420000002
Rabin-Karp: 2.808925199999999
Text1 (non-existing substring):
Boyer-Moore: 0.447043476
KMP: 3.2757958849999995
Rabin-Karp: 5.284251603000001
Text2 (existing substring):
Boyer-Moore: 0.5778965370000009
KMP: 5.117085413999998
Rabin-Karp: 6.809228431000001
Text2 (non-existing substring):
Boyer-Moore: 0.617103041
KMP: 4.903572068999999
Rabin-Karp: 8.190773848999996

В цілому:
Для існуючих підрядків в обох текстах, найшвидшим алгоритмом є Boyer-Moore.
Для неіснуючих підрядків в обох текстах, найшвидшим алгоритмом також є Boyer-Moore.
Алгоритм Кнута-Морріса-Пратта (KMP) займає друге місце за швидкістю, поступаючись алгоритму Боєра-Мура.
Алгоритм Рабіна-Карпа найповільніший серед трьох розглянутих алгоритмів.

Висновок
Алгоритм Боєра-Мура є найшвидшим для пошуку як існуючих, так і неіснуючих підрядків у текстах. Це робить його найефективнішим алгоритмом у загальному випадку для даних текстів. Алгоритм Кнута-Морріса-Пратта також демонструє хорошу продуктивність, хоча і трохи повільніший за алгоритм Боєра-Мура. Алгоритм Рабіна-Карпа показує найнижчу продуктивність серед розглянутих алгоритмів.