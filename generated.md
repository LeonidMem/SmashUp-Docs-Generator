### Общие ссылки:
* **Поделиться**
  * Мэшапом: `https://smashup.ru/share/mashup?id=[ID]&sharedBy=[NICKNAME]`
  * Плейлистом: `https://smashup.ru/share/playlist?id=[ID]&sharedBy=[NICKNAME]`

---

### Метки:
* **[T]** - нужен токен пользователя *(если он не указан, то всегда возвращается 401 код)*
* **[М]** - доступен только модераторам и администраторам *(если пользователь не является модератором или администратором, то всегда возвращается 403 код)*
* **[?]** - причина возвращаемого кода, помеченная этим символом, не будет отправлена в теле ответа
* Если возвращаемые коды не указаны, то, значит, всегда возвращается **200** *(или 401, если метод помечен как [T]; аналогично с [M])*

### Запросы:


* **Статичные данные**:
  * <details>
      <summary><b>[T]</b> Жанры: <code>[GET] https://smashup.ru/static/genres</code></summary>

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
      <summary>Компиляции: <code>[GET] https://smashup.ru/static/compilations</code></summary>

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
      <summary>Авторизация: <code>[POST] https://smashup.ru/login</code></summary>

      <br>При успешной авторизации устанавливает новое значение куки "token".

      ---

      **Пример формы:**
      ```json
      {
          "username": "Admin",
          "password": "NonHashedPassword",
          "comment": "Надо подумать над алгоритмом хэширования пароля на клиенте"
      }
      ```

      ---

      **[username] RegEx**: `(?=^[а-яА-ЯёЁa-zA-Z0-9_ ]{4,32}$)(?!^\d+$)^.+$`

      **[password] RegEx**: `[a-zA-Z0-9-_=+()*&^%$#@!]{8,32}`

      ---
    </details>
  * <details>
      <summary>Регистрация: <code>[POST] https://smashup.ru/register</code></summary>

      <br>При успешной регистрации устанавливает новое значение куки "token".

      ---

      **Пример формы:**
      ```json
      {
          "username": "УННВ",
          "email": "unnv@smashup.ru",
          "password1": "NonHashedPassword",
          "password2": "NonHashedPassword",
          "comment": "Сейчас протокол требует два пароля, но будет переделан на один"
      }
      ```

      ---

      **[username] RegEx**: `(?=^[а-яА-ЯёЁa-zA-Z0-9_ ]{4,32}$)(?!^\d+$)^.+$`

      **[password] RegEx**: `[a-zA-Z0-9-_=+()*&^%$#@!]{8,32}`

      ---
    </details>


* **Рекомендации**:
  * <details>
      <summary><b>[T]</b> v1: <code>[GET] https://smashup.ru/recommendations/v1</code></summary>

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
      <summary><b>[T]</b> Треков: <code>[GET] https://smashup.ru/search/tracks?query=[SEARCH_QUERY]</code></summary>

      <br>Возвращает списком сериализованные треки.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если всё хорошо и слава тебе, Господи
      * `400 Bad Request`
        * Если указан некорректный поисковой запрос

      ---

      **Пример запроса:** `https://smashup.ru/search/tracks?query=Поисковой%20запрос`

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
      <summary><b>[T]</b> Мэшапов: <code>[GET] https://smashup.ru/search/mashups?query=[SEARCH_QUERY]</code></summary>

      <br>Возвращает списком сериализованные мэашпы.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если всё хорошо и слава тебе, Господи
      * `400 Bad Request`
        * Если указан некорректный поисковой запрос

      ---

      **Пример запроса:** `https://smashup.ru/search/mashups?query=Поисковой%20запросс`

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
      <summary><b>[T]</b> Плейлистов: <code>[GET] https://smashup.ru/search/playlists?query=[SEARCH_QUERY]</code></summary>

      <br>Возвращает списком сериализованные плейлисты.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если всё хорошо и слава тебе, Господи
      * `400 Bad Request`
        * Если указан некорректный поисковой запрос

      ---

      **Пример запроса:** `https://smashup.ru/search/playlists?query=Поисковой%20запросс`

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
      <summary><b>[T]</b> Пользователей: <code>[GET] https://smashup.ru/search/users?query=[SEARCH_QUERY]</code></summary>

      <br>Возвращает списком сериализованных пользователей.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если всё хорошо и слава тебе, Господи
      * `400 Bad Request`
        * Если указан некорректный поисковой запрос

      ---

      **Пример запроса:** `https://smashup.ru/search/users?query=Поисковой%20запросс`

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
      <summary>Получить: <code>[GET] https://smashup.ru/mashup/get?id=[IDS]</code></summary>

      <br>Возвращает списком сериализованные мэшапы.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если всё хорошо и слава тебе, Господи
      * `400 Bad Request`
        * Если некорректно указаны ID
        * Если хотя бы один из указанных ID не является ID какого-либо мэшапа

      ---

      **Пример запроса:** `https://smashup.ru/mashup/get?id=207,428`

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
      <summary><b>[M]</b> Получить неопубликованные: <code>[GET] https://smashup.ru/mashup/get_unpublished</code></summary>

      <br>Возвращает списком все сериализованные неопубликованные мэшапы.

      *Будет в будущем немного переработан*.

      ---

      **Пример запроса:** `https://smashup.ru/mashup/get?id=207,428`

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
      <summary><b>[T]</b> Добавить прослушивание: <code>[POST] https://smashup.ru/mashup/stream/add?id=[ID]</code></summary>

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
      <summary><b>[T]</b> Добавить лайк: <code>[POST] https://smashup.ru/mashup/like/add?id=[ID]</code></summary>

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
      <summary><b>[T]</b> Убрать лайк: <code>[POST] https://smashup.ru/mashup/like/delete?id=[ID]</code></summary>

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
      <summary><b>[T]</b> Отправить мэшап на премодерацию или опубликовать его: <code>[POST] https://smashup.ru/mashup/upload</code></summary>

      <br>Возвращает сериализованный мэшап, если он был опубликован без премодерации, иначе пустую строку.

      Публикует мэшап, если запрос был отправлен верифицированным пользователем или модератором.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если всё хорошо и слава тебе, Господи
      * `400 Bad Request`
        * [?] Если указан некорректный формат данных либо их вовсе не хватает в теле запроса
        * Если указан неизвестный автор в поле "mashupAuthor"
        * Если мэшап с таким названием уже существует
        * [?] Если пользователь, не будучи модератором или верифицированным пользователем, прикрепил меньше 2 треков суммарно в "tracks" и "tracksUrls"
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

      **[tracksUrls | YouTube] RegEx**: `https:\/\/www\.youtube\.com\/watch\?v=([-a-zA-Z0-9_]{11})`

      **[tracksUrls | Яндекс.Музыка] RegEx**: `https:\/\/music\.yandex\.ru\/album\/(\d+)\/track\/(\d+)`

      ---
    </details>


* **Плейлисты**:
  * <details>
      <summary>Получить: <code>[GET] https://smashup.ru/playlist/get?id=[IDS]</code></summary>

      <br>Возвращает списком сериализованные плейлисты.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если всё хорошо и слава тебе, Господи
      * `400 Bad Request`
        * Если некорректно указаны ID
        * Если хотя бы один из указанных ID не является ID какого-либо мэшапа

      ---

      **Пример запроса:** `https://smashup.ru/playlist/get?id=689,964`

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
      <summary><b>[T]</b> Создать: <code>[GET] https://smashup.ru/playlist/create</code></summary>

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
      <summary><b>[T]</b> Удалить: <code>[GET] https://smashup.ru/playlist/delete?id=[ID]</code></summary>

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
      <summary><b>[T]</b> Изменить: <code>[POST] https://smashup.ru/mashup/edit</code></summary>

      <br>

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если всё хорошо и слава тебе, Господи
      * `400 Bad Request`
        * [?] Если указан некорректный ID
        * Если плейлист с указанным ID не существует
        * [?] Если указан некорректный формат данных в теле запроса
        * Если указанное название не соответствует регулярному выражению
        * Если изображение является прозрачным
        * Если изображение меньше 800х800 пикселей
      * `403 Forbidden`
        * Если пользователь, который отправил запрос, не является создателем плейлиста или вовсе забанен
      * `413 Payload Too Large`
        * Если изображение весит больше 5 МБ
      * `500 Internal Server Error`
        * Если невозможно декодировать изображение
        * [?] Если произошло какое-то IO исключение при работе с изображением

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

      **[tracksUrls | YouTube] RegEx**: `https:\/\/www\.youtube\.com\/watch\?v=([-a-zA-Z0-9_]{11})`

      **[tracksUrls | Яндекс.Музыка] RegEx**: `https:\/\/music\.yandex\.ru\/album\/(\d+)\/track\/(\d+)`

      ---
    </details>
  * <details>
      <summary><b>[T]</b> Добавить мэшап: <code>[POST] https://smashup.ru/playlist/add_mashup?playlistId=[PID]&id=[ID]</code></summary>

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
      <summary><b>[T]</b> Удалить мэшап: <code>[POST] https://smashup.ru/playlist/remove_mashup?playlistId=[PID]&id=[ID]</code></summary>

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
      <summary><b>[T]</b> Добавить прослушивание: <code>[POST] https://smashup.ru/playlists/stream/add?id=[ID]</code></summary>

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
      <summary><b>[T]</b> Добавить лайк: <code>[POST] https://smashup.ru/playlist/like/add?id=[ID]</code></summary>

      <br>**`[!]`** В идеале должен быть хоть какой-то таймаут, но время таймаута надо обсудить.

      ---

      ## Возвращаемые коды:
      * `200 OK`
        * Если лайк добавился или уже был добавлен
      * `400 Bad Request`
        * Если указан некорректный ID
        * Если плейлисат с указанным ID не найден

      ---

      **[ID] RegEx**: `\d+`

      ---
    </details>
  * <details>
      <summary><b>[T]</b> Убрать лайк: <code>[POST] https://smashup.ru/playlist/like/delete?id=[ID]</code></summary>

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
