import yaml
import json

code_names = {
    '200': 'OK',
    '202': 'Accepted',
    '208': 'Already reported',
    '304': 'Not Modified',
    '400': 'Bad Request',
    '403': 'Forbidden',
    '404': 'Not Found',
    '413': 'Payload Too Large',
    '429': 'Too Many Requests',
    '500': 'Internal Server Error'
}


with open('generated.md', 'w', encoding='utf8') as out:

    with open('prefix.md', 'r', encoding='utf8') as prefix_file:
        out.write(prefix_file.read())

    with open('categories/__order__.yml', 'r', encoding='utf8') as order:
        order = yaml.safe_load(order).get('order', [])

    for config_name in order:
        with open('categories/' + config_name + '.yml', 'r', encoding='utf8') as config_file:
            config = yaml.safe_load(config_file)

            out.write(f'\n\n* **{config["header"]}**:\n')

            for request in config['requests'].values():
                out.write('  * <details>\n')

                # Summary
                out.write('      <summary>')

                mark = request.get('mark')
                if mark is not None:
                    out.write(f'<b>[{mark}]</b> ')

                out.write(f'{request["name"]}: <code>{request["link"]}</code></summary>\n\n')

                # Description
                description = request.get('description', '')
                if isinstance(description, list):
                    if len(description) > 0:
                        description[0] = '<br>' + description[0]
                        for line in description:
                            out.write(f'      {line}\n\n')
                    else:
                        out.write(f'      <br>\n\n')
                else:
                    out.write(f'      <br>{description}\n\n')

                out.write(f'      ---\n\n')
                line_separator_written = True

                # Form
                form = request.get('form')
                if form is not None:
                    out.write('      **Пример формы:**\n      ```json\n      ')
                    out.write(json.dumps(form, indent=4, ensure_ascii=False).replace('\n', '\n      '))
                    out.write('\n      ```\n\n')
                    line_separator_written = False

                # Codes
                codes = request.get('codes')
                if codes is not None:
                    out.write('      ## Возвращаемые коды:\n')

                    for code, reasons in codes.items():
                        code = str(code)
                        out.write(f'      * `{code} {code_names.get(code, "code_names." + code)}`\n')
                        for reason in reasons:
                            out.write(f'        * {reason}\n')

                    out.write('\n      ---\n\n')
                    line_separator_written = True

                # Request
                request_example = request.get('request')
                if request_example is not None:
                    out.write(f'      **Пример запроса:** `{request_example}`\n\n')
                    line_separator_written = False

                # Body
                body = request.get('body')
                if body is not None:
                    out.write('      **Пример тела запроса:**\n      ```json\n      ')
                    out.write(json.dumps(body, indent=4, ensure_ascii=False).replace('\n', '\n      '))
                    out.write('\n      ```\n\n')
                    line_separator_written = False

                # Response
                response = request.get('response')
                if response is not None:
                    out.write('      **Пример ответа:**\n      ```json\n      ')
                    out.write(json.dumps(response, indent=4, ensure_ascii=False).replace('\n', '\n      '))
                    out.write('\n      ```\n\n')
                    line_separator_written = False

                # RegEx
                regex = request.get('regex')
                if regex is not None:
                    if not line_separator_written:
                        out.write('      ---\n\n')
                    for key, value in regex.items():
                        out.write(f'      **[{key}] RegEx**: `{value}`\n\n')
                    line_separator_written = False

                # Contract
                contract = request.get('contract')
                if contract is not None:
                    if not line_separator_written:
                        out.write('      ---\n\n')
                    out.write(f'      **Контракт:**: `{contract}`\n\n')

                out.write('      ---\n    </details>\n')

    with open('suffix.md', 'r', encoding='utf8') as suffix_file:
        out.write(suffix_file.read())


