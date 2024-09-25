# Transformation2Dto3DLib

Здесь будут отчёты по изменениям.

17.09.24
Разбор алгоритмов для преобразования 2д в 3д. Ознакомление с базовым инструментарием. 
Проект будет состоять из двух частей:
  1) Библиотека (собственный разрабатываемый инструментарий). Она будет включать в себя сам алгоритм для перобразования, а также алгоритмы для определения и сборки схем.
  2) Клиентский интерфейс. визуальное представление для работы с библиотекой. Пока что не определено каким образом это будет выглядеть. Может в виде отдельной программы, может быть вообще не быть (можно всё релизовать через вызовы команд в Revit). По ходу дела будет виднее как лучше будет сделать эту часть сделать.

Первое время будет много исследовательской деятельности и разработки плана, поэтому первое время проект будет пустовать.

Далее будут просто полезные ссылки и возможные алгоритмы:

https://nplus1.ru/news/2017/08/24/hsp-network (какие нейронные сети могут пригодиться. Именно данная сеть не подходит под здачи)

https://primer.dynamobim.org/ru/index.html (параметрическое моделирование с помощью low-code, интегрируемая в Revit. Python)

Сеточные алгоритмы (Mesh Algorithms)

Сегментация и идентификация объектов. Может быть и не понадобится, но будет полезно для определения элемента

Сглубленное обучение (Deep Learning). Самый простой способ, но для него требуется слишком много примеров для обучения

  1) Триангуляция Делоне. Этот метод создает триангулированную сетку из набора точек, обеспечивая оптимальное распределение углов, что помогает избежать узких треугольников. Широко используется в геометрическом моделировании и компьютерной графике для создания сеток местности и управления формами объектов.
  2) Метод конечных элементов (Finite Element Analysis, FEA). Этот метод разбивает сложные геометрические формы на более простые элементы для численного анализа (механического, теплового и пр.).
  3) B-сплайны и NURBS (Неравномерные рациональные B-сплайны). Это математические модели, которые позволяют описывать сложные и гладкие формы. Используются в CAD-системах для проектирования и создания высококачественных кривых и поверхностей, таких как кузова автомобилей и промышленные компоненты.





20.09.24
План таков. Начать разрабатывать на основе нейронки для сегментации. Саму сборку можно будет реализовать различными способами, но до неё ещё далеко.
https://oajmist.com/index.php/12/article/download/147/80/351 (Обзор методов сегментации и обнаружения объектов на изображении в реальном времени для предотвращения аварийных ситуаций РЖД)
U-Net является лучшим решением в области сегментации объектов на растровом изображении.

Загружаю U-net, которая обучается на растрированных примерах. Работоспособность ещё следует проверить

23.09.24 и 25.09.24
Продолжается работа с нейронкой U-Net. Ей можно величить точность с помощью нормализации данных. Пока что аналогов без растрирования данных не найдено. Другие вариант это создать собственную нейронку или сделать глбокое обучение (для чего нужно много примеров для обучения). На то, чтобы научиться создавать собственные нейронки уйдёт много времени. Проект нужен только для визуализации, поэтому малая погрешность погоды не сделает.
(Отдельно не мог написать отчёт 23 сентября по прицине отключения света)
Также интегрирую плагин в Revit