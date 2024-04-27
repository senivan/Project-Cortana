# Звіт. Тиждень 2

- Назва команди: `Cortana`
- Учасники: Сень Іван, Сазонова Вероніка, Шевчук Іван, Сидорчук Софія, Данііл Биков
- Використані інструменти: `Github Copilot`, `Google Gemini`, `Meta Codellama 70B`
- Вибрані завдання
    - Calculus - https://cms.ucu.edu.ua/mod/vpl/view.php?id=361853
    - Aliens - https://cms.ucu.edu.ua/mod/vpl/view.php?id=361849
    - Calendar - https://cms.ucu.edu.ua/mod/vpl/view.php?id=361854
    - Calculate expr - https://cms.ucu.edu.ua/mod/vpl/view.php?id=361852
    - star triangle frame - https://cms.ucu.edu.ua/mod/vpl/view.php?id=323793
    - target en - https://cms.ucu.edu.ua/mod/vpl/view.php?id=361851
- Посилання на гітхаб: [github-repo][https://github.com/senivan/Project-Cortana]

# Аналіз експериментів
1. ## Вплив рівня складності задачі на ефективність ШІ
    - ### Codellama
    Не впорався з жодною з задач, незалежно від промпту або її складності. Він не розуміє терміну "оптимізувати" та "рефакторити", тому надалі він не буде згадуватися в наступних пунктах.
    - ### Gemini
    Чим складнііша задача, тим більше проблем виникає в gemini. Він непогано справляється з задачею оптимізації коду, хоча часто він жертвує првильністю коду для того щоб його оптимізувати. ![](img.png) 
    Це більше проявляється на складних задачах, які розбиті на декілька функцій. Наприклад Target en або Calendar. Щодо стилю, то Gemini ігнорує правила PEP8, якшо прямо про це не сказати в промпті.
    Щодо того наскільки сильно він оптимізує код, то це під питанням. Здебільшого, якщо очевидних вузьких місць немає, то його оптимізація майже не впливає на швидкість виконання коду або на використання пам'яті. Проте він непогано справляється з скороченням коду.
    - ### Copliot
    Що дивно - Copilot не показав кращих результатів з точки оптимізації коду. Якщо в коді не має очевидних вузьких місць, то його покращення лише трохи краще за оригінальні. Щодо стилю, то copilot чудово справляється з тим щоб покрашити стиль коду. Він дотримується PEP8, незалежно від вказання в промпті. Щодо скорочення коду, то він також показав себе дуже добре.

2. ## Вплив різних промптів на результат
    Для обох ШІ більші задачі варто розбивати на декілька промптів, щоб вони могли краще їх зрозуміти. Також в промпті варто вказувати на те що ШІ має дотримуватись стилю PEP8, особливо це стосується Gemini. Більші задача варто розбивати на окремі функції, які не є великі, але є самодостатніми. Це дозволить ШІ краще їх оптимізувати.

3. ## Спільні риси згенерованих рішень
    Що Gemini, що Copilot - постійно намагаються скоротити код, незвадаючи на читабельність коду. Часто це саме скорочення веде до погіршення швидкості коду. Також ШІ можуть оптимізувати час ігноруючи пам'ять, або навпаки, вони не намагаються знайти золоту середину. 
    Обидвом ШІ дуже важко оптимізувати який немає очевидних проблем.

# Висновки
- Copilot та Gemini можуть допомогти оптимізувати код, але не треба на них покладатися повністю. Вони можуть погіршити швидкість коду або зробити його менш читабельним.
- Щодо допомоги з форматуванням кодом, то також не зрозуміло навіщо ШІ для цього коли є autopep8, black formatter для Python і Prettier для інших мов.

# Рекомендації
- Якщо ви все ж таки хочете використати ШІ для оптимізації, то варто перевіряти весь код який вони пишуть. В промти варто додавати лише самодостатні шматки коду, так ШІ краще справляється з оптимізацією. Після того відповідь ШІ варто відредугувати так щоб покращити читабельність коду.
- Для форматування коду краще використовувати форматтери, а не ШІ. Адже вони більш надійні та дають більше можливостей для налаштування.