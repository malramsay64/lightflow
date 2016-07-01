
class ImportWorkflowError(RuntimeError):
    pass


class DataStoreNotConnected(RuntimeError):
    pass


class DataStoreIDExists(RuntimeError):
    pass


class DataStoreIDInvalid(RuntimeError):
    pass


class DataStoreDecodeGridfsIdInvalid(RuntimeError):
    pass


class DataStoreDecodeUnknownType(RuntimeError):
    pass


class TaskReturnActionInvalid(RuntimeError):
    pass
