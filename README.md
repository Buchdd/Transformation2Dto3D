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
https://damassets.autodesk.net/content/dam/autodesk/draftr/2528/revit-ifc-handbook-ru.pdf

27.09.24
Было решено на время оставить использование ИИ, сфокусировавшись на атрибутах элементов. Каждый будет строиться по своему шаблону, согласно заявленному классу.
Почти подготовил экспериментльную версию, собирающую стены объекта.

01.10.24
Интеграция в Revit продолжается (пока что Revit не видит программу). Также не смог импортировать схему, созданную в автокаде (там у меня открылось) в Revit. Обратил внимаание, что тм не было произведено сборки по типу (каждый тип объекта должен находиться на собственном слое). Наша программа также должна решать и даанную задачу. Стало понятно, что нужно реализовать плагин и для автокада, чтобы он там собирал по слоям в идеале автономно.
в следующий раз постараюсь реализовать хоть какой-то импорт схемы в Revit. Изучу вопрос на счёт разбиения объекта по слоям. Если удатся правильно импортировать объект, то в целом сборку Revit реализует самостоятельно. Нужно только будет настроить удобный просмотр.

04.10.24
Было решено работать с нейросетью U-net по причине его высокой точности. Он используется в медицинских целях, поэтому лучше пока что не найти. Нейросетей, которые работали бы со схемами пока что нет. Только через растрирование (превращение векторной графики, описанной формлами, в графику где описается каждый пиксель).
Реализована база для работы с ней.

07.10.24
https://docs.aspose.com/imaging/python-net/installation/
https://www.convertapi.com/dwg-to-png/python
Появились проблемы с подключением библиотеки для Python для конвертации dwg в png

15.10.24
Было решено пересмотреть весть принцип построения. Проблема всё в том же U-net модели, которая давала бы довольно точные прогнозы (На практике ещё не выяснено, может после тестов её придётсся полностью исключить), но при этом нужно было бы растрировать изображение. Проблема заключается в том, что нужно придумать метод, который бы сопоставлял данные маски, полученной из модели, и сам чертёж. Научный руководитель сказал, что я банально не нашёл нужную нейросеть, хотя я уже месяц потратил на её поиски. Кроме решений с сегментированием приведённых выше, ничего нового не найдено и придётся решать именно таким образом. 

Был проведёно сравнение между U-net и GANs. 
Сегментация чертежа с помощью модели U-Net
Преимущества:
    Контроль над результатом: Используя U-Net для сегментации, вы можете более точно управлять тем, как различные элементы чертежа (стены, окна, двери) распределяются по слоям и семействам.
    Совместимость с Revit: Если элементы правильно сегментированы и размещены по семействам, то в Revit можно будет собрать архитектурную 3D-модель. Это обеспечит высший уровень детализации и точности.
    Возможность дальнейшей адаптации: Можно легко доработать или изменить существующие сегменты, если они будут неправильно интерпретированы.
Недостатки:
    Необходимость ручной настройки: Процесс сегментации может требовать значительного времени на подготовку и настройку модели, чтобы достичь высоких результатов.
    Потребность в качественных данных: Для обучении модели U-Net нужны качественные помеченные данные.
2) Генерация 3D-модели с помощью GANs
Преимущества:
  Автоматизация процесса: GANs могут генерировать 3D-модели полностью автономно на основе чертежей, что снижает трудозатраты на ручную сегментацию.
  Креативность: GAN-модели могут предлагать неожиданные и инновационные решения, создавая уникальные дизайны.
Недостатки:
  Непредсказуемость результатов: Генерация с помощью GANs может давать результаты, которые будут сложно интерпретировать или без точной связи с исходным чертежом.
  Ограниченная контроль: Вы не всегда сможете задать точные параметры для генерации объектов, что может вести к несоответствию стандартам и требованиям проекта.
  Необходимость большого объема данных: GANs требуют значительного объема обучающих данных для достижения качественных результатов.

Вывод таков: целесообразно воспользоваться U-net моделью для лучшего контроля. GANs можно использовать уже после реализации основной задачи для создания новых объектов окружения (к примеру).
https://www.kaggle.com/code/oluwatobiojekanmi/carla-image-semantic-segmentation-with-u-net/notebook#1.-Import-Required-Packages (Неплохой вариант сегментации вместе с обучающими материалами, но это не чертежи...)
Надо попробовать данный вариант и обучить его на других данных. Интересно, что из этого получится

18.10.2024
Перешёл на исключительно иностранные источники. Как оказаллось, в России в принципе ничего не продвигалось по этой технологии, по крайней мере последние несколько лет. Не проверял только диссертации и другие вкр. Но информации так мало, что было решено перейти на другие источники. 
По данной ниже книге удалось узнать, что TernausNet лучше U-Net в плане семантического сегмантирования архитектурных и конструкторских чертежей по точности, потерям и времени. Так же было предложено срезать частично свертку, что в данном случае повысить характеристики модели, так как недообученности не проявляется,
https://etd.lib.metu.edu.tr/upload/12624598/index.pdf (AUTO-CONVERSION FROM 2D DRAWING TO 3D MODEL WITH DEEP LEARNING)
Также есть полностью готовая нейронка Theia, которая сейчас находится в бете (недоделанная). Может на основе чертежа сгенерировать полноценную 3д модель. По сути выполняет большую часть работы. На следующей неделе буду тестировать данные нейронки
https://youtu.be/8yXVtbcKGho (пример её работы)

21.10.2024
Как и предполагалось Thiea beta всё ещё нельзя использовать. U-net точно с открытым кодом, а на счёт модификации ещё так и не узнал

22.10.2024
https://github.com/ternaus/TernausNet?tab=readme-ov-file
Здесь открытый доступ к TernausNet. Здесь же сразу он будет обучен на основе данных из Kaggle Carnava
https://www.modelo.io/
Аналог для конвертации двг в 3д модель. (Правда, я так и не нашёл там как загрузить чертёж, хотя чётко об этом говорится)
На рынке сейчас по большей части популярны автоматизированные инструменты лишь помогающие в генерации 3д-модели. Наша задача исключить человеческий ресурс для максимально быстрого и простого решения. 
Также я потихоньку заполняю документ со своими исследованиями и ссылками, чтобы не запутаться в решении. Этот же документ может послужить как документация к проекту.