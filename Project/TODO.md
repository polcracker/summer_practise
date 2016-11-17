# =====================================================================================================================
# TODO LIST
# =====================================================================================================================
DATE: 18.09.2016        VERSION: v0.1.0
    [+] Write class for work with web-page. Using Grab.
    [+] Write main class
    [-] Write logger (deprecated)
# =====================================================================================================================
DATE: 23.09.2016        VERSION: v0.2.0-v0.3.0
    [+] Create garbage folder (this folder have some modules and some testing code)
    [+] Get region (by parentId of subject)
        https://rosreestr.ru/wps/PA_FCCLPGUOReqService/ru.fccland.pgu.online.request?
        ru.fccland.ibmportal.spring.portlet.handler.BeanNameParameterHandlerMapping-PATH=%2FChildsRegionController
        &ru.fccland.ibmportal.spring.portlet.dispatcher.DispatcherServiceServlet.directRequest=x&parentId=110000000000
    [+] Get city type (by parentId of region)
        https://rosreestr.ru/wps/PA_FCCLPGUOReqService/ru.fccland.pgu.online.request?
        ru.fccland.ibmportal.spring.portlet.handler.BeanNameParameterHandlerMapping-PATH=%2FChildsRegionTypesController
        &ru.fccland.ibmportal.spring.portlet.dispatcher.DispatcherServiceServlet.directRequest=x&parentId=112402000000
    [+] Get city (by parentId of region)
        https://rosreestr.ru/wps/PA_FCCLPGUOReqService/ru.fccland.pgu.online.request?
        ru.fccland.ibmportal.spring.portlet.handler.BeanNameParameterHandlerMapping-PATH=%2FChildsRegionController
        &ru.fccland.ibmportal.spring.portlet.dispatcher.DispatcherServiceServlet.directRequest=x&parentId=112402000000
        &settlement_type=set0&add_settlement_type=true
# =====================================================================================================================
DATE: 24.09.2016        VERSION: v0.4.0
    [+] Создать UI
    [?] Реализовать режимы DEBUG и RELEASE
    [+] Отселектить сие добро курлоv, заполнить гуи. Затем зафулить грабом форму и посмотреть что получилось.
      Надеюсь все будет зи.
    [+] Проверить форму на работоспособность через граб. Сможет ли граб получить страницу по прямому воткнутому значение
      в комбобокс.
    [+] Написать классы для работы с webdriver
    [-] Rewrite README.md
# =====================================================================================================================
DATE: 27.09.2016        VERSION: v0.4.5
    [?] Отдебажить смену региона. Есть подозрения что не выполнено запоминание айдишников
    [+] Лютая дичь происходит. Нужно парсить нп отдельно. Пишем регулярку под это. будем парсить города отдельно
    [?] Исправить проблему с вылетом при отправке формы
    [+] Накинуть обработчиков исключений
# =====================================================================================================================
DATE: 28.09.2016        VERSION: v0.5.1
    [+] Исправить проблему с вылетом при отправке формы
    [+] Накинуть обработчиков исключений
    [+] Добавить очистку формы
    [+] Добавить пустоту в комбобоксы
# =====================================================================================================================
DATE: 30.09.2016        VERSION: v0.6.1
    [+] Выгрузить в csv
    [?] Рефакторинг кода
    [+] Тестирование и отладка в режиме релиз ("DEBUG = False")
# =====================================================================================================================
DATE: 02.10.2016        VERSION: v1.0.1
    [+] Исправить косяки со скрываемостью хрома
    [-] ИСправить косяк с простоем фантома
    [+] Исправление мелких недочетов
# =====================================================================================================================
OTHER DAYS:
    [+] Написать парсер выходной инфы. Реализовать отдельное ui с таблицей под сие какишь.
    [?] Рефакторинг кода
    [?] Ускорить работу программы при GET-запросах
    [+] Исключить лишние пустоты в комбобоксах
# =====================================================================================================================
