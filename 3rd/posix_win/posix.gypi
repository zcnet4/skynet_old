# 3rd.gypi
{
  'targets': [
  {
	  # 目标工程名
      'target_name': 'posix',
      'type': 'shared_library',
	  #目标工程预处理宏定义
      'defines': [
      ],
	  #目标工程C++ include目录
      'include_dirs': [
      ],
	  #目标工程源代码路径
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
