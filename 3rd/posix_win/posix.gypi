# 3rd.gypi
{
  'targets': [
  {
	  # Ŀ�깤����
      'target_name': 'posix',
      'type': 'shared_library',
	  #Ŀ�깤��Ԥ����궨��
      'defines': [
      ],
	  #Ŀ�깤��C++ includeĿ¼
      'include_dirs': [
      ],
	  #Ŀ�깤��Դ����·��
      'sources': [
		"arpa/inet.h",
		"cpoll/cpoll.h",
		"cpoll/cpoll.cpp",
		"netinet/in.h",
		"netinet/tcp.h",
		"sys/file.h",
		"sys/socket.h",
		"atomic_lock.c",
		"atomic_lock.h",
		"dlfcn.c",
		"dlfcn.h",
		"pthread.h",
		"sched.h",
		"semaphore.h",
		"unistd.c",
		"unistd.h",
	  ],
      'direct_dependent_settings': {
        'include_dirs': [
          '..',
        ],
      },
    },
  ],
}
