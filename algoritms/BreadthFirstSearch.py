# Импортируем deque из модуля collections для эффективной работы с очередью
from collections import deque

# Граф социальных связей представлен в виде словаря:
# - Ключи: имена людей
# - Значения: списки их друзей (соседей в графе)
# Продавцы манго помечены суффиксом '_seller'
graph = {
    'you': ['alice', 'bob', 'claire'],  # У вас 3 друга
    'alice': ['peggy_seller'],  # Продавец на 1 уровне
    'bob': ['anuj_seller', 'peggy'],  # Продавец на 1 уровне
    'claire': ['thom', 'jonny_seller'],  # Продавец на 2 уровне
    'thom': [],
    'jonny_seller': [],
    'peggy_seller': [],
    'anuj_seller': [],
    'peggy': []
}


def is_mango_seller(person):
    """
    Проверяет, является ли человек продавцом манго.
    В этом примере проверяем по суффиксу '_seller'.
    В реальной задаче здесь могла бы быть сложная логика проверки.
    """
    return person.endswith('_seller')


def bfs_mango_seller(graph, start):
    """
    Алгоритм поиска в ширину (BFS) для нахождения ближайшего продавца манго.
    Возвращает первого найденного продавца с указанием уровня удаленности.
    """
    # Инициализируем очередь с начальным узлом и уровнем 0
    # Каждый элемент очереди - кортеж (имя, уровень)
    queue = deque()
    queue.append((start, 0))

    # Множество для отслеживания уже проверенных людей
    visited = set()
    visited.add(start)

    # Счетчик для отслеживания общего количества проверенных друзей
    total_friends = 0

    print("👉 Начинаем поиск с:", start)

    # Основной цикл поиска: работает пока очередь не пуста
    while queue:
        # Извлекаем первый элемент из очереди (FIFO - First In First Out)
        current_person, level = queue.popleft()

        # Если текущий человек - продавец, завершаем поиск
        if is_mango_seller(current_person):
            print(f"\n🔍 Всего проверено друзей: {total_friends}")
            return f"🎉 Ближайший продавец: {current_person} (уровень {level})"

        # Получаем список друзей текущего человека
        friends = graph.get(current_person, [])

        # Отладочный вывод информации о текущем шаге
        print(f"\n🔎 Уровень {level}: проверяем {current_person}")
        print(f"   Друзья {current_person}: {friends}")

        # Добавляем всех друзей текущего человека в очередь
        for friend in friends:
            if friend not in visited:
                visited.add(friend)  # Помечаем как посещенного
                queue.append((friend, level + 1))  # Увеличиваем уровень на 1
                total_friends += 1  # Увеличиваем счетчик проверок

    # Если очередь пуста и продавец не найден
    return "😞 Продавец не найден"


# Запускаем поиск от узла 'you'
result = bfs_mango_seller(graph, 'you')
print(result)
