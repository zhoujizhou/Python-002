学习笔记
关于线程安全：
单例模式使用双重锁机制保证线程安全

Class Singleton(object):
      _instance_lock = threading.Lock()

      def __new__(cls,*args,**kwargs):
            if not hasattr(Singleton,"_instance"):
                  with Singleton._instance_lock:
                        if not hasattr(Singleton,"_instance"):
                              Singleton._instance = object.__new__(cls)
            return Singleton._instance