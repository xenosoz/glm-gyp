#
# glm.gyp
#
{
  'targets': [
    {
      'target_name': 'glm',
      'type': 'none',
      'direct_dependent_settings': {
        'include_dirs': [
          'glm-0.9.3.4/',
        ],
        'conditions': [
          ['OS=="win"', {
            'msvs_settings': {
              'VCCLCompilerTool': {
                'DisableSpecificWarnings': [
                  '4819',
                ],
              },
            },
          }], # OS=="win"
        ],
      },
    }
  ],
}
# vim:sts=2:sw=2:norl
