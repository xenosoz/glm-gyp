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
      'sources': [
        'glm-0.9.3.4/glm/ext.hpp',
        'glm-0.9.3.4/glm/glm.hpp',
        'glm-0.9.3.4/glm/gtc/half_float.hpp',
        'glm-0.9.3.4/glm/gtc/matrix_access.hpp',
        'glm-0.9.3.4/glm/gtc/matrix_integer.hpp',
        'glm-0.9.3.4/glm/gtc/matrix_inverse.hpp',
        'glm-0.9.3.4/glm/gtc/matrix_transform.hpp',
        'glm-0.9.3.4/glm/gtc/quaternion.hpp',
        'glm-0.9.3.4/glm/gtc/swizzle.hpp',
        'glm-0.9.3.4/glm/gtc/type_precision.hpp',
        'glm-0.9.3.4/glm/gtc/type_ptr.hpp',
        'glm-0.9.3.4/glm/gtx/associated_min_max.hpp',
        'glm-0.9.3.4/glm/gtx/bit.hpp',
        'glm-0.9.3.4/glm/gtx/closest_point.hpp',
        'glm-0.9.3.4/glm/gtx/color_cast.hpp',
        'glm-0.9.3.4/glm/gtx/color_space.hpp',
        'glm-0.9.3.4/glm/gtx/color_space_YCoCg.hpp',
        'glm-0.9.3.4/glm/gtx/compatibility.hpp',
        'glm-0.9.3.4/glm/gtx/component_wise.hpp',
        'glm-0.9.3.4/glm/gtx/epsilon.hpp',
        'glm-0.9.3.4/glm/gtx/euler_angles.hpp',
        'glm-0.9.3.4/glm/gtx/extend.hpp',
        'glm-0.9.3.4/glm/gtx/extented_min_max.hpp',
        'glm-0.9.3.4/glm/gtx/fast_exponential.hpp',
        'glm-0.9.3.4/glm/gtx/fast_square_root.hpp',
        'glm-0.9.3.4/glm/gtx/fast_trigonometry.hpp',
        'glm-0.9.3.4/glm/gtx/gradient_paint.hpp',
        'glm-0.9.3.4/glm/gtx/handed_coordinate_space.hpp',
        'glm-0.9.3.4/glm/gtx/inertia.hpp',
        'glm-0.9.3.4/glm/gtx/int_10_10_10_2.hpp',
        'glm-0.9.3.4/glm/gtx/integer.hpp',
        'glm-0.9.3.4/glm/gtx/intersect.hpp',
        'glm-0.9.3.4/glm/gtx/log_base.hpp',
        'glm-0.9.3.4/glm/gtx/matrix_cross_product.hpp',
        'glm-0.9.3.4/glm/gtx/matrix_interpolation.hpp',
        'glm-0.9.3.4/glm/gtx/matrix_major_storage.hpp',
        'glm-0.9.3.4/glm/gtx/matrix_operation.hpp',
        'glm-0.9.3.4/glm/gtx/matrix_query.hpp',
        'glm-0.9.3.4/glm/gtx/mixed_product.hpp',
        'glm-0.9.3.4/glm/gtx/multiple.hpp',
        'glm-0.9.3.4/glm/gtx/noise.hpp',
        'glm-0.9.3.4/glm/gtx/norm.hpp',
        'glm-0.9.3.4/glm/gtx/normal.hpp',
        'glm-0.9.3.4/glm/gtx/normalize_dot.hpp',
        'glm-0.9.3.4/glm/gtx/number_precision.hpp',
        'glm-0.9.3.4/glm/gtx/ocl_type.hpp',
        'glm-0.9.3.4/glm/gtx/optimum_pow.hpp',
        'glm-0.9.3.4/glm/gtx/orthonormalize.hpp',
        'glm-0.9.3.4/glm/gtx/perpendicular.hpp',
        'glm-0.9.3.4/glm/gtx/polar_coordinates.hpp',
        'glm-0.9.3.4/glm/gtx/projection.hpp',
        'glm-0.9.3.4/glm/gtx/quaternion.hpp',
        'glm-0.9.3.4/glm/gtx/random.hpp',
        'glm-0.9.3.4/glm/gtx/raw_data.hpp',
        'glm-0.9.3.4/glm/gtx/reciprocal.hpp',
        'glm-0.9.3.4/glm/gtx/rotate_vector.hpp',
        'glm-0.9.3.4/glm/gtx/simd_mat4.hpp',
        'glm-0.9.3.4/glm/gtx/simd_vec4.hpp',
        'glm-0.9.3.4/glm/gtx/spline.hpp',
        'glm-0.9.3.4/glm/gtx/std_based_type.hpp',
        'glm-0.9.3.4/glm/gtx/string_cast.hpp',
        'glm-0.9.3.4/glm/gtx/transform.hpp',
        'glm-0.9.3.4/glm/gtx/transform2.hpp',
        'glm-0.9.3.4/glm/gtx/ulp.hpp',
        'glm-0.9.3.4/glm/gtx/vec1.hpp',
        'glm-0.9.3.4/glm/gtx/vector_access.hpp',
        'glm-0.9.3.4/glm/gtx/vector_angle.hpp',
        'glm-0.9.3.4/glm/gtx/vector_query.hpp',
        'glm-0.9.3.4/glm/gtx/verbose_operator.hpp',
        'glm-0.9.3.4/glm/gtx/wrap.hpp',
        'glm-0.9.3.4/glm/virtrev/xstream.hpp',
      ],
    }
  ],
}
# vim:sts=2:sw=2:norl
