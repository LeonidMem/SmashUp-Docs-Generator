### Форматы JSON-ответов

* `status` — указывает статус-код. Присутствует **всегда**:
```json
{
    "status": "OK"
}
```

* `response` — хранит ответ на поступивший запрос. Может быть и массивом, и объектов в зависимости от запроса:
```json
{
    "status": "OK",
    "response": {
        "1": true,
        "2": false
    }
}
```

* `message` — код сообщения, который предполагается для того, чтобы показать пользователю:
```json
{
    "status": "Bad Request",
    "message": "login.bad_password"
}
```

* `problemInfo` — объект, показывающий проблемное место
  * `contract` — нарушенный контракт метода
    ```json
    {
        "status": "Bad Request",
        "message": "user.get.contract_violated",
        "problemInfo": {
            "contract": "(id == null) != (username == null)"
        }
    }
    ```
  * `badParameter` — некорректный параметр
    ```json
    {
        "status": "Bad Request",
        "message": "exception.bad_parameter",
        "problemInfo": {
            "badParameter": "id"
        }
    }
    ```

* `exceptionClass` — класс исключения. Появляется только при внутренней ошибки сервера:
* `stackTrace` — стектрейс исключения. Появляется только при внутренней ошибки сервера:
  ```json
  {
      "status": "Internal Server Error",
      "exceptionClass": "java.lang.IllegalStateException",
      "stackTrace": [
          "ru.smashup.application.controllers.entities.TrackController.get(TrackController.java:24)",
          "java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)",
          "java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:77)",
          "java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)",
          "java.base/java.lang.reflect.Method.invoke(Method.java:568)",
          "org.springframework.web.method.support.InvocableHandlerMethod.doInvoke(InvocableHandlerMethod.java:207)",
          "org.springframework.web.method.support.InvocableHandlerMethod.invokeForRequest(InvocableHandlerMethod.java:152)",
          "org.springframework.web.servlet.mvc.method.annotation.ServletInvocableHandlerMethod.invokeAndHandle(ServletInvocableHandlerMethod.java:118)",
          "org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter.invokeHandlerMethod(RequestMappingHandlerAdapter.java:884)",
          "org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter.handleInternal(RequestMappingHandlerAdapter.java:797)"
      ]
  }
  ```

### Общие ссылки:
* **Поделиться** _**[ТЕСТ]** Неактуально_
  * Мэшапом: `/share/mashup?id=[ID]&sharedBy=[NICKNAME]`
  * Плейлистом: `/share/playlist?id=[ID]&sharedBy=[NICKNAME]`
* **Контент**
  * Получить мэшап: `/uploads/mashup/[ID].mp3?bitrate=[MAX_BITRATE]`
  * Получить обложку мэшапа: `/uploads/mashup/[ID]_[SIZE].png`
    * Возможные значения SIZE: `[100x100, 400x400, 800x800]`
  * Получить обложку плейлиста: `/uploads/playlist/[ID]_[SIZE].png`
    * Возможные значения SIZE: `[100x100, 400x400, 800x800]`
  * Получить обложку трека: `/uploads/track/[ID]_[SIZE].png`
    * Возможные значения SIZE: `[100x100, 400x400, 800x800]`
  * Получить аватар пользователя: `/uploads/user/[ID]_[SIZE].png`
    * Возможные значения SIZE: `[100x100, 400x400, 800x800]`
  * Получить мэшап на премодерации: `/uploads/moderators/mashup/[ID].mp3` _**[ТЕСТ]** Неактуально_
  * Получить обложку мэшапа на премодерации: `/uploads/moderators/mashup/[ID].png` _**[ТЕСТ]** Неактуально_

---

### Различные константы:
* **Плейлисты:** _**[ТЕСТ]** Неактуально_
  * "Новинки": `1`
  * "Чарты | 24 часа": `2`
  * "Чарты | 7 дней": `3`
* **Биты прав пользователей:**
  * Администратор: `0`
  * Модератор: `1`
  * Верифицированный пользователь: `2`
  * Мэшапер: `3`
  * Пользователь забанен: `4`
* **Биты настроек пользователей:**
  * Включено проигрывание Explicit треков: `0`
  * Включена мульти-сессия: `1`
* **Биты статусов мэшапов:**
  * Explicit: `0`
  * #mashup: `0`
  * \[alt]: `0`

---

### Метки:
* **[T]** - нужен токен пользователя в заголовке `Authorization` в формате `Bearer token` *(если он не указан, то всегда возвращается 401 код)*
* **[М]** - доступен только модераторам и администраторам *(если пользователь не является модератором или администратором, то всегда возвращается 403 код)*
* **[V]** - доступен только верифицированным пользователям, модераторам и администраторам *(если пользователь не является модератором или администратором, то всегда возвращается 403 код)*
* Если возвращаемые коды не указаны, то, значит, всегда возвращается **200** *(или 401, если метод помечен как [T]; аналогично с [M])*

### Запросы:


* **Авторизация и регистрация**:
  * <details>
      <summary>Авторизация: <code>[POST] /login</code></summary>

      <br>Поле `username` может быть как никнеймом, так и почтой.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если авторизация прошла успешно
      * `400 Bad Request`
        * Если отправлена некорректная почта или никнейм
        * Если пароль не подходит
      * `404 Not Found`
        * Если пользователь с указанными почтой или никнеймом не найден

      ---

      **Пример тела запроса:**
      ```json
      {
          "username": "Admin",
          "password": "NonHashedPassword"
      }
      ```

      **Пример ответа:**
      ```json
      {
          "id": 1,
          "username": "SmashUp",
          "imageUrl": "default",
          "backgroundColor": 16777215,
          "permissions": 7,
          "token": "d404f899-eac6-4355-a651-1a8daef84550"
      }
      ```

      ---

      **[username] RegEx**: `(?=^[а-яА-ЯёЁa-zA-Z0-9_ ]{4,32}$)(?!^\d+$)^.+$`

      **[password] RegEx**: `[a-zA-Z0-9-_=+()*&^%$#@!]{8,32}`

      ---
    </details>
  * <details>
      <summary>Регистрация: <code>[POST] /register</code></summary>

      <br>**[ТЕСТ]** Письмо на почту не отправляется. Коды неактуальны и не обновлены. Ответ актуален только для теста

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если письмо с подтверждением было отправлено на почту
      * `400 Bad Request`
        * Если отправлена некорректная почта, никнейм или пароль
        * Если пользователь с отправленными почтой или никнеймом уже зарегистрирован
        * Если письмо подтверждения уже было отправлено

      ---

      **Пример тела запроса:**
      ```json
      {
          "username": "УННВ",
          "email": "unnv@smashup.ru",
          "password": "NonHashedPassword"
      }
      ```

      **Пример ответа:**
      ```json
      {
          "id": 1,
          "username": "SmashUp",
          "imageUrl": "default",
          "backgroundColor": 16777215,
          "permissions": 7,
          "token": "d404f899-eac6-4355-a651-1a8daef84550"
      }
      ```

      ---

      **[username] RegEx**: `(?=^[а-яА-ЯёЁa-zA-Z0-9_ ]{4,32}$)(?!^\d+$)^.+$`

      **[password] RegEx**: `[a-zA-Z0-9-_=+()*&^%$#@!]{8,32}`

      ---
    </details>


* **Пользователи**:
  * <details>
      <summary>Получить: <code>[GET] /user/get?id=[ID] *или* /user/get?username=[USERNAME] *или* /user/get?token=[TOKEN]</code></summary>

      <br>Возвращает сериализованного пользователя.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если всё хорошо и слава тебе, Господи
      * `400 Bad Request`
        * Если нарушен контракт
        * Если некорректно указан ID, USERNAME или TOKEN
      * `404 Not Found`
        * Если пользователь с указанным ID, USERNAME или TOKEN не был найден

      ---

      **Пример запроса:** `/user/get?id=1`

      **Пример ответа:**
      ```json
      [
          {
              "id": 1,
              "username": "SmashUp",
              "imageUrl": "1",
              "backgroundColor": 16777215,
              "permissions": 1
          }
      ]
      ```

      ---

      **[ID] RegEx**: `\d+`

      **[USERNAME] RegEx**: `(?=^[а-яА-ЯёЁa-zA-Z0-9_ ]{4,32}$)(?!^\d+$)^.+$`

      **[TOKEN] RegEx**: `[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}`

      ---

      **Контракт:**: `Only one of parameters (id, username, token) must be specified`

      ---
    </details>
  * <details>
      <summary><b>[T]</b> Получить настройки: <code>[GET] /user/get_settings</code></summary>

      <br>Возвращает настройки пользователя, сделавшего этот запрос.

      ---

      **Пример запроса:** `/user/get_settings`

      **Пример ответа:**
      ```json
      {
          "settings": 1
      }
      ```

      ---
    </details>
  * <details>
      <summary><b>[T]</b> Изменить настройки: <code>[GET] /user/change_setting?bit=[BIT]&value=[VALUE]</code></summary>

      <br>Изменяет настройки пользователя, сделавшего этот запрос, и возвращает новое значение бит-маски.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если настройка была изменена
      * `304 Not Modified`
        * Если настройка уже имела нужное значение
      * `404 Not Found`
        * Если настройка с указанным битом не найдена

      ---

      **Пример запроса:** `/user/get_settings`

      **Пример ответа:**
      ```json
      {
          "settings": 1
      }
      ```

      ---

      **[BIT] RegEx**: `\d+`

      **[VALUE] RegEx**: `0|1`

      ---
    </details>


* **Мэшапы**:
  * <details>
      <summary>Получить: <code>[GET] /mashup/get?id=[IDS]</code></summary>

      <br>Возвращает списком сериализованные мэшапы.

      `duration` указан в мс.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если всё хорошо и слава тебе, Господи
      * `400 Bad Request`
        * Если некорректно указаны ID
      * `404 Not Found`
        * Если хотя бы один из указанных ID не является ID какого-либо мэшапа

      ---

      **Пример запроса:** `/mashup/get?id=207,428`

      **Пример ответа:**
      ```json
      [
          {
              "id": 207,
              "name": "Unlike 1.kla$ - Everything Почему",
              "authors": [
                  "CTAK_CO6AK"
              ],
              "genres": [
                  "рэп"
              ],
              "tracks": [
                  5781,
                  403
              ],
              "imageUrl": "207",
              "backgroundColor": 16777215,
              "statuses": 1,
              "albumId": -1,
              "likes": 4,
              "streams": 29,
              "bitrate": 320044,
              "duration": 1800000
          },
          {
              "id": 428,
              "name": "everything you MFers talk about is 1.kla$",
              "authors": [
                  "MC Symon"
              ],
              "genres": [
                  "рэп"
              ],
              "tracks": [
                  7303,
                  402
              ],
              "imageUrl": "428",
              "backgroundColor": 16777215,
              "statuses": 1,
              "albumId": -1,
              "likes": 1,
              "streams": 21,
              "bitrate": 128049,
              "duration": 1000000
          }
      ]
      ```

      ---

      **[IDS] RegEx**: `\d+(?:,\d+){1,100}`

      ---
    </details>
  * <details>
      <summary><b>[T]</b> Добавить прослушивание: <code>[POST] /mashup/add_stream?id=[ID]</code></summary>

      <br>**`[!]`** В будущем нужно будет ещё учитывать задержку между запросами.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если прослушивание добавилось
      * `400 Bad Request`
        * Если указан некорректный ID
      * `404 Not Found`
        * Если мэшап с указанным ID не найден

      ---

      **[ID] RegEx**: `\d+`

      ---
    </details>
  * <details>
      <summary><b>[T]</b> Добавить лайк: <code>[POST] /mashup/add_like?id=[ID]</code></summary>

      <br>**`[!]`** В идеале должен быть хоть какой-то таймаут, но время таймаута надо обсудить.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если лайк добавился или уже был добавлен
      * `304 Not Modified`
        * Если лайк уже был
      * `400 Bad Request`
        * Если указан некорректный ID
      * `404 Not Found`
        * Если мэшап с указанным ID не найден

      ---

      **[ID] RegEx**: `\d+`

      ---
    </details>
  * <details>
      <summary><b>[T]</b> Убрать лайк: <code>[POST] /mashup/remove_like?id=[ID]</code></summary>

      <br>

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если лайк убрался
      * `304 Not Modified`
        * Если лайка не было
      * `400 Bad Request`
        * Если указан некорректный ID
      * `404 Not Found`
        * Если мэшап с указанным ID не найден

      ---

      **[ID] RegEx**: `\d+`

      ---
    </details>
  * <details>
      <summary><b>[T]</b> Получить лайки: <code>[GET] /mashup/get_likes?id=[IDS]</code></summary>

      <br>Данный запрос не проверяет, существует ли мэшап с указанным ID, в таком случае, сервер просто вернёт `false`.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если всё хорошо и слава тебе, Господи
      * `400 Bad Request`
        * Если указан некорректный ID

      ---

      **Пример ответа:**
      ```json
      {
          "1": true,
          "2": false,
          "3": false,
          "4": true
      }
      ```

      ---

      **[IDS] RegEx**: `\d+(?:,\d+){1,100}`

      ---
    </details>
  * <details>
      <summary><b>[T]</b> Отправить мэшап на премодерацию или опубликовать его: <code>[POST] /mashup/upload</code></summary>

      <br>Публикует мэшап, если запрос был отправлен верифицированным пользователем или модератором.

      * `authors` — ID авторов, включая самого пользователя, что его опубликовывает в случае, если мэшап выкладывается самим создателем, а не модератором.

      * `albumId` — ID альбома-плейлиста, к которому будет прикреплён мэшап. Если значение меньше 0, то привязки не будет.

      * `tracks` — ID треков

      * `tracksUrls` — ссылки треков

      * `statusesUrls` — ссылки на подтверждение статуса мэшапа (например, пост в `#mashup` или `[alt]`)

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если всё хорошо и слава тебе, Господи
      * `202 Accepted`
        * Если мэшап был добавлен в базу данных, но что-то пошло не так при сохранении изображении или мэшапа
      * `400 Bad Request`
        * Если указан некорректный формат данных, либо их вовсе не хватает в теле запроса
        * Если мэшап с таким названием уже существует
        * Если пользователь, не будучи модератором или верифицированным пользователем, прикрепил меньше 2 треков суммарно в "tracks" и "tracksUrls"
        * Если мэшап представлен не .mp3 файлом
        * Если изображение является прозрачным
        * Если изображение меньше 800х800 пикселей
      * `403 Forbidden`
        * Если пользователь, который отправил запрос, забанен
      * `413 Payload Too Large`
        * Если изображение весит больше 5 МБ
        * Если мэшап весит больше 20 МБ
      * `429 Too Many Requests`
        * Если пользователь достиг ограничения загрузки в 5 мэшапов в час
      * `500 Internal Server Error`
        * Если невозможно декодировать изображение

      ---

      **Пример тела запроса:**
      ```json
      {
          "basedMashupFile": "[Base64 decoded mp3 file]",
          "basedImageFile": "[Base64 decoded png/jpg file]",
          "name": "Мэшап без названия",
          "authors": [
              1,
              2
          ],
          "explicit": false,
          "albumId": -1,
          "tracks": [
              1,
              2,
              3
          ],
          "tracksUrls": [
              "https://www.youtube.com/watch?v=CQKxE8nBwSA",
              "https://music.yandex.ru/album/6319802/track/46804521"
          ],
          "statusesUrls": [
              "https://vk.com/mashup?w=wall-39786657_711087"
          ],
          "genres": [
              "рок"
          ]
      }
      ```

      ---

      **[name] RegEx**: `^[а-яА-ЯёЁa-zA-Z0-9_\$.,=+()*&^%$#@!\-?':\| ]{2,48}$`

      **[tracksUrls | YouTube] RegEx**: `https://www\.youtube\.com/watch\?v=([-a-zA-Z0-9_]{11})`

      **[tracksUrls | Яндекс.Музыка] RegEx**: `https://music\.yandex\.ru/album/(\d+)/track/(\d+)`

      ---
    </details>


* **Плейлисты**:
  * <details>
      <summary>Получить: <code>[GET] /playlist/get?id=[IDS]</code></summary>

      <br>Возвращает списком сериализованные плейлисты.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если всё хорошо и слава тебе, Господи
      * `400 Bad Request`
        * Если некорректно указаны ID
      * `404 Not Found`
        * Если хотя бы один из указанных ID не является ID какого-либо мэшапа

      ---

      **Пример запроса:** `/playlist/get?id=689,964`

      **Пример ответа:**
      ```json
      [
          {
              "id": 689,
              "name": "Пылесосен",
              "description": "",
              "authors": [
                  "LeonidM"
              ],
              "imageUrl": "default",
              "backgroundColor": 16777215,
              "type": "playlist",
              "mashups": [
                  340,
                  648
              ],
              "likes": 0,
              "streams": 0
          },
          {
              "id": 964,
              "name": "Убиты, но не вами",
              "description": "",
              "authors": [
                  "LeonidM"
              ],
              "imageUrl": "964",
              "backgroundColor": 16777215,
              "mashups": [
                  368,
                  509,
                  156,
                  114,
                  591,
                  377,
                  144,
                  376
              ],
              "likes": 1,
              "streams": 7
          }
      ]
      ```

      ---

      **[IDS] RegEx**: `\d+(?:,\d+){1,100}`

      ---
    </details>
  * <details>
      <summary><b>[T]</b> Создать: <code>[GET] /playlist/create</code></summary>

      <br>**[ТЕСТ]** Пока нет проверки на наличие 10 плейлистов.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если плейлист был создан
      * `400 Bad Request`
        * Если у пользователя уже есть 10 плейлистов и при этом нет особых прав *(верификация, модератор, администратор)*
      * `500 Internal Server Error`
        * Если произошла ошибка при создании плейлиста

      ---

      **Пример тела запроса:**
      ```json
      {
          "name": "Какое-то имя",
          "description": "Какое-то описание",
          "basedImageFile": "[Base64 decoded png/jpg file]",
          "__basedImageFile__": "Параметр 'basedImageFile' необязателен"
      }
      ```

      **Пример ответа:**
      ```json
      {
          "id": 100,
          "name": "Какое-то имя",
          "description": "Какое-то описание",
          "authors": [
              "LeonidM"
          ],
          "imageUrl": "100",
          "backgroundColor": 16777215,
          "mashups": [],
          "likes": 0,
          "streams": 0
      }
      ```

      ---
    </details>
  * <details>
      <summary><b>[T]</b> Добавить мэшап: <code>[POST] /playlist/add_mashup?playlistId=[PID]&id=[ID]</code></summary>

      <br>**[ТЕСТ]** Пока нет проверки на наличие 100 мэшапов.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если мэшап был добавлен в плейлист
      * `400 Bad Request`
        * Если хотя бы один из указанных ID некорректный
        * Если в плейлисте уже есть указанный мэшап
        * Если в плейлисте уже есть 100 мэшапов
      * `403 Forbidden`
        * Если пользователь, который отправил запрос, не является создателем плейлиста
      * `404 Not Found`
        * Если мэшап с указанным ID не существует
        * Если плейлиста с указанным ID не существует

      ---

      **[PID] RegEx**: `\d+`

      **[ID] RegEx**: `\d+`

      ---
    </details>
  * <details>
      <summary><b>[T]</b> Удалить мэшап: <code>[POST] /playlist/remove_mashup?playlistId=[PID]&id=[ID]</code></summary>

      <br>

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если мэшап был удалён из плейлиста
      * `400 Bad Request`
        * Если хотя бы один из указанных ID некорректный
        * Если мэшап с указанным ID не существует
        * Если плейлиста с указанным ID не существует
        * Если в плейлисте нет указанного мэшапа
      * `403 Forbidden`
        * Если пользователь, который отправил запрос, не является создателем плейлиста

      ---

      **[PID] RegEx**: `\d+`

      **[ID] RegEx**: `\d+`

      ---
    </details>
  * <details>
      <summary><b>[T]</b> Добавить прослушивание: <code>[POST] /playlists/add_stream?id=[ID]</code></summary>

      <br>**`[!]`** В будущем нужно будет ещё учитывать задержку между запросами.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если прослушивание добавилось
      * `400 Bad Request`
        * Если указан некорректный ID
      * `404 Not Found`
        * Если плейлист с указанным ID не найден

      ---

      **[ID] RegEx**: `\d+`

      ---
    </details>
  * <details>
      <summary><b>[T]</b> Добавить лайк: <code>[POST] /playlist/add_like?id=[ID]</code></summary>

      <br>**`[!]`** В идеале должен быть хоть какой-то таймаут, но время таймаута надо обсудить.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если лайк добавился или уже был добавлен
      * `400 Bad Request`
        * Если указан некорректный ID
      * `404 Not Found`
        * Если плейлист с указанным ID не найден

      ---

      **[ID] RegEx**: `\d+`

      ---
    </details>
  * <details>
      <summary><b>[T]</b> Убрать лайк: <code>[POST] /playlist/remove_like?id=[ID]</code></summary>

      <br>

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если лайк убрался или уже был убран
      * `400 Bad Request`
        * Если указан некорректный ID
      * `404 Not Found`
        * Если плейлист с указанным ID не найден

      ---

      **[ID] RegEx**: `\d+`

      ---
    </details>
  * <details>
      <summary><b>[T]</b> Получить лайки: <code>[GET] /playlist/get_likes?id=[IDS]</code></summary>

      <br>Данный запрос не проверяет, существует ли плейлист с указанным ID, в таком случае, сервер просто вернёт `false`.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если всё хорошо и слава тебе, Господи
      * `400 Bad Request`
        * Если указан некорректный ID

      ---

      **Пример ответа:**
      ```json
      {
          "1": true,
          "2": false,
          "3": false,
          "4": true
      }
      ```

      ---

      **[IDS] RegEx**: `\d+(?:,\d+){1,100}`

      ---
    </details>


* **Треки**:
  * <details>
      <summary>Получить: <code>[GET] /track/get?id=[IDS]</code></summary>

      <br>Возвращает списком сериализованные треки.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если всё хорошо и слава тебе, Господи
      * `400 Bad Request`
        * Если некорректно указаны ID
        * Если хотя бы один из указанных ID не является ID какого-либо трека

      ---

      **Пример запроса:** `/track/get?id=1,400`

      **Пример ответа:**
      ```json
      [
          {
              "id": 1,
              "name": "Я ПЫЛЬ",
              "authors": [
                  "MORGENSHTERN"
              ],
              "imageUrl": "1",
              "backgroundColor": 16777215,
              "link": "https://music.yandex.ru/album/9647864/"
          },
          {
              "id": 400,
              "name": "Спортивные очки",
              "authors": [
                  "Буерак"
              ],
              "imageUrl": "398",
              "backgroundColor": 16777215,
              "link": "https://music.yandex.ru/album/5512081/"
          }
      ]
      ```

      ---

      **[IDS] RegEx**: `\d+(?:,\d+){1,100}`

      ---
    </details>
  * <details>
      <summary><b>[V]</b> Опубликовать с Яндекс.Музыки: <code>[GET] /track/upload/yandex_music?albumId=[ID]</code></summary>

      <br>Возвращает списком сериализованные треки.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если всё хорошо и слава тебе, Господи
      * `202 Accepted`
        * Если трек был добавлен в базу данных, но что-то пошло не так при сохранении изображении
      * `400 Bad Request`
        * Если некорректно указан ID
      * `404 Not Found`
        * Если альбом с указанным ID не найден в Яндекс.Музыке
      * `409 Conflict`
        * Если указанный альбом уже есть в базе данных

      ---

      **Пример запроса:** `/track/upload/yandex_music?id=4712222`

      **Пример ответа:**
      ```json
      [
          {
              "id": 1,
              "name": "Я ПЫЛЬ",
              "authors": [
                  "MORGENSHTERN"
              ],
              "imageUrl": "1",
              "backgroundColor": 16777215,
              "link": "https://music.yandex.ru/album/9647864/"
          },
          {
              "id": 400,
              "name": "Спортивные очки",
              "authors": [
                  "Буерак"
              ],
              "imageUrl": "398",
              "backgroundColor": 16777215,
              "link": "https://music.yandex.ru/album/5512081/"
          }
      ]
      ```

      ---

      **[ID] RegEx**: `\d+`

      ---
    </details>
  * <details>
      <summary><b>[V]</b> Опубликовать с видео YouTube: <code>[GET] /track/upload/youtube/video</code></summary>

      <br>Возвращает сериализованный трек.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если всё хорошо и слава тебе, Господи
      * `202 Accepted`
        * Если трек был добавлен в базу данных, но что-то пошло не так при сохранении изображении
      * `400 Bad Request`
        * Если указан некорректный формат данных, либо их вовсе не хватает в теле запроса
      * `409 Conflict`
        * Если указанное видео уже есть в базе данных

      ---

      **Пример тела запроса:**
      ```json
      {
          "videoId": "dQw4w9WgXcQ",
          "authors": [
              "Rick Astley"
          ],
          "name": "Never Gonna Give You Up"
      }
      ```

      **Пример ответа:**
      ```json
      {
          "id": 10000,
          "name": "Never Gonna Give You Up",
          "authors": [
              "Rick Astley"
          ],
          "imageUrl": "10000",
          "backgroundColor": 16777215,
          "link": "https://youtube.com/watch?v=dQw4w9WgXcQ"
      }
      ```

      ---
    </details>


* **Поиск**:
  * <details>
      <summary><b>[T]</b> Треков: <code>[GET] /track/search?query=[SEARCH_QUERY]</code></summary>

      <br>Возвращает списком сериализованные треки, максимум 25.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если всё хорошо и слава тебе, Господи
      * `400 Bad Request`
        * Если указан некорректный поисковой запрос

      ---

      **Пример запроса:** `/track/search?query=Поисковой%20запрос`

      **Пример ответа:**
      ```json
      [
          {
              "id": 83,
              "name": "Интро",
              "authors": [
                  "УННВ"
              ],
              "imageUrl": "83",
              "backgroundColor": 16777215,
              "link": "https://music.yandex.ru/album/6983656/"
          },
          {
              "id": 84,
              "name": "Ода под D",
              "authors": [
                  "УННВ"
              ],
              "imageUrl": "83",
              "backgroundColor": 16777215,
              "link": "https://music.yandex.ru/album/6983656/"
          }
      ]
      ```

      ---

      **[SEARCH_QUERY] RegEx**: `.+{4,32}`

      ---
    </details>
  * <details>
      <summary><b>[T]</b> Мэшапов: <code>[GET] /mashup/search?query=[SEARCH_QUERY]</code></summary>

      <br>Возвращает списком сериализованные мэшапы, максимум 25.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если всё хорошо и слава тебе, Господи
      * `400 Bad Request`
        * Если указан некорректный поисковой запрос

      ---

      **Пример запроса:** `/mashup/search?query=1.kla$`

      **Пример ответа:**
      ```json
      [
          {
              "id": 207,
              "name": "Unlike 1.kla$ - Everything Почему",
              "authors": [
                  "CTAK_CO6AK"
              ],
              "genres": [
                  "рэп"
              ],
              "tracks": [
                  5781,
                  403
              ],
              "imageUrl": "207",
              "backgroundColor": 16777215,
              "statuses": 1,
              "albumId": -1,
              "likes": 4,
              "streams": 29,
              "bitrate": 320044,
              "duration": 1800000
          },
          {
              "id": 428,
              "name": "everything you MFers talk about is 1.kla$",
              "authors": [
                  "MC Symon"
              ],
              "genres": [
                  "рэп"
              ],
              "tracks": [
                  7303,
                  402
              ],
              "imageUrl": "428",
              "backgroundColor": 16777215,
              "statuses": 1,
              "albumId": -1,
              "likes": 1,
              "streams": 21,
              "bitrate": 128049,
              "duration": 1000000
          }
      ]
      ```

      ---

      **[SEARCH_QUERY] RegEx**: `.+{4,32}`

      ---
    </details>
  * <details>
      <summary><b>[T]</b> Плейлистов: <code>[GET] /playlist/search?query=[SEARCH_QUERY]</code></summary>

      <br>Возвращает списком сериализованные плейлисты, максимум 25.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если всё хорошо и слава тебе, Господи
      * `400 Bad Request`
        * Если указан некорректный поисковой запрос

      ---

      **Пример запроса:** `/playlist/search?query=мэшапы`

      **Пример ответа:**
      ```json
      [
          {
              "id": 206,
              "name": "Все (мои) мэшапы из SoundCloud",
              "description": "",
              "authors": [
                  "CnucDx"
              ],
              "imageUrl": "206",
              "backgroundColor": 16777215,
              "mashups": [],
              "likes": 0,
              "streams": 0
          },
          {
              "id": 482,
              "name": "1.kla$ные мэшапы",
              "description": "",
              "authors": [
                  "LeonidM"
              ],
              "imageUrl": "default",
              "backgroundColor": 16777215,
              "mashups": [
                  138,
                  136,
                  228,
                  227,
                  207,
                  191,
                  190,
                  185,
                  123,
                  124,
                  125,
                  126,
                  117,
                  287,
                  262,
                  311,
                  417,
                  415,
                  353,
                  451,
                  511,
                  479,
                  486,
                  132,
                  399,
                  463,
                  535,
                  585,
                  448,
                  469,
                  601,
                  611,
                  538,
                  584,
                  694,
                  772
              ],
              "likes": 1,
              "streams": 12
          }
      ]
      ```

      ---

      **[SEARCH_QUERY] RegEx**: `.+{4,32}`

      ---
    </details>
  * <details>
      <summary><b>[T]</b> Пользователей: <code>[GET] /user/search?query=[SEARCH_QUERY]</code></summary>

      <br>Возвращает списком сериализованных пользователей, максимум 25.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если всё хорошо и слава тебе, Господи
      * `400 Bad Request`
        * Если указан некорректный поисковой запрос

      ---

      **Пример запроса:** `/user/search?query=Deep`

      **Пример ответа:**
      ```json
      [
          {
              "id": 1146,
              "username": "Deephook81",
              "imageUrl": "default",
              "backgroundColor": 16777215,
              "permissions": 0
          },
          {
              "id": 2463,
              "username": "Deep Space Audio",
              "imageUrl": "2463",
              "backgroundColor": 16777215,
              "permissions": 76
          }
      ]
      ```

      ---

      **[SEARCH_QUERY] RegEx**: `.+{4,32}`

      ---
    </details>


* **Модерация**:
  * <details>
      <summary><b>[M]</b> Изменить неопубликованный мэшап: <code>[POST] /moderation/edit_unpublished_mashup</code></summary>

      <br>Возвращает сериализованный неопубликованный мэшап.

      *`statuses` — список статусов в виде строк, в данный момент доступны следующие:

        * `EXPLICIT` — присутствует ненормативная лексика

        * `MASHUP` — мэшап был опубликован в #mashup

        * `ALT` — мэшап был опубликован в \[alt]

      * Значения остальных полей JSON можно найти в `Мэшапы -> Отправить мэшап на премодерацию или опубликовать его`.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если всё хорошо и слава тебе, Господи
      * `400 Bad Request`
        * Если указан некорректный формат данных, либо их вовсе не хватает в теле запроса
      * `404 Not Found`
        * Если неопубликованный мэшап с указанным ID не был найден

      ---

      **Пример тела запроса:**
      ```json
      {
          "id": 1,
          "name": "Мэшап без названия",
          "authors": [
              1,
              2
          ],
          "statuses": [
              "MASHUP",
              "EXPLICIT"
          ],
          "albumId": -1,
          "tracks": [
              1,
              2,
              3
          ],
          "tracksUrls": [
              "https://www.youtube.com/watch?v=CQKxE8nBwSA",
              "https://music.yandex.ru/album/6319802/track/46804521"
          ],
          "statusesUrls": [
              "https://vk.com/mashup?w=wall-39786657_711087"
          ],
          "genres": [
              "рок"
          ]
      }
      ```

      **Пример ответа:**
      ```json
      {
          "name": "Мэшап без названия",
          "authors": [
              1,
              2
          ],
          "statuses": [
              "MASHUP",
              "EXPLICIT"
          ],
          "albumId": -1,
          "tracks": [
              1,
              2,
              3
          ],
          "tracksUrls": [
              "https://www.youtube.com/watch?v=CQKxE8nBwSA",
              "https://music.yandex.ru/album/6319802/track/46804521"
          ],
          "statusesUrls": [
              "https://vk.com/mashup?w=wall-39786657_711087"
          ],
          "genres": [
              "рок"
          ]
      }
      ```

      ---

      **[name] RegEx**: `^[а-яА-ЯёЁa-zA-Z0-9_\$.,=+()*&^%$#@!\-?':\| ]{2,48}$`

      **[tracksUrls | YouTube] RegEx**: `https://www\.youtube\.com/watch\?v=([-a-zA-Z0-9_]{11})`

      **[tracksUrls | Яндекс.Музыка] RegEx**: `https://music\.yandex\.ru/album/(\d+)/track/(\d+)`

      ---
    </details>
  * <details>
      <summary><b>[M]</b> Публикация неопубликованного мэшапа: <code>[POST] /moderation/publish_mashup?id=[ID]</code></summary>

      <br>Возвращает сериализованный мэшап.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если всё хорошо и слава тебе, Господи
      * `202 Accepted`
        * Если мэшап был добавлен в базу данных, но что-то пошло не так при сохранении изображении или мэшапа
      * `400 Bad Request`
        * Если указан некорректный формат данных, либо их вовсе не хватает в теле запроса
      * `404 Not Found`
        * Если неопубликованный мэшап с указанным ID не был найден

      ---

      **Пример ответа:**
      ```json
      {
          "id": 207,
          "name": "Unlike 1.kla$ - Everything Почему",
          "authors": [
              "CTAK_CO6AK"
          ],
          "genres": [
              "рэп"
          ],
          "tracks": [
              5781,
              403
          ],
          "imageUrl": "207",
          "backgroundColor": 16777215,
          "statuses": 1,
          "albumId": -1,
          "likes": 4,
          "streams": 29,
          "bitrate": 320044,
          "duration": 1800000
      }
      ```

      ---

      **[ID] RegEx**: `\d+`

      ---
    </details>
  * <details>
      <summary><b>[M]</b> Отклонить неопубликованный мэшап: <code>[POST] /moderation/reject_mashup</code></summary>

      <br>

      ---

      **Пример тела запроса:**
      ```json
      {
          "id": 1,
          "reason": "Оффбит"
      }
      ```

      ---
    </details>
