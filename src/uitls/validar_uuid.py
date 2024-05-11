from uuid import UUID

def validar_uuid(uuid: str | UUID):

    if not uuid:
        return None
    
    if isinstance(uuid, UUID):
        return uuid
    
    if isinstance(uuid, str):
        try:
            uuid_validado = UUID(uuid)
            return uuid_validado
        except Exception:
            raise AttributeError("Formato de uuid inválido.1")
    else:
        raise AttributeError("Formato de uuid inválido.2")
