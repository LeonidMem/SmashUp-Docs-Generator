### Общие ссылки:
* **Поделиться**
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
  * Получить мэшап на премодерации: `/uploads/moderators/mashup/[ID].mp3`
  * Получить обложку мэшапа на премодерации: `/uploads/moderators/mashup/[ID].png`

---

### Различные константы:
* **Плейлисты**
  * "Новинки": `1`
  * "Чарты | 24 часа": `2`
  * "Чарты | 7 дней": `3`
* **Биты настроек и прав пользователей**
  * Администратор: `0`
  * Модератор: `1`
  * Верифицированный пользователь: `2`
  * Включено проигрывание Explicit треков *(настройка)*: `3`
  * Пользователь забанен: `4`
  * Включена мульти-сессия *(настройка)*: `5`
  * Мэшапер: `6`

---

### Метки:
* **[T]** - нужен токен пользователя *(если он не указан, то всегда возвращается 401 код)*
* **[М]** - доступен только модераторам и администраторам *(если пользователь не является модератором или администратором, то всегда возвращается 403 код)*
* **[V]** - доступен только верифицированным пользователям, модераторам и администраторам *(если пользователь не является модератором или администратором, то всегда возвращается 403 код)*
* Если возвращаемые коды не указаны, то, значит, всегда возвращается **200** *(или 401, если метод помечен как [T]; аналогично с [M])*

### Запросы:


* **Статичные данные**:
  * <details>
      <summary><b>[T]</b> Жанры: <code>[GET] /static/genres</code></summary>

      <br>Возвращает списком все существующие на сайте жанры.

      ---

      **Пример ответа:**
      ```json
      [
          "рок",
          "рэп",
          "фолк"
      ]
      ```

      ---
    </details>
  * <details>
      <summary>Компиляции: <code>[GET] /static/compilations</code></summary>

      <br>Возвращает списком ID плейлистов, которые были помечены как компиляции.

      ---

      **Пример ответа:**
      ```json
      [
          1,
          2,
          3
      ]
      ```

      ---
    </details>


* **Авторизация и регистрация**:
  * <details>
      <summary>Авторизация: <code>[POST] /login</code></summary>

      <br>При успешной авторизации устанавливает новое значение куки "token".

      ---

      **Пример формы:**
      ```json
      {
          "username": "Admin",
          "__username__": "Поле username может быть как никнеймом, так и почтой",
          "password": "NonHashedPassword"
      }
      ```

      ## Возвращаемые коды:
      * `200 OK`
        * Если авторизация прошла успешно
      * `400 Bad Request`
        * Если отправлена некорректная почта или никнейм
        * Если пароль не подходит
      * `404 code_names.404`
        * Если пользователь с указанными почтой или никнеймом не найден

      ---

      **[username] RegEx**: `(?=^[а-яА-ЯёЁa-zA-Z0-9_ ]{4,32}$)(?!^\d+$)^.+$`

      **[password] RegEx**: `[a-zA-Z0-9-_=+()*&^%$#@!]{8,32}`

      ---
    </details>
  * <details>
      <summary>Регистрация: <code>[POST] /register</code></summary>

      <br>При успешной регистрации будет отправлено письмо на почту.

      ---

      **Пример формы:**
      ```json
      {
          "username": "УННВ",
          "email": "unnv@smashup.ru",
          "password": "NonHashedPassword"
      }
      ```

      ## Возвращаемые коды:
      * `200 OK`
        * Если письмо с подтверждением было отправлено на почту
      * `400 Bad Request`
        * Если отправлена некорректная почта, никнейм или пароль
        * Если пользователь с отправленными почтой или никнеймом уже зарегистрирован
        * Если письмо подтверждения уже было отправлено

      ---

      **[username] RegEx**: `(?=^[а-яА-ЯёЁa-zA-Z0-9_ ]{4,32}$)(?!^\d+$)^.+$`

      **[password] RegEx**: `[a-zA-Z0-9-_=+()*&^%$#@!]{8,32}`

      ---
    </details>
  * <details>
      <summary>Подтверждение регистрации: <code>[POST] /register_confirm?id=[ID]</code></summary>

      <br>При успешной авторизации устанавливает новое значение куки "token".

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если пользователь был зарегистрирован
      * `404 code_names.404`
        * Если подтверждение регистрации с указанными ID не найдено
      * `500 Internal Server Error`
        * Если произошла ошибка при создании пользователя

      ---

      **[ID] RegEx**: `{UUID RegEx}`

      ---
    </details>


* **Рекомендации**:
  * <details>
      <summary><b>[T]</b> v1: <code>[GET] /recommendations/v1</code></summary>

      <br>Возвращает списком ID рекомендованных мэшапов.

      ---

      **Пример ответа:**
      ```json
      [
          1,
          2,
          3,
          4,
          5,
          6,
          7,
          8,
          9,
          10
      ]
      ```

      ---
    </details>


* **Поиск**:
  * <details>
      <summary><b>[T]</b> Треков: <code>[GET] /search/tracks?query=[SEARCH_QUERY]</code></summary>

      <br>Возвращает списком сериализованные треки.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если всё хорошо и слава тебе, Господи
      * `400 Bad Request`
        * Если указан некорректный поисковой запрос

      ---

      **Пример запроса:** `/search/tracks?query=Поисковой%20запрос`

      **Пример ответа:**
      ```json
      [
          {
              "id": 83,
              "name": "Интро",
              "author": "УННВ",
              "imageUrl": "83"
          },
          {
              "id": 84,
              "name": "Ода под D",
              "author": "УННВ",
              "imageUrl": "83"
          }
      ]
      ```

      ---

      **[SEARCH_QUERY] RegEx**: `.+{4,32}`

      ---
    </details>
  * <details>
      <summary><b>[T]</b> Мэшапов: <code>[GET] /search/mashups?query=[SEARCH_QUERY]</code></summary>

      <br>Возвращает списком сериализованные мэашпы.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если всё хорошо и слава тебе, Господи
      * `400 Bad Request`
        * Если указан некорректный поисковой запрос

      ---

      **Пример запроса:** `/search/mashups?query=Поисковой%20запросс`

      **Пример ответа:**
      ```json
      [
          {
              "id": 207,
              "name": "Unlike 1.kla$ - Everything Почему",
              "authors": [
                  "CTAK_CO6AK"
              ],
              "imageUrl": "207",
              "explicit": true,
              "bitrate": 320044,
              "streams": 29,
              "likes": 4,
              "tracks": [
                  5781,
                  403
              ]
          },
          {
              "id": 428,
              "name": "everything you MFers talk about is 1.kla$",
              "authors": [
                  "MC Symon"
              ],
              "imageUrl": "428",
              "explicit": true,
              "bitrate": 128049,
              "streams": 21,
              "likes": 1,
              "tracks": [
                  7303,
                  402
              ]
          }
      ]
      ```

      ---

      **[SEARCH_QUERY] RegEx**: `.+{4,32}`

      ---
    </details>
  * <details>
      <summary><b>[T]</b> Плейлистов: <code>[GET] /search/playlists?query=[SEARCH_QUERY]</code></summary>

      <br>Возвращает списком сериализованные плейлисты.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если всё хорошо и слава тебе, Господи
      * `400 Bad Request`
        * Если указан некорректный поисковой запрос

      ---

      **Пример запроса:** `/search/playlists?query=Поисковой%20запросс`

      **Пример ответа:**
      ```json
      [
          {
              "id": 206,
              "name": "Все (мои) мэшапы из SoundCloud",
              "owner": "CnucDx",
              "imageUrl": "61a8f47d24e73d69ef53d1145976f97101d969a1c3cb719ad4a96d21b257949e",
              "streams": 0,
              "likes": 0,
              "mashups": []
          },
          {
              "id": 482,
              "name": "1.kla$ные мэшапы",
              "owner": "LeonidM",
              "imageUrl": "default",
              "streams": 12,
              "likes": 1,
              "tracks": [
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
              ]
          }
      ]
      ```

      ---

      **[SEARCH_QUERY] RegEx**: `.+{4,32}`

      ---
    </details>
  * <details>
      <summary><b>[T]</b> Пользователей: <code>[GET] /search/users?query=[SEARCH_QUERY]</code></summary>

      <br>Возвращает списком сериализованных пользователей.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если всё хорошо и слава тебе, Господи
      * `400 Bad Request`
        * Если указан некорректный поисковой запрос

      ---

      **Пример запроса:** `/search/users?query=Поисковой%20запросс`

      **Пример ответа:**
      ```json
      [
          {
              "id": 1146,
              "username": "Deephook81",
              "imageUrl": "default",
              "permissions": 0,
              "mashups": [],
              "playlists": []
          },
          {
              "id": 2463,
              "username": "Deep Space Audio",
              "imageUrl": "574dfbca5645bd8927a00617b466d3dcb3b204f85e15fa25e1249a4a86acfe5b",
              "permissions": 76,
              "streams": 12,
              "mashups": [
                  771,
                  772
              ],
              "playlists": [
                  123,
                  235
              ]
          }
      ]
      ```

      ---

      **[SEARCH_QUERY] RegEx**: `.+{4,32}`

      ---
    </details>


* **Мэшапы**:
  * <details>
      <summary>Получить: <code>[GET] /mashup/get?id=[IDS]</code></summary>

      <br>Возвращает списком сериализованные мэшапы.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если всё хорошо и слава тебе, Господи
      * `400 Bad Request`
        * Если некорректно указаны ID
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
              "imageUrl": "207",
              "explicit": true,
              "bitrate": 320044,
              "streams": 29,
              "likes": 4,
              "tracks": [
                  5781,
                  403
              ]
          },
          {
              "id": 428,
              "name": "everything you MFers talk about is 1.kla$",
              "authors": [
                  "MC Symon"
              ],
              "imageUrl": "428",
              "explicit": true,
              "bitrate": 128049,
              "streams": 21,
              "likes": 1,
              "tracks": [
                  7303,
                  402
              ]
          }
      ]
      ```

      ---

      **[IDS] RegEx**: `\d+(?:,\d+){0,}`

      ---
    </details>
  * <details>
      <summary><b>[M]</b> Получить неопубликованные: <code>[GET] /mashup/get_unpublished</code></summary>

      <br>Возвращает списком все сериализованные неопубликованные мэшапы.

      *Будет в будущем немного переработан*.

      ---

      **Пример запроса:** `/mashup/get?id=207,428`

      **Пример ответа:**
      ```json
      {
          "91": {
              "id": 91,
              "name": "Оксимироны из Мадагаскара",
              "owner": "mileon",
              "imageUrl": "91",
              "genres": [
                  "morph"
              ],
              "tracks": [
                  8954,
                  9559
              ],
              "tracksUrls": [
                  "https://www.youtube.com/watch?v=0VqGcjTA5xg [Уже добавлено под названием \"Пингвины Мадагаскара - Титры\"]"
              ],
              "explicit": false
          },
          "92": {
              "id": 92,
              "name": "Винсент боится самолета",
              "owner": "mileon",
              "imageUrl": "92",
              "genres": [
                  "рок"
              ],
              "tracks": [
                  9560,
                  9561
              ],
              "tracksUrls": [
                  "https://www.youtube.com/watch?v=YXd9GrSvNlw [Уже добавлено под названием \"Геннадий Горин - Самолёты\"]",
                  "https://music.yandex.ru/album/88356/track/15387033 [Альбом уже добавлен]"
              ],
              "explicit": false
          }
      }
      ```

      ---
    </details>
  * <details>
      <summary><b>[T]</b> Добавить прослушивание: <code>[POST] /mashup/stream/add?id=[ID]</code></summary>

      <br>**`[!]`** Должен быть вызван раз в 15 секунд, иначе прослушивание не будет добавлено.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если прослушивание добавилось
      * `208 Already reported`
        * Если менее 15 секунд назад было добавлено другое прослушивание
      * `400 Bad Request`
        * Если указан некорректный ID
        * Если мэшап с указанным ID не найден

      ---

      **[ID] RegEx**: `\d+`

      ---
    </details>
  * <details>
      <summary><b>[T]</b> Добавить лайк: <code>[POST] /mashup/like/add?id=[ID]</code></summary>

      <br>**`[!]`** В идеале должен быть хоть какой-то таймаут, но время таймаута надо обсудить.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если лайк добавился или уже был добавлен
      * `400 Bad Request`
        * Если указан некорректный ID
        * Если мэшап с указанным ID не найден

      ---

      **[ID] RegEx**: `\d+`

      ---
    </details>
  * <details>
      <summary><b>[T]</b> Убрать лайк: <code>[POST] /mashup/like/delete?id=[ID]</code></summary>

      <br>

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если лайк убрался или уже был убран
      * `400 Bad Request`
        * Если указан некорректный ID
        * Если мэшап с указанным ID не найден

      ---

      **[ID] RegEx**: `\d+`

      ---
    </details>
  * <details>
      <summary><b>[T]</b> Отправить мэшап на премодерацию или опубликовать его: <code>[POST] /mashup/upload</code></summary>

      <br>Возвращает сериализованный мэшап, если он был опубликован без премодерации, иначе пустую строку.

      Публикует мэшап, если запрос был отправлен верифицированным пользователем или модератором.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если всё хорошо и слава тебе, Господи
      * `400 Bad Request`
        * Если указан некорректный формат данных либо их вовсе не хватает в теле запроса
        * Если указан неизвестный автор в поле "mashupAuthor"
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
        * Если произошло какое-то IO исключение при работе с изображением
        * Если произошла какая-то ошибка при записи мэшапа в базу данных

      ---

      **Пример тела зароса:**
      ```json
      {
          "mashupFile": "[Base64 decoded mp3 file]",
          "imageFile": "[Base64 decoded png/jpg file]",
          "mashupName": "Мэшап без названия",
          "mashupAuthor": "LeonidM",
          "mashupAuthor__": "Указывается только в случае, если запрос был отправлен модератором с указанием другого автора",
          "explicit": false,
          "genres": [
              "рок"
          ],
          "tracks": [
              1,
              2,
              3
          ],
          "tracksUrls": [
              "https://www.youtube.com/watch?v=CQKxE8nBwSA",
              "https://music.yandex.ru/album/6319802/track/46804521"
          ],
          "tracksUrls__": "Доступно только для тех, кто отправляет мэшап на премодерацию, позже будет переделано"
      }
      ```

      **Пример ответа:**
      ```json
      {
          "id": 207,
          "name": "Unlike 1.kla$ - Everything Почему",
          "authors": [
              "CTAK_CO6AK"
          ],
          "imageUrl": "207",
          "explicit": true,
          "bitrate": 320044,
          "streams": 29,
          "likes": 4,
          "tracks": [
              5781,
              403
          ]
      }
      ```

      ---

      **[mashupName] RegEx**: `^[а-яА-ЯёЁa-zA-Z0-9_\$.,=+()*&^%$#@!\-?':\| ]{2,48}$`

      **[mashupAuthor] RegEx**: `(?=^[а-яА-ЯёЁa-zA-Z0-9_ ]{4,32}$)(?!^\d+$)^.+$`

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
        * Если хотя бы один из указанных ID не является ID какого-либо мэшапа

      ---

      **Пример запроса:** `/playlist/get?id=689,964`

      **Пример ответа:**
      ```json
      [
          {
              "id": 689,
              "name": "Пылесосен",
              "owner": "LeonidM",
              "imageUrl": "default",
              "description": "",
              "streams": 0,
              "likes": 0,
              "tracks": [
                  340,
                  648
              ]
          },
          {
              "id": 964,
              "name": "Убиты, но не вами",
              "owner": "LeonidM",
              "imageUrl": "44abc4f77cae0585df37f8e7437f064c9c568a62b98da3c7029dc66bfd934709",
              "description": "",
              "streams": 7,
              "likes": 1,
              "tracks": [
                  368,
                  509,
                  156,
                  114,
                  591,
                  377,
                  144,
                  376
              ]
          }
      ]
      ```

      ---

      **[IDS] RegEx**: `\d+(?:,\d+){0,}`

      ---
    </details>
  * <details>
      <summary><b>[T]</b> Создать: <code>[GET] /playlist/create</code></summary>

      <br>В случае успешного создания плейлиста, возвращает его в сериализованном виде, иначе пустую строку.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если плейлист был создан
      * `400 Bad Request`
        * Если у пользователя уже есть 10 плейлистов и при этом нет особых прав *(верификация, модератор, администратор)*
      * `500 Internal Server Error`
        * Если произошла ошибка при создании плейлиста

      ---

      **Пример ответа:**
      ```json
      {
          "id": 1294,
          "name": "Новый плейлист",
          "owner": "LeonidM",
          "imageUrl": "default",
          "description": "",
          "streams": 0,
          "likes": 0,
          "mashups": []
      }
      ```

      ---
    </details>
  * <details>
      <summary><b>[T]</b> Удалить: <code>[GET] /playlist/delete?id=[ID]</code></summary>

      <br>

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если плейлист был удалён
      * `400 Bad Request`
        * Если указан некорректный ID
        * Если плейлиста с указанным ID не существует
      * `403 Forbidden`
        * Если пользователь, который отправил запрос, не является создателем плейлиста

      ---

      **[ID] RegEx**: `\d+`

      ---
    </details>
  * <details>
      <summary><b>[T]</b> Изменить: <code>[POST] /mashup/edit</code></summary>

      <br>

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если всё хорошо и слава тебе, Господи
      * `400 Bad Request`
        * Если указан некорректный ID
        * Если плейлист с указанным ID не существует
        * Если указан некорректный формат данных в теле запроса
        * Если указанное название не соответствует регулярному выражению
        * Если изображение является прозрачным
        * Если изображение меньше 800х800 пикселей
      * `403 Forbidden`
        * Если пользователь, который отправил запрос, не является создателем плейлиста или вовсе забанен
      * `413 Payload Too Large`
        * Если изображение весит больше 5 МБ
      * `500 Internal Server Error`
        * Если невозможно декодировать изображение
        * Если произошло какое-то IO исключение при работе с изображением

      ---

      **Пример тела зароса:**
      ```json
      {
          "playlistName": "Новый плейлист",
          "imageFile": "[Base64 decoded png/jpg file]",
          "comment": "Нужно указывать поля только в том случае, если их значения были изменены пользователем"
      }
      ```

      **Пример ответа:**
      ```json
      {
          "playlistName": "Новый плейлист",
          "imageUrl": "61a8f47d24e73d69ef53d1145976f97101d969a1c3cb719ad4a96d21b257949e"
      }
      ```

      ---

      **[playlistName] RegEx**: `^[а-яА-ЯёЁa-zA-Z0-9_\$.,=+()*&^%$#@!\-?':\| ]{4,48}$`

      **[tracksUrls | YouTube] RegEx**: `https://www\.youtube\.com/watch\?v=([-a-zA-Z0-9_]{11})`

      **[tracksUrls | Яндекс.Музыка] RegEx**: `https://music\.yandex\.ru/album/(\d+)/track/(\d+)`

      ---
    </details>
  * <details>
      <summary><b>[T]</b> Добавить мэшап: <code>[POST] /playlist/add_mashup?playlistId=[PID]&id=[ID]</code></summary>

      <br>

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если мэшап был добавлен в плейлист
      * `400 Bad Request`
        * Если хотя бы один из указанных ID некорректный
        * Если мэшап с указанным ID не существует
        * Если плейлиста с указанным ID не существует
        * Если в плейлисте уже есть указанный мэшап
        * Если в плейлисте уже есть 100 мэшапов
      * `403 Forbidden`
        * Если пользователь, который отправил запрос, не является создателем плейлиста

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
      <summary><b>[T]</b> Добавить прослушивание: <code>[POST] /playlists/stream/add?id=[ID]</code></summary>

      <br>**`[!]`** Должен быть вызван раз в 60 секунд, иначе прослушивание не будет добавлено.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если прослушивание добавилось
      * `208 Already reported`
        * Если менее 60 секунд назад было добавлено другое прослушивание
      * `400 Bad Request`
        * Если указан некорректный ID
        * Если плейлист с указанным ID не найден

      ---

      **[ID] RegEx**: `\d+`

      ---
    </details>
  * <details>
      <summary><b>[T]</b> Добавить лайк: <code>[POST] /playlist/like/add?id=[ID]</code></summary>

      <br>**`[!]`** В идеале должен быть хоть какой-то таймаут, но время таймаута надо обсудить.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если лайк добавился или уже был добавлен
      * `400 Bad Request`
        * Если указан некорректный ID
        * Если плейлист с указанным ID не найден

      ---

      **[ID] RegEx**: `\d+`

      ---
    </details>
  * <details>
      <summary><b>[T]</b> Убрать лайк: <code>[POST] /playlist/like/delete?id=[ID]</code></summary>

      <br>

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если лайк убрался или уже был убран
      * `400 Bad Request`
        * Если указан некорректный ID
        * Если плейлист с указанным ID не найден

      ---

      **[ID] RegEx**: `\d+`

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

      **Пример запроса:** `/mashup/get?id=1,400`

      **Пример ответа:**
      ```json
      [
          {
              "id": 1,
              "name": "Я ПЫЛЬ",
              "owner": "MORGENSHTERN",
              "imageUrl": "1"
          },
          {
              "id": 400,
              "name": "Спортивные очки",
              "owner": "Буерак",
              "imageUrl": "398"
          }
      ]
      ```

      ---

      **[IDS] RegEx**: `\d+(?:,\d+){0,}`

      ---
    </details>
  * <details>
      <summary>Получить популярные мэшапы с этим треком: <code>[GET] /track/get_popular_mashups?id=[ID]</code></summary>

      <br>Возвращает списком все сериализованные мэшапы *(максимум 25)*, отсортированные по прослушиваниям.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если всё хорошо и слава тебе, Господи
      * `400 Bad Request`
        * Если указан некорректный ID

      ---

      **Пример запроса:** `/track/get_popular_mashups/get?id=248`

      **Пример ответа:**
      ```json
      [
          {
              "id": 26,
              "name": "不要离开院子",
              "owner": "ДЖКБ",
              "imageUrl": "26",
              "explicit": false,
              "bitrate": 320000,
              "streams": 208,
              "likes": 35,
              "tracks": [
                  904,
                  248
              ]
          },
          {
              "id": 166,
              "name": "ДОРАДУЛО",
              "owner": "Илья Муррка",
              "imageUrl": "166",
              "explicit": false,
              "bitrate": 192004,
              "streams": 202,
              "likes": 40,
              "tracks": [
                  52,
                  272,
                  248
              ]
          }
      ]
      ```

      ---

      **[ID] RegEx**: `\d+`

      ---
    </details>
  * <details>
      <summary>Получить случайные мэшапы с этим треком: <code>[GET] /track/get_popular_mashups?id=[ID]</code></summary>

      <br>Возвращает списком в случайном порядке сериализованные мэшапы *(максимум 25)*.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если всё хорошо и слава тебе, Господи
      * `400 Bad Request`
        * Если указан некорректный ID

      ---

      **Пример запроса:** `/mashup/get?id=248`

      **Пример ответа:**
      ```json
      [
          {
              "id": 166,
              "name": "ДОРАДУЛО",
              "owner": "Илья Муррка",
              "imageUrl": "166",
              "explicit": false,
              "bitrate": 192004,
              "streams": 202,
              "likes": 40,
              "tracks": [
                  52,
                  272,
                  248
              ]
          },
          {
              "id": 26,
              "name": "不要离开院子",
              "owner": "ДЖКБ",
              "imageUrl": "26",
              "explicit": false,
              "bitrate": 320000,
              "streams": 208,
              "likes": 35,
              "tracks": [
                  904,
                  248
              ]
          }
      ]
      ```

      ---

      **[ID] RegEx**: `\d+`

      ---
    </details>
  * <details>
      <summary><b>[V]</b> Опубликовать трек с YouTube: <code>[POST] /track/upload</code></summary>

      <br>Прямо сейчас загружать треки с YouTube'а могут только модераторы

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если всё хорошо и слава тебе, Господи
      * `400 Bad Request`
        * Если указан некорректный формат данных либо их вовсе не хватает в теле запроса
        * Если уже загружен трек по указанной ссылкой
        * Если изображение является прозрачным
        * Если изображение меньше 800х800 пикселей
      * `403 Forbidden`
        * Если пользователь, который отправил запрос, забанен
      * `413 Payload Too Large`
        * Если изображение весит больше 5 МБ
        * Если мэшап весит больше 20 МБ
      * `500 Internal Server Error`
        * Если невозможно декодировать изображение
        * Если произошло какое-то IO исключение при работе с изображением
        * Если произошла какая-то ошибка при записи трека в базу данных

      ---

      **Пример тела зароса:**
      ```json
      {
          "trackName": "Japan",
          "trackAuthor": "Aphex Twin",
          "link": "https://www.youtube.com/watch?v=S7c_OYURKss",
          "imageFile": "[Base64 decoded png/jpg file]"
      }
      ```

      ---

      **[trackName] RegEx**: `^[а-яА-ЯёЁa-zA-Z0-9_\$.,=+()*&^%$#@!\-?':\| ]{1,64}$`

      **[trackAuthor] RegEx**: `^[а-яА-ЯёЁa-zA-Z0-9_\$.,=+()*&^%$#@!\-?':\| ]{1,64}$`

      **[link] RegEx**: `https:\/\/www\\.youtube\\.com\/watch\\?v=([-a-zA-Z0-9_]{11})`

      ---
    </details>
  * <details>
      <summary><b>[V]</b> Запарсить альбом с Яндекс.Музыки: <code>[POST] /track/list_album?link=[LINK]</code></summary>

      <br>

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если всё хорошо и слава тебе, Господи
      * `400 Bad Request`
        * Если указана некорректная ссылка
        * Если уже загружен трек по указанной ссылкой
        * Если изображение является прозрачным
        * Если изображение меньше 800х800 пикселей
      * `403 Forbidden`
        * Если пользователь, который отправил запрос, забанен
      * `413 Payload Too Large`
        * Если изображение весит больше 5 МБ
        * Если мэшап весит больше 20 МБ
      * `500 Internal Server Error`
        * Если невозможно декодировать изображение
        * Если произошло какое-то IO исключение при работе с изображением
        * Если произошла какая-то ошибка при записи трека в базу данных

      ---

      **Пример запроса:** `/track/list_album?link=https://music.yandex.ru/album/3453403`

      **Пример ответа:**
      ```json
      {
          "imageLink": "https://avatars.yandex.net/get-music-content/28589/00051503.a.3453403-1/800x800",
          "tracks": [
              {
                  "author": "Aphex Twin",
                  "name": "Digeridoo"
              },
              {
                  "author": "Aphex Twin",
                  "name": "Flaphead"
              },
              {
                  "author": "Aphex Twin",
                  "name": "Phloam"
              },
              {
                  "author": "Aphex Twin",
                  "name": "Isoprophlex Aka Isopropanol"
              },
              {
                  "author": "Aphex Twin",
                  "name": "Polynomial-C"
              },
              {
                  "author": "Aphex Twin",
                  "name": "Tamphex Hedphuq Mix"
              },
              {
                  "author": "Aphex Twin",
                  "name": "Phlange Phace"
              },
              {
                  "author": "Aphex Twin",
                  "name": "Dodeccaheedron"
              },
              {
                  "author": "Aphex Twin",
                  "name": "Analogue Bubblebath"
              },
              {
                  "author": "Aphex Twin",
                  "name": "Metapharstic"
              },
              {
                  "author": "Aphex Twin",
                  "name": "We Have Arrived Aphex Twin QQT Mix"
              },
              {
                  "author": "Aphex Twin",
                  "name": "We Have Arrived Aphex Twin TTQ Mix"
              },
              {
                  "author": "Aphex Twin",
                  "name": "Digeridoo Live in Cornwall, 1990"
              }
          ]
      }
      ```

      ---

      **[link] RegEx**: `https:\/\/music\.yandex\.ru\/album\/(\d+)`

      ---
    </details>
  * <details>
      <summary><b>[V]</b> Загрузить альбом с Яндекс.Музыки: <code>[POST] /track/upload_tracks?link=[LINK]</code></summary>

      <br>

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если всё хорошо и слава тебе, Господи
      * `400 Bad Request`
        * Если указана некорректная ссылка
        * Если уже загружен трек по указанной ссылкой
        * Если изображение является прозрачным
        * Если изображение меньше 800х800 пикселей
      * `403 Forbidden`
        * Если пользователь, который отправил запрос, забанен
      * `413 Payload Too Large`
        * Если изображение весит больше 5 МБ
        * Если мэшап весит больше 20 МБ
      * `500 Internal Server Error`
        * Если невозможно декодировать изображение
        * Если произошло какое-то IO исключение при работе с изображением
        * Если произошла какая-то ошибка при записи трека в базу данных

      ---

      **Пример запроса:** `/track/list_album?link=https://music.yandex.ru/album/3453403`

      **Пример ответа:**
      ```json
      {
          "imageLink": "https://avatars.yandex.net/get-music-content/28589/00051503.a.3453403-1/800x800",
          "tracks": [
              {
                  "author": "Aphex Twin",
                  "name": "Digeridoo"
              },
              {
                  "author": "Aphex Twin",
                  "name": "Flaphead"
              },
              {
                  "author": "Aphex Twin",
                  "name": "Phloam"
              },
              {
                  "author": "Aphex Twin",
                  "name": "Isoprophlex Aka Isopropanol"
              },
              {
                  "author": "Aphex Twin",
                  "name": "Polynomial-C"
              },
              {
                  "author": "Aphex Twin",
                  "name": "Tamphex Hedphuq Mix"
              },
              {
                  "author": "Aphex Twin",
                  "name": "Phlange Phace"
              },
              {
                  "author": "Aphex Twin",
                  "name": "Dodeccaheedron"
              },
              {
                  "author": "Aphex Twin",
                  "name": "Analogue Bubblebath"
              },
              {
                  "author": "Aphex Twin",
                  "name": "Metapharstic"
              },
              {
                  "author": "Aphex Twin",
                  "name": "We Have Arrived Aphex Twin QQT Mix"
              },
              {
                  "author": "Aphex Twin",
                  "name": "We Have Arrived Aphex Twin TTQ Mix"
              },
              {
                  "author": "Aphex Twin",
                  "name": "Digeridoo Live in Cornwall, 1990"
              }
          ]
      }
      ```

      ---

      **[link] RegEx**: `https:\/\/music\.yandex\.ru\/album\/(\d+)`

      ---
    </details>
