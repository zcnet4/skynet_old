# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

# This is the "public" ppapi.gyp file, which must have dependencies on the
# redistributable portions of PPAPI only. This prevents circular dependencies
# in the .gyp files (since ppapi_internal depends on parts of Chrome).

{
  'variables': {
    'chromium_code': 1,  # Use higher warning level.
  },
  'target_defaults': {
    'conditions': [
      # Linux shared libraries should always be built -fPIC.
      #
      # TODO(ajwong): For internal pepper plugins, which are statically linked
      # into chrome, do we want to build w/o -fPIC?  If so, how can we express
      # that in the build system?
      #['os_posix == 1 and OS != "mac" and OS != "android"', {
      #  'cflags': ['-fPIC', '-fvisibility=default'],

        # This is needed to make the Linux shlib build happy. Without this,
        # -fvisibility=hidden gets stripped by the exclusion in common.gypi
        # that is triggered when a shared library build is specified.
      #  'cflags/': [['include', '^-fvisibility=default$']],
	  #	'scons_variable_settings': {'SHLIBPREFIX':'',},
      #}],
    ],
	'include_dirs': [
		# ����ȫ�ֿ���Ŀ¼��
		#'..',
		#'../common',
    ],
	#Ŀ�깤��Ԥ����궨��
	'defines': [
		#'DEFINE_ZC_VALUE=ZC',
		#'NOMINMAX',
	],
  },
  'includes': [
	'skynet-src/skynet.gypi',
  ],
  'targets': [
    {
	  # Ŀ�깤����
      'target_name': 'skynet_bin',
      'type': 'executable',
	  # Ŀ�깤����������
      'dependencies': [
	    '3rd/3rd.gyp:lua',
		'skynet',
		'snlua',
		'logger',
		'harbor',
		'harbor2',
		'memory',
		'socketdriver',
      ],
	  #Ŀ�깤��Ԥ����궨��
      'defines': [
      ],
	  #Ŀ�깤��C++ includeĿ¼
      'include_dirs': [
		'.'
      ],
	  #Ŀ�깤��Դ����·��
      'sources': [
		"skynet-src/skynet_main.c",		
	  ],
	  'conditions': [
        ['OS=="win"', {
		  'product_name':'skynet2',
          'defines': [
            'NOUSE_JEMALLOC',
          ],
		  'msvs_disabled_warnings': [
			'4204','4013','4996','4152','4047','4024','4133'
		  ],
		  'msvs_settings': {
              'VCLinkerTool': {
				'AdditionalLibraryDirectories':[
					'3rd',
				],
              },
            },
			'dependencies': [	
				'3rd/3rd.gyp:posix_win',
			],
        }, { # OS != "win",
		  'product_name':'skynet',
          'defines': [
            
          ],
        }]
      ],
    },
  ],
  
}
