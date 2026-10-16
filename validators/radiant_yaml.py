"""Read the strict YAML subset used by Radiant data blocks, with the standard library only.

Every document accepted here is valid YAML with the same value, so readers with
a full parser agree with this one. Anything outside the subset is refused with
the line number instead of being guessed.
"""

import re

KEY = re.compile(r"([A-Za-z_][A-Za-z0-9_-]*):(?: (.*))?$")
INTEGER = re.compile(r"-?(?:0|[1-9][0-9]*)$")
ESCAPES = {'"': '"', "\\": "\\", "n": "\n"}
# Words YAML 1.1 or 1.2 reads as booleans or nulls in some spelling; only the
# lowercase true, false and null are accepted, everything else needs quotes.
TYPED_WORDS = {"y", "Y", "yes", "Yes", "YES", "n", "N", "no", "No", "NO", "true", "True", "TRUE",
               "false", "False", "FALSE", "on", "On", "ON", "off", "Off", "OFF", "null", "Null",
               "NULL", "~"}
SPECIAL_FLOATS = {".inf", "-.inf", "+.inf", ".nan"}
FLOW_INDICATORS = set(",[]{}")
VALUE_START = re.compile(r"(?:^|:[ ]+|(?:^|[ ])-[ ]+|[\[,][ ]*)$")


class YamlError(ValueError):
    def __init__(self, number, message):
        super().__init__(f"linha {number}: {message}")


def quoted_pair(text, index, quote):
    """Length of an escape that keeps a quoted value open: \\x in double, '' in single."""
    if quote == '"' and text[index] == "\\":
        return 2
    if quote == "'" and text[index:index + 2] == "''":
        return 2
    return 0


def strip_comment(text):
    """Split off a trailing comment, honoring quotes that open a value.

    A quote inside a plain value, as in "it's", is a literal character. Returns
    the content and whether a comment followed it.
    """
    quote = None
    index = 0
    while index < len(text):
        char = text[index]
        skip = quoted_pair(text, index, quote)
        if skip:
            index += skip
            continue
        if quote:
            if char == quote:
                quote = None
        elif char in "\"'" and VALUE_START.search(text[:index]):
            quote = char
        elif char == "#" and (index == 0 or text[index - 1] in " \t"):
            return text[:index], True
        index += 1
    return text, False


def logical_lines(text):
    lines = []
    for number, raw in enumerate(text.splitlines(), start=1):
        body = raw.lstrip(" ")
        if body.startswith("\t"):
            raise YamlError(number, "tab na indentação; use espaços")
        content, commented = strip_comment(body)
        content = content.rstrip(" ")
        if not content:
            continue
        if content.startswith("---") or content.startswith("..."):
            raise YamlError(number, "marcador de documento não é aceito")
        lines.append([number, len(raw) - len(body), content, commented])
    return lines


def is_item(content):
    return content == "-" or content.startswith("- ")


def split_flow(inner, number):
    parts, current, quote = [], "", None
    index = 0
    while index < len(inner):
        char = inner[index]
        index += 1
        skip = quoted_pair(inner, index - 1, quote)
        if skip:
            current += inner[index - 1:index - 1 + skip]
            index += skip - 1
            continue
        if quote:
            current += char
            if char == quote:
                quote = None
        elif char in "\"'":
            quote = char
            current += char
        elif char == ",":
            parts.append(current.strip())
            current = ""
        else:
            current += char
    if quote:
        raise YamlError(number, "aspas sem fechamento")
    parts.append(current.strip())
    if any(not part for part in parts):
        raise YamlError(number, "item vazio em lista entre colchetes")
    return parts


def plain(text, number, flow):
    """Accept a plain value only when every YAML reader agrees it is this exact string."""
    if text in ("true", "false"):
        return text == "true"
    if text == "null":
        return None
    if INTEGER.match(text):
        return int(text)
    if text in TYPED_WORDS or text.lower() in SPECIAL_FLOATS:
        raise YamlError(number, f"{text!r} tem tipo implícito em YAML; use aspas")
    first = text[0]
    starts_well = first.isalpha() or first in "_/" or (
        first == "." and len(text) > 1 and (text[1].isalpha() or text[1] == "/"))
    if not starts_well:
        raise YamlError(number, f"valor simples deve começar com letra, '_', '/' ou '.' seguido de letra; use aspas em {text!r}")
    if any(not char.isprintable() for char in text):
        raise YamlError(number, "caractere de controle ou espaço especial em valor simples; use aspas")
    if ": " in text or text.endswith(":"):
        raise YamlError(number, "valor com ':' precisa de aspas")
    if " #" in text:
        raise YamlError(number, "valor com ' #' precisa de aspas")
    if flow and FLOW_INDICATORS.intersection(text):
        raise YamlError(number, "item de lista com ',', '[', ']', '{' ou '}' precisa de aspas")
    return text


def scalar(text, number, flow=False):
    if text[0] in "&*!|>{[":
        raise YamlError(number, f"recurso de YAML fora do subconjunto: {text[0]!r}")
    if text[0] == '"':
        if len(text) < 2 or not text.endswith('"'):
            raise YamlError(number, "aspas duplas sem fechamento")
        result, index, body = "", 0, text[1:-1]
        while index < len(body):
            char = body[index]
            if char == '"':
                raise YamlError(number, "aspas duplas fora do lugar")
            if char == "\\":
                escape = body[index + 1:index + 2]
                if escape not in ESCAPES:
                    raise YamlError(number, f"escape não aceito: \\{escape}")
                result += ESCAPES[escape]
                index += 2
                continue
            result += char
            index += 1
        return result
    if text[0] == "'":
        if len(text) < 2 or not text.endswith("'") or "'" in text[1:-1].replace("''", ""):
            raise YamlError(number, "aspas simples sem fechamento")
        return text[1:-1].replace("''", "'")
    return plain(text, number, flow)


def inline(text, number, commented=False):
    if text.startswith("["):
        if not text.endswith("]"):
            raise YamlError(number, "lista entre colchetes sem fechamento")
        inner = text[1:-1].strip()
        if not inner:
            return []
        values = []
        for part in split_flow(inner, number):
            if part[0] in "[{":
                raise YamlError(number, "lista aninhada não é aceita")
            values.append(scalar(part, number, flow=True))
        return values
    if commented and text[0] not in "\"'":
        raise YamlError(number, "comentário depois de valor simples; use aspas ou ponha o comentário na própria linha")
    return scalar(text, number)


class Parser:
    def __init__(self, lines):
        self.lines = lines
        self.index = 0

    def current(self):
        return self.lines[self.index] if self.index < len(self.lines) else None

    def block(self, indent):
        line = self.current()
        return self.sequence(indent) if is_item(line[2]) else self.mapping(indent)

    def mapping(self, indent):
        result = {}
        while True:
            line = self.current()
            if line is None or line[1] < indent:
                return result
            number, column, content, commented = line
            if column > indent:
                raise YamlError(number, "indentação inesperada")
            if is_item(content):
                return result
            match = KEY.match(content)
            if not match:
                raise YamlError(number, "esperado 'chave: valor'")
            key, rest = match.group(1), match.group(2)
            if key in TYPED_WORDS:
                raise YamlError(number, f"chave {key!r} tem tipo implícito em YAML")
            if key in result:
                raise YamlError(number, f"chave repetida {key!r}")
            self.index += 1
            if rest is not None and rest.strip():
                result[key] = inline(rest.strip(" "), number, commented)
                continue
            following = self.current()
            if following is not None and following[1] > indent:
                result[key] = self.block(following[1])
            elif following is not None and following[1] == indent and is_item(following[2]):
                result[key] = self.sequence(indent)
            else:
                result[key] = None

    def sequence(self, indent):
        result = []
        while True:
            line = self.current()
            if line is None or line[1] < indent:
                return result
            number, column, content, commented = line
            if column > indent:
                raise YamlError(number, "indentação inesperada")
            if not is_item(content):
                return result
            item = content[1:].lstrip(" ")
            if not item:
                self.index += 1
                following = self.current()
                if following is None or following[1] <= indent:
                    result.append(None)
                else:
                    result.append(self.block(following[1]))
            elif KEY.match(item):
                line[1] = column + len(content) - len(item)
                line[2] = item
                result.append(self.mapping(line[1]))
            else:
                self.index += 1
                result.append(inline(item, number, commented))


def load(text):
    lines = logical_lines(text)
    if not lines:
        return None
    parser = Parser(lines)
    value = parser.block(lines[0][1])
    leftover = parser.current()
    if leftover is not None:
        raise YamlError(leftover[0], "conteúdo fora da estrutura")
    return value
