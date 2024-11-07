from rest_framework.fields import Field
from rest_framework.serializers import Serializer


def inline_serializer(
    name: str,
    fields: dict[str, Field],
    docstring: str = "",
    **kwargs,
) -> Serializer:
    """динамически создает класс сериализатора в Django REST Framework.
    1. Параметры:
    - name: строка, задающая имя создаваемого сериализатора.
    - fields: словарь, содержащий поля сериализатора, где ключи — это имена полей, 
    а значения — объекты типа Field.
    - docstring: (опционально) строка с документацией для сериализатора.
    - **kwargs: дополнительные аргументы для инициализации сериализатора.
    2. Создание класса:
    - serializer_class = type(name, (Serializer,), fields): создается новый класс сериализатора, 
    который наследуется от Serializer, с заданными полями.
    3. Документация:
    - serializer_class.doc = docstring: присваивает строку документации классу.
    4. Возврат экземпляра:
    - return serializer_class(**kwargs): возвращает экземпляр созданного сериализатора, 
    передавая дополнительные параметры. 
    Используется для создания кастомных сериализаторов на лету."""
    
    serializer_class = type(name, (Serializer,), fields)
    serializer_class.__doc__ = docstring
    return serializer_class(**kwargs)
