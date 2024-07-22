def build_shift_table(pattern):
  """Створити таблицю зсувів для алгоритму Боєра-Мура."""
  table = {}
  length = len(pattern)
  # Для кожного символу в підрядку встановлюємо зсув рівний довжині підрядка
  for index, char in enumerate(pattern[:-1]):
    table[char] = length - index - 1
  # Якщо символу немає в таблиці, зсув буде дорівнювати довжині підрядка
  table.setdefault(pattern[-1], length)
  return table

def boyer_moore_search(text, pattern):
  # Створюємо таблицю зсувів для патерну (підрядка)
  shift_table = build_shift_table(pattern)
  i = 0 # Ініціалізуємо початковий індекс для основного тексту

  # Проходимо по основному тексту, порівнюючи з підрядком
  while i <= len(text) - len(pattern):
    j = len(pattern) - 1 # Починаємо з кінця підрядка

    # Порівнюємо символи від кінця підрядка до його початку
    while j >= 0 and text[i + j] == pattern[j]:
      j -= 1 # Зсуваємось до початку підрядка

    # Якщо весь підрядок збігається, повертаємо його позицію в тексті
    if j < 0:
      return i # Підрядок знайдено

    # Зсуваємо індекс i на основі таблиці зсувів
    # Це дозволяє "перестрибувати" над неспівпадаючими частинами тексту
    i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

  # Якщо підрядок не знайдено, повертаємо -1
  return -1


def kmp_search(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    i = 0
    j = 0

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1

def rabin_karp_search(text, pattern):
    d = 256
    q = 101
    n = len(text)
    m = len(pattern)
    h = 1
    p = 0
    t = 0

    for i in range(m-1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if text[i:i+m] == pattern:
                return i

        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q

    return -1

import timeit

# Завантаження текстових файлів
with open('file1.txt', 'r', encoding='utf-8') as file:
    text1 = file.read()

with open('file2.txt', 'r', encoding='utf-8') as file:
    text2 = file.read()

# Вибір підрядків для пошуку
existing_substring1 = "integers[Math.min(jumpStep,"
non_existing_substring1 = "nonexistent substring"
existing_substring2 = "Садаладж П. Дж. NoSQL"
non_existing_substring2 = "nonexistent substring"

# Вимірювання часу для кожного алгоритму
def measure_time(algorithm, text, pattern):
    return timeit.timeit(lambda: algorithm(text, pattern), number=1000)

# Вимірювання часу для text1
time_boyer_moore_text1_existing = measure_time(boyer_moore_search, text1, existing_substring1)
time_boyer_moore_text1_non_existing = measure_time(boyer_moore_search, text1, non_existing_substring1)
time_kmp_text1_existing = measure_time(kmp_search, text1, existing_substring1)
time_kmp_text1_non_existing = measure_time(kmp_search, text1, non_existing_substring1)
time_rabin_karp_text1_existing = measure_time(rabin_karp_search, text1, existing_substring1)
time_rabin_karp_text1_non_existing = measure_time(rabin_karp_search, text1, non_existing_substring1)

# Вимірювання часу для text2
time_boyer_moore_text2_existing = measure_time(boyer_moore_search, text2, existing_substring2)
time_boyer_moore_text2_non_existing = measure_time(boyer_moore_search, text2, non_existing_substring2)
time_kmp_text2_existing = measure_time(kmp_search, text2, existing_substring2)
time_kmp_text2_non_existing = measure_time(kmp_search, text2, non_existing_substring2)
time_rabin_karp_text2_existing = measure_time(rabin_karp_search, text2, existing_substring2)
time_rabin_karp_text2_non_existing = measure_time(rabin_karp_search, text2, non_existing_substring2)

# Виведення результатів
print(f"Text1 (existing substring):")
print(f"Boyer-Moore: {time_boyer_moore_text1_existing}")
print(f"KMP: {time_kmp_text1_existing}")
print(f"Rabin-Karp: {time_rabin_karp_text1_existing}")

print(f"Text1 (non-existing substring):")
print(f"Boyer-Moore: {time_boyer_moore_text1_non_existing}")
print(f"KMP: {time_kmp_text1_non_existing}")
print(f"Rabin-Karp: {time_rabin_karp_text1_non_existing}")

print(f"Text2 (existing substring):")
print(f"Boyer-Moore: {time_boyer_moore_text2_existing}")
print(f"KMP: {time_kmp_text2_existing}")
print(f"Rabin-Karp: {time_rabin_karp_text2_existing}")

print(f"Text2 (non-existing substring):")
print(f"Boyer-Moore: {time_boyer_moore_text2_non_existing}")
print(f"KMP: {time_kmp_text2_non_existing}")
print(f"Rabin-Karp: {time_rabin_karp_text2_non_existing}")
